# Multimodal Dataset Collection & Analysis

## Task 1: Multimodal Dataset Collection
This project involves collecting, curating, and organizing datasets across multiple modalities, including images, text, audio, and structured weather data. Automated scripts were used for scraping, downloading, and preprocessing data.

### Subtasks:
#### 1_a: Image Dataset Collection
- Collected images across 20 categories using automated web scraping.
- Organized images into labeled folders.
- Metadata (URLs, filenames, resolutions) stored in a CSV file.

#### 1_b: Text Dataset Collection
- Scraped textual data from selected websites for 20 different topics.
- Processed the text using NLP techniques like stopword removal and HTML tag stripping.
- Organized the data into 20 text files.

#### 1_c: Audio Dataset Collection
- Recorded audio streams from online AM/FM radio stations.
- Stored 30 recordings in WAV/MP3 format with metadata (station name, timestamp, duration).

#### 1_d: Weather Dataset Collection
- Collected real-time and historical weather data from an open-source API.
- Recorded data for 20 Indian cities, tracking temperature, humidity, and wind speed.
- Stored observations in a structured CSV file.

#### 1_e: Indian Data Analysis
- Selected a dataset from the Indian Government's data portal (https://data.gov.in).
- Cleaned and preprocessed the dataset.
- Conducted exploratory data analysis (EDA) to identify patterns and trends.

## Task 2: Flags & Anthems Analysis
This project analyzes national flags' visual characteristics and national anthems' linguistic features to identify cultural and historical correlations.

### Subtasks:
#### 3_a: Data Collection
- Downloaded national flags for 100+ countries.
- Collected English translations of their anthems.
- Retrieved audio compositions of selected national anthems.

#### 3_b: Visual Analysis
- Performed data analysis on flag images to extract dominant colors and patterns.
- Compared findings with historical and cultural contexts.

#### 3_c: Textual Analysis
- Processed anthem lyrics by removing stop words and extracting key themes.
- Identified patterns in language, sentiment, and recurring words.

#### 3_d: Audio Analysis
- Analyzed the composition of national anthems.
- Explored rhythmic patterns, tempo, and commonalities across different regions.

#### 3_e: Multimodal Correlation
- Investigated relationships between flag colors, anthem lyrics, and audio compositions.
- Explored connections between cultural identity and symbolic representation in data.



## Technologies Used
- **Web Scraping**: `selenium`, `BeautifulSoup`, `requests`
- **Data Processing**: `pandas`, `numpy`
- **NLP**: `NLTK`, `spaCy`
- **Audio Processing**: `pydub`, `librosa`
- **Visualization**: `matplotlib`, `seaborn`, `plotly`

