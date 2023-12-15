import os
import csv
import re

# Define the directory to search for files
directory = 'temp/jjwt'

# Function to count comments in the content
def count_comments(content):
    # Find single line comments
    single_line_comments = re.findall(r'//.*', content)
    # Find block comments
    block_comments = re.findall(r'/\*[\s\S]*?\*/', content)
    # Return the total count of comments
    return len(single_line_comments) + len(block_comments)

# Open the output.csv file in write mode
with open('temp/output.csv', 'w', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Path', 'Comment Count', 'Size (Bytes)', 'Public Count', 'Private Count', 'Protected Count', 'Method Count', 'Field Count', 'Inheritance Info', 'Dependency Count', 'Annotation Count'])

    # Recursively walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the full path of the file
            path = os.path.join(root, file)

            # Process only Java files
            if path.endswith(".java"):
                # Open the Java file in read mode
                with open(path, 'r') as java_file:
                    # Read the content of the Java file
                    content = java_file.read()

                    # Count the number of comments in the content
                    comment_count = count_comments(content)

                    # Get the size of the file in bytes
                    size = os.path.getsize(path)

                    # Count the occurrences of public, private, and protected keywords
                    public_count = len(re.findall(r'\bpublic\b', content))
                    private_count = len(re.findall(r'\bprivate\b', content))
                    protected_count = len(re.findall(r'\bprotected\b', content))

                    # Count the number of methods and fields
                    method_count = len(re.findall(r'\b(public|private|protected|static|final|abstract|synchronized|native|strictfp)\s+[\w<>\[\]]+\s+\w+\s*\(.*?\)', content))
                    field_count = len(re.findall(r'\b(public|private|protected|static|final|transient|volatile)\s+[\w<>\[\]]+\s+\w+\s*(=|;)', content))

                    # Check if the content contains inheritance or implementation keywords
                    inheritance_info = bool(re.search(r'\bextends\b|\bimplements\b', content))

                    # Count the number of constructors, dependencies, and annotations
                    dependency_count = len(set(re.findall(r'import\s+[\w.]+;', content)))
                    annotation_count = len(re.findall(r'@\w+', content))

                    # Write the row to the CSV file
                    writer.writerow([path, comment_count, size, public_count, private_count, protected_count, method_count, field_count, inheritance_info, dependency_count, annotation_count])
