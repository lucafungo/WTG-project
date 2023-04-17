import csv
from textblob import TextBlob
import os
from api_caller import yesterday
import boto3
from keys import ACCESS_KEY, SECRET_ACCESS_KEY, BUCKET_NAME

# Create a connection to the S3 service
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_ACCESS_KEY)

# Define origin folder, the files to analyse will be found here
folder = f'{yesterday}'

# Define the name of the file that will be created by the script with the output
output_file = f'{yesterday}sentiment_analysis.csv'

# Define a list where all the analisys will be stored
analysis_list = []

# This create and open the destination file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['filename', 'analysis'])
    # Here starts the analisys process opening the origin folder
    for filename in os.listdir(folder):
        # Grab all the text files referring to the articles
        if filename.endswith('.txt'):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r') as file:
                text = file.read()
                # Initalise and process blob analisys
                blob = TextBlob(text)
                analysis = blob.sentiment.polarity
                writer.writerow([filename, analysis])
                # Print a confirtmation message on terminal for all the analisys done
                print(f'Sentiment analysis for {filename}: {analysis}')
                # Append al the analisys to the destination file, exluding the one scoring zero,
                # as most likely the are result of an error in the analisys
                if analysis != 0:
                    analysis_list.append(analysis)

# Upload the file to the S3 bucket
s3.upload_file(output_file, BUCKET_NAME, output_file)


