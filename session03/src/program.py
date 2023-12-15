import os
import csv
import re 
import json 

directory = 'temp/jjwt'

frequency = dict()

# ---------- Helpers ------------------------------ 
def tokenize_comments(text):
    tokens = []
    comments = re.findall(r'//[^\n]*|/\*.*?\*/', text, re.DOTALL)
    for comment in comments:
        for token in re.split(r'\W+', comment):
            tokens.append(token.lower())  # Convert token to lowercase

    return tokens
    

# ---------- First Pass ------------------------------ 
# Collect the frequency of tokens in the comments.
for root, dirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(root, file)

        if path.endswith(".java"):
            # Read the file into text
            with open(path, 'r') as file:
                text = file.read()

                for token in tokenize_comments(text):
                    frequency[token] = frequency.get(token, 0) + 1

# ---------- Second Pass ------------------------------ 
# Use frequency to remove tokens that are very frequent.

# Open the CSV file in write mode
with open('temp/output.json', 'w') as dumpfile:
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)

            if path.endswith(".java"):
                # Read the file into text
                with open(path, 'r') as file:
                    metrics = dict()
                    metrics["path"] = path

                    content = file.read()
                    
                    # Reading commits and weighting them.
                    size_comments = 0
                    size_comments_w = 0
                
                    for token in tokenize_comments(content):
                        size_comments += len(token)
                        size_comments_w += len(token) / frequency[token]

                    metrics["size_comments"] = size_comments
                    metrics["size_comments_w"] = size_comments_w

                    # Metrics from "jbarber07"!

                    # Get the size of the file in bytes
                    metrics["size"] = os.path.getsize(path)

                    # Count the occurrences of public, private, and protected keywords
                    metrics["public_count"] = len(re.findall(r'\bpublic\b', content))
                    metrics["private_count"] = len(re.findall(r'\bprivate\b', content))
                    metrics["protected_count"] = len(re.findall(r'\bprotected\b', content))

                    # Count the number of methods and fields
                    metrics["method_count"] = len(re.findall(r'\b(public|private|protected|static|final|abstract|synchronized|native|strictfp)\s+[\w<>\[\]]+\s+\w+\s*\(.*?\)', content))
                    metrics["field_count"] = len(re.findall(r'\b(public|private|protected|static|final|transient|volatile)\s+[\w<>\[\]]+\s+\w+\s*(=|;)', content))

                    # Check if the content contains inheritance or implementation keywords
                    metrics["inheritance_info"] = bool(re.search(r'\bextends\b|\bimplements\b', content))

                    # Count the number of constructors, dependencies, and annotations
                    metrics["dependency_count"] = len(set(re.findall(r'import\s+[\w.]+;', content)))
                    metrics["annotation_count"] = len(re.findall(r'@\w+', content))

                    # Small trick to not always have to write the header.
                    # Using line-delimited json (can later be read by pd.read_json('newresults.json', lines=True)).
                    json.dump(metrics, dumpfile)
                    dumpfile.write("\n")