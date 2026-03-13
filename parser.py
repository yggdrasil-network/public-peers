import os
import re
import json
import csv

def extract_nodes_from_file(file_path):
    addresses = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r'`((tcp|tls|quic|ws|wss)://([a-z0-9\.\-:\[\]]+(:[0-9]+)?(\?[^\s]*)?))`'
    matches = re.findall(pattern, content)

    for match in matches:
        addresses.append(f"{match[0]}") 

    return addresses

def main():
    all_nodes = {}
    # Recursive search all .md files
    for root, dirs, files in os.walk('.'):
        # Save parent directory name
        parent_directory = os.path.basename(root)

        for filename in files:
            if filename.endswith('.md'):
                file_path = os.path.join(root, filename)
                addresses = extract_nodes_from_file(file_path)

                if addresses:
                    subcategory = os.path.splitext(filename)[0]  # Remove .md from name

                    if parent_directory not in all_nodes:
                        all_nodes[parent_directory] = {}
                    all_nodes[parent_directory][subcategory] = addresses

    # Save in JSON file
    with open('nodes.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_nodes, json_file, ensure_ascii=False, indent=4)

    # Save in CSV file
    with open('nodes.csv', 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Category", "Subcategory", "URI"])  # Titles

        for parent, subcategories in all_nodes.items():
            for subcategory, addresses in subcategories.items():
                for address in addresses:
                    csv_writer.writerow([parent, subcategory, address])  # Contents

if __name__ == "__main__":
    main()
