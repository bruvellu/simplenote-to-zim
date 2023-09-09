#!/usr/bin/env python3

'''Simplenote to Zim

A script to convert your notes from Simplenote to Zim Desktop Wiki.
    
Usage: simplenote_to_zim.py notes.json

Author: Bruno C. Vellutini - https://brunovellutini.com

Curiosity: An AI assisted me in creating this script. It was an interesting
experience. See: https://brunovellutini.com/posts/simplenote-to-zim/
'''

import sys
import json
import os
import re
from datetime import datetime

def extract_title(content):
    # Extract the title from the first line of the content
    lines = content.split('\n')
    title = lines[0].strip()

    return title

def format_creation_date(creation_date):
    # Format the creation date as "Tuesday 25 July 2023"
    date = datetime.fromisoformat(creation_date)
    formatted_date = date.strftime("%A %d %B %Y")

    return formatted_date

def format_creation_date_iso(creation_date):
    # Format the creation date as ISO 8601 with offset
    date = datetime.fromisoformat(creation_date)
    formatted_date = date.astimezone().replace(microsecond=0).isoformat()
    
    return formatted_date

def format_tags(tags):
    # Format the tags with "@" before each tag and separate with " "
    formatted_tags = [f"@{tag}" for tag in tags]
    
    return " ".join(formatted_tags)

def sanitize_filename(filename):
    # Remove special characters and replace spaces with underscores
    sanitized_filename = re.sub(r'[\\/:\*\?"<>\|#]', '', filename)
    sanitized_filename = sanitized_filename.replace(' ', '_')

    # Ensure filename does not start with an underscore
    if sanitized_filename.startswith('_'):
        sanitized_filename = sanitized_filename[1:]

    return sanitized_filename

def convert_to_zim(simplenote_file):
    with open(simplenote_file, 'r') as f:
        data = json.load(f)
        notes = data['activeNotes']

    for note in notes:
        content = note['content']
        creation_date = note['creationDate']

        # Extract the title from the content
        title = extract_title(content)

        # Remove the title from the content
        lines = content.split('\n')[1:]

        # Remove leading/trailing whitespace
        content = '\n'.join(lines).strip()

        # Sanitize the filename
        sanitized_title = sanitize_filename(title)

        # Generate the filename by replacing spaces with underscores
        filename = f"{sanitized_title}.txt"

        with open(filename, 'w') as f:
            # Write the Zim Desktop Wiki format
            f.write("Content-Type: text/x-zim-wiki\n")
            f.write("Wiki-Format: zim 0.6\n")
            f.write(f"Creation-Date: {format_creation_date_iso(creation_date)}\n\n")
            f.write(f"====== {title} ======\n")
            f.write(f"Created {format_creation_date(creation_date)}\n\n")

            if 'tags' in note:
                tags = note['tags']
                formatted_tags = format_tags(tags)
                # Add newline after tags
                f.write(f"{formatted_tags}\n\n")

            # Remove extra blank line
            f.write(f"{content}\n")

    print("Conversion completed successfully!")

# Usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide the path to the Simplenote JSON file as an argument.")
    else:
        simplenote_file = sys.argv[1]
        convert_to_zim(simplenote_file)

