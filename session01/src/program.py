import os
import csv
import re

directory = 'temp/jjwt'

# Open the CSV file in write mode
with open('temp/output.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['path', 'comment', "size"])

    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)

            if path.endswith(".java"):
                # Read the file into text
                with open(path, 'r') as file:
                    text = file.read()

                    # Count the number of Java comments
                    comment_count = len(re.findall(r'//.*|/\*.*?\*/', text, re.DOTALL))

                    # Size of the file.
                    size = len(text)

                    # Write the path and comment count to the CSV file
                    writer.writerow([path, comment_count, size])
