# Weather Scraper - Created by Nathenael Tamirat
# This script fetches live weather data using web scraping.
# It extracts temperature, weather conditions, and location.

import requests
from bs4 import BeautifulSoup

# Target website (Reliable weather source)
URL = "https://www.timeanddate.com/weather/"

# Function to fetch weather data for a given city
def get_weather(city):
    city = city.replace(" ", "-")  # Adjust city name for the URL format
    page = requests.get(URL + city)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract weather details
    temperature = soup.find("div", class_="h2").text.strip()
    condition = soup.find("p").text.strip()
    
    # Display weather information
    print(f"\nWeather in {city.replace('-', ' ')}:")
    print(f"Temperature: {temperature}")
    print(f"Condition: {condition}")

# Input from the user
city = input("Enter a city: ").strip()
get_weather(city)
