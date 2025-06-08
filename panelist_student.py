import json
import csv

# Helper function to determine panelist category
def get_category(name):
    return "Alum" if "(alum)" in name.lower() or "(alum)" in name else "Faculty"

# Load data
with open("data.json", "r") as f:
    data = json.load(f)

# Prepare rows
rows = []

for year, semesters in data.items():
    for semester, content in semesters.items():
        term = f"{semester.capitalize()} {year}"
        students = content.get("student", [])
        panelists = content.get("panelists", [])
        
        for panelist in panelists:
            category = get_category(panelist)
            for student in students:
                rows.append({
                    "Year": year,
                    "Term": term,
                    "Panelist": panelist.replace(" (alum)", "").replace(" (Alum)", ""),
                    "Category": category,
                    "Student": student
                })

# Write to CSV
with open("panelist_student_long_format.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Year", "Term", "Panelist", "Category", "Student"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print("CSV file 'panelist_student_long_format.csv' has been created.")
