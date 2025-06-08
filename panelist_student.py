import json
import csv

def clean_panelist(name):
    return name.replace(" (alum)", "").replace(" (Alum)", "").strip()

def get_category(name):
    return "Alum" if "(alum)" in name.lower() else "Faculty"

# Load data
with open("data.json", "r") as f:
    data = json.load(f)

rows = []

for year, semesters in data.items():
    for semester, content in semesters.items():
        term = f"{semester.capitalize()} {year}"
        students = content.get("student", [])
        panelists = content.get("panelists", [])

        panel_groups = []
        current_panel = []

        for p in panelists:
            current_panel.append(p)
            if "(alum)" in p.lower():
                panel_groups.append(current_panel)
                current_panel = []

        # Match each panel group to each student in order
        for student, panel_group in zip(students, panel_groups):
            for panelist in panel_group:
                rows.append({
                    "Year": year,
                    "Term": term,
                    "Panelist": clean_panelist(panelist),
                    "Category": get_category(panelist),
                    "Student": student
                })

# Write to CSV
with open("panelists_by_student.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Year", "Term", "Panelist", "Category", "Student"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

print("✅ CSV created using alum-based panel boundaries.")
