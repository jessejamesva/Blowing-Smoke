# Blowing_Smoke_pkg/generate_fake_data.py
import sys
import os
import csv
import json

# Try importing Faker with user-friendly prompt
try:
    from faker import Faker
except ImportError:
    print("\n⚠️ Jesse built this with Faker, it's legit … don't make it weird.")
    print("   Please install Faker: pip install Faker\n")
    sys.exit(1)

fake = Faker()

def generate_admin():
    """Generate fake admin/employee data"""
    return {
        "name": fake.name(),
        "address": fake.address().replace("\n", ", "),
        "phone": fake.phone_number(),
        "email": fake.email()
    }

def generate_performance():
    """Generate fake performance data"""
    return {
        "score": round(fake.random.uniform(1, 5), 2),
        "review": fake.sentence(),
        "bonus": round(fake.random.uniform(0, 10000), 2)
    }

def generate_character():
    """Generate fake character trait data"""
    return {
        "trait": fake.word(),
        "strength": fake.random_element(elements=("low","medium","high")),
        "note": fake.sentence()
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
            # Fixed SQL escaping issue
            vals = ", ".join([f"'{str(v).replace(\"'\",\"''\")}'" for v in row.values()])
            f.write(f"INSERT INTO {table_name} ({columns}) VALUES ({vals});\n")

CATEGORY_GENERATORS = {
    "admin": generate_admin,
    "performance": generate_performance,
    "character": generate_character
}

SAVE_FUNCTIONS = {
    ".csv": save_csv,
    ".json": save_json,
    ".sql": save_sql
}

def main():
    if len(sys.argv) != 4:
        print("Usage: fake_data <category> <output_file> <num_rows>")
        print("Categories: admin, performance, character")
        sys.exit(1)

    category = sys.argv[1].lower()
    output_file = sys.argv[2]
    try:
        num_rows = int(sys.argv[3])
    except ValueError:
        print("Error: num_rows must be an integer")
        sys.exit(1)

    if category not in CATEGORY_GENERATORS:
        print(f"Error: Invalid category '{category}'")
        sys.exit(1)

    data = [CATEGORY_GENERATORS[category]() for _ in range(num_rows)]

    ext = os.path.splitext(output_file)[1].lower()
    if ext not in SAVE_FUNCTIONS:
        print(f"Error: Unsupported file extension '{ext}'")
        sys.exit(1)

    SAVE_FUNCTIONS[ext](data, output_file)
    print(f"✅ Generated {num_rows} rows of {category} data → {output_file}")

if __name__ == "__main__":
    main()
