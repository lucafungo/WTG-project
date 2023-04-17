## TODO: clean the result to have a clean text

# Import required libraries
import requests
from bs4 import BeautifulSoup
import csv
import os
from api_caller import yesterday
import zipfile
import boto3
from keys import ACCESS_KEY, SECRET_ACCESS_KEY, BUCKET_NAME

# Create a directory with the current date to store the articles
if not os.path.exists(f'{yesterday}'):
    os.makedirs(f'{yesterday}')

# Scrape articles from The Guardian website using links from the CSV file
with open(f'{yesterday}.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    article_count = 0
    for row in reader:
        article_count += 1
        # Define the filename for each article from the corresponding row in the CSV file
        title = row['webTitle']
        link = row['webUrl']
        
        # Use BeautifulSoup to extract the article text from the HTML content
        req = requests.get(link)
        soup = BeautifulSoup(req.content, 'html.parser')
        
        # Find all paragraphs in the article using the 'p' tag and the class names used by The Guardian
        paragraphs = soup.find_all('p', class_='dcr-n6w1lc')
        if not paragraphs:
            paragraphs = soup.find_all('p', class_='dcr-1gesh1i')
        
        # Concatenate all paragraphs to create the full article text
        full_article = ""
        for paragraph in paragraphs:
            full_article += paragraph.text.strip() + " "

        # Save the full article text to a text file in the directory
        if full_article != "":
            # Remove invalid characters from the title
            title = "".join([c for c in title if c.isalnum() or c in "._- "])
        
        # Save the full article text to a text file in the directory
        if full_article != "":
            with open(f'{yesterday}/{title}.txt', 'w') as f:
                f.write(full_article)
                print(f'Article {article_count} saved as {title}.txt')

# Define the name of the zipfile
zip_file_name = f'{yesterday}.zip'

# Create a new zip file and add the .txt files to it
with zipfile.ZipFile(zip_file_name, mode='w') as zip_file:
    for file_name in os.listdir(f'{yesterday}'):
        if file_name.endswith('.txt'):
            file_path = os.path.join(f'{yesterday}', file_name)
            # Add the file to the zip file
            zip_file.write(file_path)

# Create a connection to the S3 service
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY)

# Upload the file to the S3 bucket
s3.upload_file(zip_file_name, BUCKET_NAME, zip_file_name)
