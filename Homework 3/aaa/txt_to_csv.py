import csv

# Read the text file
with open('7.txt', 'r') as file:
    lines = file.readlines()

# Parse the text data and convert it into a list of dictionaries
data = []
for line in lines:
    parts = line.strip().split()
    id, *words = parts
    data.append({'id': id, 'text': ' '.join(words)})

# Sort the data by the 'id' field
sorted_data = sorted(data, key=lambda x: int(x['id']))

# Write the sorted data to a CSV file
with open('7.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in sorted_data:
        writer.writerow(row)

print("Data has been transferred to output.csv and sorted by ID.")
