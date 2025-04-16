import json
import csv

# Load your JSON file
with open('panel_data.json', 'r') as f:
    data = json.load(f)

# Create a list of rows for the CSV
rows = []

for year, semesters in data.items():
    for semester, semester_data in semesters.items():
        for panelist in semester_data["panelists"]:
            rows.append({
                'Year': year,
                'Semester': semester,
                'Panelist': panelist
            })

# Write the CSV
with open('panelists.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Year', 'Semester', 'Panelist'])
    writer.writeheader()
    writer.writerows(rows)

print("CSV file 'panelists.csv' created successfully.")
