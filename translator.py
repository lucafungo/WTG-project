import os
import json
from googletrans import Translator
from api_caller import yesterday
import zipfile

# Define the input and output directories
input_dir = f'{yesterday}'
output_dir = f'{yesterday}_italian'


# Create the output directory if it doesn't already exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a translator object
translator = Translator()

# Loop through all the files in the input directory
for filename in os.listdir(input_dir):
    # Check that the file is a text file
    if filename.endswith(".txt"):
        # Read the input file
        with open(os.path.join(input_dir, filename), "r") as input_file:
            input_text = input_file.read()

        # Check that the input text is not empty
        if input_text.strip() == "":
            print(f"Skipping {filename} because it is empty.")
            continue

        # Translate the input text to Italian
        try:
            output_text = translator.translate(input_text, dest="it").text
        except Exception as e:
            print(f"Error translating {filename}: {e}")
            continue

        # Write the translated text to a file in the output directory
        with open(os.path.join(output_dir, filename), "w") as output_file:
            output_file.write(output_text)

        print(f"Translated {filename} from English to Italian.")

# Define the name of the zipfile
zip_file_name_ita = f'{yesterday}_italian.zip'

# Create a new zip file and add the .txt files to it
with zipfile.ZipFile(zip_file_name_ita, mode='w') as zip_file:
    for file_name in os.listdir(f'{yesterday}'):
        if file_name.endswith('.txt'):
            file_path = os.path.join(f'{yesterday}', file_name)
            # Add the file to the zip file
            zip_file.write(file_path)