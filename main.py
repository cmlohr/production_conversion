import os
import docx2txt
import re

# Set the file paths
directory_path = '/Users/cmloh/Downloads/2022 Events'
output_file_path = '/Users/cmloh/Downloads/2022 Events/events_file.txt'

# Convert the docx files to a single plain text document
combined_text = ''
for file_name in os.listdir(directory_path):
    if file_name.endswith('.docx'):
        file_path = os.path.join(directory_path, file_name)
        text = docx2txt.process(file_path)
        combined_text += text

# Remove integers
line_without_integers = re.sub(r'\d+', '', combined_text)

# Write the modified text to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(line_without_integers)
