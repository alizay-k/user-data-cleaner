# 🧼 User Data Cleaner

This is a beginner-friendly Python project that loads messy user data from a CSV file, cleans it, and saves a cleaned version.

## 🧠 What It Does

- Loads data from `dirty_user.csv`
- Removes duplicate rows
- Fills missing:
  - `name` → "unknown"
  - `email` → "noemail@example.com"
  - `age` → 0
  - `country` → "unknown"
- Saves cleaned data to `cleaned_user.csv`

## 🛠️ Tools & Libraries

- Python
- pandas

## 🚀 How to Run

1. Make sure Python and `pandas` are installed
2. Place your dirty data in a file called `dirty_user.csv`
3. Run the script:

```bash
python user-data-cleaner.py
