import json
import csv
import os



def flatten_json(nested_json, parent_key='', sep='_'):
    """
    Flatten a nested json file.
    """
    items = []
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_json({f"{new_key}{sep}{i}": item}, '', sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def json_to_csv(json_file, csv_file):
    # Load JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Ensure the data is a list of dictionaries
    if not isinstance(data, list):
        data = [data]

    # Flatten the JSON data
    flat_data = [flatten_json(record) for record in data]

    # Extract fieldnames from the first record
    fieldnames = set()
    for record in flat_data:
        fieldnames.update(record.keys())
    fieldnames = sorted(fieldnames)  # Sort fieldnames to maintain consistent column order

    # Write CSV data
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in flat_data:
            writer.writerow(row)
    print ('The file has been converted successfully and has been placed into the output folder')

input_path = "./input/"
output_path = "./output/"
replaceExistingFile = False
#maxWidth=64
#ColorAlternateRows = True
#fillColor = 'F0F0F0F0'
#hideEmptyColumns = True
for path, dir, files in os.walk(input_path):
    if len(files) == 0:
        print("Please place json file in the correct format into the /input folder")
    for file in files:
        if file.endswith(".tgz") or file.endswith(".zip"):
            try:
                print("zip/tgz file support to be added later: " + file)
            except Exception as err:
                print(f'Error processing {input_path + file} {err}')
        elif file.endswith(".json"):
            print("Parsing... " + file)
    
            json_file = input_path + file
            csv_file = output_path + 'output.csv'
            if replaceExistingFile or not os.path.exists(output_path + csv_file):
                json_to_csv(json_file, csv_file)
            else:
                print(f"Output file already exists. Skipping the processing.")   

