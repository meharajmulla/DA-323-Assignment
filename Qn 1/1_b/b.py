import os
import requests
from bs4 import BeautifulSoup
import csv
import time
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Ensure necessary nltk data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Define categories and websites (Modified)
categories = {
    "Technology": ["https://www.techcrunch.com/", "https://www.wired.com/", "https://www.theverge.com/"],
    "Space Exploration": ["https://www.nasa.gov/", "https://www.space.com/", "https://www.esa.int/"],
    "Programming": ["https://stackoverflow.com/questions", "https://www.freecodecamp.org/news/", "https://www.geeksforgeeks.org/"],
    "Gaming": ["https://www.ign.com/", "https://www.gamespot.com/", "https://www.polygon.com/"],
    "Books": ["https://www.goodreads.com/news", "https://www.nytimes.com/books/", "https://www.penguinrandomhouse.com/"],
    "Music": ["https://www.billboard.com/", "https://pitchfork.com/", "https://www.rollingstone.com/music/"],
    "Cryptocurrency": ["https://www.coindesk.com/", "https://cointelegraph.com/", "https://www.binance.com/en/blog"],
    "Startups": ["https://techcrunch.com/startups/", "https://www.entrepreneur.com/topic/startups", "https://www.ycombinator.com/blog/"],
    "Sustainability": ["https://www.greenbiz.com/", "https://www.earth.org/", "https://www.nationalgeographic.com/environment/"],
    "Personal Development": ["https://www.psychologytoday.com/", "https://www.mindful.org/", "https://www.developgoodhabits.com/"],
    "Cooking Recipes": ["https://www.allrecipes.com/", "https://www.bbcgoodfood.com/", "https://www.simplyrecipes.com/"],
    "DIY Projects": ["https://www.instructables.com/", "https://www.diynetwork.com/", "https://www.familyhandyman.com/"],
    "Gardening": ["https://www.gardenersworld.com/", "https://www.rhs.org.uk/", "https://www.almanac.com/gardening"],
    "Fitness": ["https://www.menshealth.com/fitness/", "https://www.womenshealthmag.com/fitness/", "https://www.muscleandfitness.com/"],
    "Mental Health": ["https://www.mhanational.org/", "https://www.nimh.nih.gov/", "https://www.nami.org/"],
    "Product Reviews": ["https://www.cnet.com/reviews/", "https://www.pcmag.com/reviews", "https://www.techradar.com/reviews"],
    "Travel Guides": ["https://www.travelandleisure.com/", "https://www.cntraveler.com/", "https://www.fodors.com/"],
    "Automotive": ["https://www.caranddriver.com/", "https://www.motortrend.com/", "https://www.topgear.com/"],
    "Investing": ["https://www.fool.com/", "https://www.wsj.com/finance", "https://www.reuters.com/business/finance/"],
    "Data Science": ["https://towardsdatascience.com/", "https://www.kdnuggets.com/", "https://www.datasciencecentral.com/"]
}

# Function to clean text
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize text
    stop_words = set(stopwords.words("english"))  # Get stop words
    cleaned_text = " ".join([word for word in tokens if word not in stop_words])  # Remove stopwords
    return cleaned_text

# Function to scrape articles
def scrape_category(category, urls):
    text_data = []
    
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract title, content, and date if available
            title = soup.title.string if soup.title else "No Title"
            content = " ".join([p.text for p in soup.find_all("p")])
            cleaned_content = clean_text(content)

            text_data.append(f"Title: {title}\nContent: {cleaned_content}\n\n")
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")

    return text_data

# Create text files for each category
for category, urls in categories.items():
    print(f"Scraping {category}...")
    articles = scrape_category(category, urls)
    
    with open(f"{category}.txt", "w", encoding="utf-8") as file:
        file.writelines(articles)

print("Scraping complete! Data saved to text files.")