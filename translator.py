import os
from textblob import TextBlob
from api_caller import yesterday

# Set the source and destination directories
src_dir = f'{yesterday}'
dst_dir = f'{yesterday}_ita'

# Create the destination directory if it doesn't exist
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Loop through each file in the source directory
for filename in os.listdir(src_dir):
    if filename.endswith('.txt'):
        # Open the file and read its contents
        with open(os.path.join(src_dir, filename), 'r', encoding='utf-8') as f:
            text = f.read()

        # Translate the text using TextBlob
        blob = TextBlob(text)
        translated_text = str(blob.translate(to='ita')) # Translate to Italian

        # Save the translated text to a new file in the destination directory
        dst_filename = filename[:-4] + '_translated.txt'
        with open(os.path.join(dst_dir, dst_filename), 'w', encoding='utf-8') as f:
            f.write(translated_text)
