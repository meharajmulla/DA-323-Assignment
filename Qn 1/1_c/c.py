import os
import time
import datetime
import subprocess
import csv

# Define radio streams and their URLs (Modified)
radio_stations = {
    "Chillhop_Radio": "http://stream.chillhop.com/chillhop.mp3",
    "Deep_House_Lounge": "http://199.189.87.165:8000/stream",
    "Ambient_Sleeping_Pill": "http://listen.radiosleep.com/ambient",
    "LoFi_Hip_Hop": "http://stream.radioboss.fm:8040/stream",
    "Smooth_Jazz": "http://91.121.165.109:8000/stream",
    "Classical_Piano": "http://streams.977music.com/classicalpiano",
    "Nature_Sounds": "http://streaming.tdiradio.com:8000/bestnature.mp3",
    "Indie_Folk": "http://icecast.radioio.com/indiefolk.mp3",
    "Reggae_Vibes": "http://192.99.146.131:8000/stream",
    "Electronic_Dance": "http://199.189.87.165:8000/stream",
}

# Directory to store recordings
output_dir = "recordings"
os.makedirs(output_dir, exist_ok=True)

# Function to record audio
def record_audio(station_name, stream_url, duration=60):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{station_name}_{timestamp}.mp3"
    filepath = os.path.join(output_dir, filename)

    print(f"Recording {station_name} for {duration} seconds...")

    # Run ffmpeg command to record the stream
    command = [
        "ffmpeg", "-i", stream_url, "-t", str(duration), "-y",
        "-acodec", "mp3", filepath
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return filename, filepath, timestamp, duration

# Record 30 audio samples from different stations
audio_metadata = []
for i in range(30):
    station_name, stream_url = list(radio_stations.items())[i % len(radio_stations)]
    duration = 30 + (i % 3) * 30  # Vary duration between 30-90s

    try:
        filename, filepath, timestamp, duration = record_audio(station_name, stream_url, duration)
        audio_metadata.append([station_name, filename, timestamp, duration])
        time.sleep(2)  # Small delay to avoid overwhelming the system
    except Exception as e:
        print(f"Error recording {station_name}: {e}")

print("Recording complete!")

# Save metadata to CSV
metadata_file = os.path.join(output_dir, "audio_metadata.csv")
with open(metadata_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Station Name", "Filename", "Timestamp", "Duration"])
    writer.writerows(audio_metadata)

print(f"Metadata saved to {metadata_file}")