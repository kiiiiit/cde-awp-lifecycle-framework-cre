#!/usr/bin/env python3
import os, sys, csv, json, argparse

def convert_csv_to_json(csv_file, json_file):
    """Convert CSV file to JSON array of objects"""
    try:
        data = []
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(dict(row))

        os.makedirs(os.path.dirname(json_file), exist_ok=True)
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Converted {csv_file} -> {json_file} ({len(data)} records)")
        return True

    except Exception as e:
        print(f"Error converting {csv_file}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert CSV to JSON")
    parser.add_argument("csv_file", help="Input CSV file")
    parser.add_argument("json_file", help="Output JSON file")

    args = parser.parse_args()

    if not os.path.exists(args.csv_file):
        print(f"Input file not found: {args.csv_file}")
        sys.exit(1)

    success = convert_csv_to_json(args.csv_file, args.json_file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
