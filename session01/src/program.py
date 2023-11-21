import os
import csv

directory = "temp/jjwt"

# https://docs.python.org/3/library/csv.html
with open("temp/output.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["path", "import"])
        
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)

            if path.endswith(".java"):
                with open(path, 'r') as file:
                    text = file.read()

                    writer.writerow([path, text.count("import")])

