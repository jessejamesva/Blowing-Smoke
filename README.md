# Blowing_Smoke

## Description

Blowing_Smoke is a CLI tool to generate fake employee data, performance data, and character traits using the Python Faker library. It supports CSV, JSON, and SQL outputs, and is designed for quick testing, development, or demo purposes. I am working on my DevOps skill's and attempted to build a tool to potentialy make my life a little easier, tomorrow. If I am giong to be moving lots of data in my quest to gain DevOps skills then I certainly don't want to get lost in the weeds.

---

## Features

- Generate fake **admin data**: name, address, phone, email
- Generate **performance data**: score, review, bonus
- Generate **character trait data**: trait, strength, note
- Combine all categories in one file using the `all` option
- Auto-create output directories if they don’t exist
- Default 10 rows if not specified
- Supports CSV, JSON, and SQL formats
- Easy CLI usage anywhere after installation
- Friendly prompt if Faker is not installed:
  > ⚠️ Jesse built this with Faker, it's legit … don't make it weird.

---

## Installation

1. Clone the repository:

```bash
*command to install git with dnf
git clone https://github.com/jessejamesva/Blowing-Smoke.git
cd Blowing-Smoke
```

2. Create a virtual environment:

```bash
python3 -m venv ~/venv
source ~/venv/bin/activate
```

3. Install the package in editable mode:

```bash
python3 -m upgrade pip
pip install -e .
```

4. Make the Bash wrapper executable:

```bash
chmod +x scripts/fake_data.sh
```

5. Install Faker

```bash
pip install faker
```

---

## Usage

```bash
fake_data <category> <output_file> [num_rows]
```

### Arguments

- `<category>`: `admin`, `performance`, `character`, `all`
- `<output_file>`: path and filename with extension (`.csv`, `.json`, `.sql`)
- `[num_rows]`: optional, defaults to 10

### Help

```bash
fake_data --help
```

Outputs usage instructions and supported categories.

---

## Examples

Generate 10 rows of admin data to CSV:

```bash
fake_data admin data/employees.csv 10
```

Generate 5 rows of performance data to JSON:

```bash
fake_data performance data/perf.json 5
```

Generate 3 rows of character data to SQL:

```bash
fake_data character data/traits.sql 3
```

Generate all categories combined into one JSON file:

```bash
fake_data all data/all_data.json 5
```

---

## Output

- **CSV**: standard spreadsheet-ready table
- **JSON**: human-readable, pretty-printed format
- **SQL**: safe `INSERT INTO` statements with single quotes escaped

Example JSON output snippet:

```json
[
  {
    "score": 4.53,
    "review": "Employee performed exceptionally well.",
    "bonus": 5234.12
  },
  {
    "score": 3.87,
    "review": "Met expectations with minor issues.",
    "bonus": 4120.0
  }
]
```

---

## Optional Enhancements (Planned / Not Yet Implemented)

- Logging or verbose mode for progress tracking
- Seed option for reproducible data
- Timestamped filenames to avoid overwrites
- Colorized terminal output for success, warnings, and errors
- Filtering or querying JSON output using `jq` or Python

---

## Notes

- If Faker is not installed, the CLI prints a friendly message and exits:

```
⚠️ Jesse built this with Faker, it's legit … don't make it weird.
Please install Faker: pip install Faker
```

- The CLI automatically creates output directories if they do not exist.
- Default number of rows is 10 if not specified.
- `all` category adds a `"category"` field in combined output to distinguish types.

- Jesse's Closing Thoughts - I'm getting better at estimating the time to completion, over-estimated myself by a factor of 2 during planning. But, I accomplished pretty much all the stretch goals so haters, you know what to do. | I have a firmer grip on the computer file structure, and not in a way that I understand it better - but instead, in a way where I can picture in my mind easier. Traversing and building out the tree felt natural. Just a note | Thank you for coming to my TedTalk and reading all the way down here.... | "Always be the duck!"

---

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.
