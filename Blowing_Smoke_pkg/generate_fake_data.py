#!/usr/bin/env python3
import sys
import csv
import json
import random
from faker import Faker

fake = Faker()

# --- Admin / Employee data ---
def generate_admin(num_rows, output_file):
    fields = ["name", "address", "phone", "email"]
    data = [
        {
            "name": fake.name(),
            "address": fake.address().replace("\n", ", "),
            "phone": fake.phone_number(),
            "email": fake.email(),
        }
        for _ in range(num_rows)
    ]
    write_output(data, fields, output_file)

# --- Performance data ---
def generate_performance(num_rows, output_file):
    fields = ["employee_name", "job_title", "performance_score", "salary", "hire_date"]
    data = [
        {
            "employee_name": fake.name(),
            "job_title": fake.job(),
            "performance_score": random.randint(1, 10),
            "salary": round(random.uniform(40000, 120000), 2),
            "hire_date": str(fake.date_between(start_date='-5y', end_date='today'))
        }
        for _ in range(num_rows)
    ]
    write_output(data, fields, output_file)

# --- Character trait data ---
def generate_character(num_rows, output_file):
    traits = ["Leadership", "Teamwork", "Creativity", "Dependability", "Integrity"]
    fields = ["employee_name"] + traits
    data = []
    for _ in range(num_rows):
        entry = {"employee_name": fake.name()}
        entry.update({t: random.randint(1, 5) for t in traits})
        data.append(entry)
    write_output(data, fields, output_file)

# --- Helper: write CSV, JSON, or SQL ---
def write_output(data, fields, output_file):
    if output_file.endswith(".csv"):
        with open(output_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
    elif output_file.endswith(".json"):
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
    elif output_file.endswith(".sql"):
        table = output_file.split("/")[-1].replace(".sql", "")
        with open(output_file, "w") as f:
            for row in data:
                cols = ", ".join(row.keys())
                vals = ", ".join([f"'{str(v).replace('\'','\'\'')}'" for v in row.values()])
                f.write(f"INSERT INTO {table} ({cols}) VALUES ({vals});\n")
    else:
        print(f"Unsupported output type for {output_file}. Use .csv, .json, or .sql")

def main():
    if len(sys.argv) != 4:
        print("Usage: generate_fake_data.py [admin|performance|character] [output_file] [num_rows]")
        sys.exit(1)

    category, output_file, num_rows = sys.argv[1], sys.argv[2], int(sys.argv[3])

    if category == "admin":
        generate_admin(num_rows, output_file)
    elif category == "performance":
        generate_performance(num_rows, output_file)
    elif category == "character":
        generate_character(num_rows, output_file)
    else:
        print(f"Unknown category: {category}")
        sys.exit(1)

    print(f"✅ Generated {num_rows} rows of {category} data → {output_file}")

def main():
    import sys
    # (existing code from generate_fake_data.py)
    if len(sys.argv) != 4:
        print("Usage: fake_data [admin|performance|character] [output_file] [num_rows]")
        sys.exit(1)

    category, output_file, num_rows = sys.argv[1], sys.argv[2], int(sys.argv[3])

    if category == "admin":
        generate_admin(num_rows, output_file)
    elif category == "performance":
        generate_performance(num_rows, output_file)
    elif category == "character":
        generate_character(num_rows, output_file)
    else:
        print(f"Unknown category: {category}")
        sys.exit(1)

    print(f"✅ Generated {num_rows} rows of {category} data → {output_file}")

if __name__ == "__main__":
    main()
