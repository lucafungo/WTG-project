# Import required libraries
import requests
import datetime
import json
import csv
import os
from keys import apikey

# Set the topic and date for the API call
topic = 'politics'

date = datetime.date.today() - datetime.timedelta(days=1)
yesterday = date.strftime('%Y-%m-%d')

# API key for accessing the Guardian API
key = apikey

# Create the API link
api_link = f"https://content.guardianapis.com/search?section={topic}&from-date={yesterday}&to-date={yesterday}&page-size=50&api-key={key}"

# Send the API request and save the JSON response
response = requests.get(api_link)
with open(f"{yesterday}.json", "w") as outfile:
    json.dump(response.json(), outfile)

# Extract the articles from the JSON data
with open(f'{yesterday}.json', 'r') as f:
    data = json.load(f)
politics_results = [result for result in data['response']
                    ['results'] if result['sectionId'] == 'politics']

# Create a CSV file to store the articles and write the data
with open(f'{yesterday}.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(['webTitle', 'webUrl'])
    for result in politics_results:
        writer.writerow([result['webTitle'], result['webUrl']])

# Delete the JSON file
os.remove(f"{yesterday}.json")
