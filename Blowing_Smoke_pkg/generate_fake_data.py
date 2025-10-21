## This python script can be used for data generation. Built by JesseV2025

# Usage: fake_data <category> <output_file> [num_rows]

#    Categories:
#       admin        Generate employee admin data (name, address, phone, email)
#       performance  Generate performance data (score, review, bonus)
#       character    Generate character traits (trait, strength, note)
#       all          Generate all three categories into one file

#    Supported output files: .csv, .json, .sql

#   Examples:
#       fake_data admin data/employees.csv 10
#       fake_data all data/fake_all.json 5

import sys
import os
import csv
import json
from datetime import datetime

# Try importing Faker
try:
    from faker import Faker
except ImportError:
    print("\n⚠️ Jesse built this with Faker, it's legit … don't make it weird.")
    print("   Please install Faker: pip install Faker\n")
    sys.exit(1)

fake = Faker()

def generate_admin():
    return {
        "name": fake.name(),
        "address": fake.address().replace("\n", ", "),
        "phone": fake.phone_number(),
        "email": fake.email()
    }

def generate_performance():
    return {
        "score": round(fake.random.uniform(1, 5), 2),
        "review": fake.sentence(),
        "bonus": round(fake.random.uniform(0, 10000), 2)
    }

def generate_character():
    return {
        "trait": fake.word(),
        "strength": fake.random_element(elements=("low","medium","high")),
        "note": fake.sentence()
    }

CATEGORY_GENERATORS = {
    "admin": generate_admin,
    "performance": generate_performance,
    "character": generate_character
}

SAVE_FUNCTIONS = {
    ".csv": "csv",
    ".json": "json",
    ".sql": "sql"
}

def save_csv(data, output_file):
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_json(data, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def save_sql(data, output_file):
    table_name = "fake_data"
    with open(output_file, "w", encoding="utf-8") as f:
        for row in data:
            columns = ", ".join(row.keys())
            vals_list = []
            for v in row.values():
                safe_val = str(v).replace("'", "''")
                vals_list.append(f"'{safe_val}'")
            vals = ", ".join(vals_list)
            f.write(f"INSERT INTO {table_name} ({columns}) VALUES ({vals});\n")

def main():
    # Help flag
    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        print("""
Usage: fake_data <category> <output_file> [num_rows]

Categories:
  admin        Generate employee admin data (name, address, phone, email)
  performance  Generate performance data (score, review, bonus)
  character    Generate character traits (trait, strength, note)
  all          Generate all three categories into one file

Supported output files: .csv, .json, .sql

Examples:
  fake_data admin data/employees.csv 10
  fake_data all data/fake_all.json 5
""")
        sys.exit(0)

    if len(sys.argv) < 3:
        print("Error: Not enough arguments. Use --help for usage info.")
        sys.exit(1)

    category = sys.argv[1].lower()
    output_file = sys.argv[2]
    num_rows = int(sys.argv[3]) if len(sys.argv) > 3 else 10  # default 10 rows

    # Ensure output folder exists
    folder = os.path.dirname(output_file) or "data"
    os.makedirs(folder, exist_ok=True)

    # Determine categories to generate
    if category == "all":
        categories = ["admin", "performance", "character"]
    elif category in CATEGORY_GENERATORS:
        categories = [category]
    else:
        print(f"Error: Invalid category '{category}'. Use --help for options.")
        sys.exit(1)

    ext = os.path.splitext(output_file)[1].lower()
    if ext not in SAVE_FUNCTIONS:
        print(f"Error: Unsupported file extension '{ext}'")
        sys.exit(1)

    combined_data = []
    for cat in categories:
        cat_data = [CATEGORY_GENERATORS[cat]() for _ in range(num_rows)]
        if category == "all":
            for i, row in enumerate(cat_data):
                row["category"] = cat  # mark category if combining
        combined_data.extend(cat_data)

    # Save file
    if ext == ".csv":
        save_csv(combined_data, output_file)
    elif ext == ".json":
        save_json(combined_data, output_file)
    elif ext == ".sql":
        save_sql(combined_data, output_file)

    print(f"✅ Generated {num_rows} rows of {category} data → {output_file}")

if __name__ == "__main__":
    main()
