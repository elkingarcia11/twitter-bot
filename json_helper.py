import os
import json

def merge_json_files(input_folder, output_file):
    merged_verses = []

    # Iterate over each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            filepath = os.path.join(input_folder, filename)
            
            try:
                with open(filepath, 'r') as file:
                    data = json.load(file)
                    
                    # Extract book name and chapters
                    book = data.get('book', '')
                    chapters = data.get('chapters', [])
                    print(f"Working on book {book}")
                    # Iterate over chapters
                    for chapter_data in chapters:
                        chapter_number = chapter_data.get('chapter', '')
                        verses = chapter_data.get('verses', [])

                        # Iterate over verses
                        for verse_data in verses:
                            verse_number = verse_data.get('verse', '')
                            verse_text = verse_data.get('text', '')

                            # Create the merged verse object
                            merged_verse = {
                                'text': verse_text,
                                'source': f'{book} {chapter_number}:{verse_number}'
                            }

                            # Append to the list of merged verses
                            merged_verses.append(merged_verse)
            except Exception as e:
                print(f"Error processing file '{filename}': {e}")
                continue  # Continue to the next file
    
    # Write merged verses to the output file
    with open(output_file, 'w') as outfile:
        json.dump(merged_verses, outfile, indent=2)

    print(f'Merged verses written to {output_file}')

# Example usage:
input_folder = './json_data'
output_file = './merged_data.json'
merge_json_files(input_folder, output_file)
