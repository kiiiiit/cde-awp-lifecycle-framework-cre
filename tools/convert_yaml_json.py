#!/usr/bin/env python3
import os, sys, json, yaml, argparse

def convert_yaml_to_json(yaml_file, json_file):
    """Convert YAML file to JSON"""
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        os.makedirs(os.path.dirname(json_file), exist_ok=True)
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Converted {yaml_file} -> {json_file}")
        return True

    except Exception as e:
        print(f"Error converting {yaml_file}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert YAML to JSON")
    parser.add_argument("yaml_file", help="Input YAML file")
    parser.add_argument("json_file", help="Output JSON file")

    args = parser.parse_args()

    if not os.path.exists(args.yaml_file):
        print(f"Input file not found: {args.yaml_file}")
        sys.exit(1)

    success = convert_yaml_to_json(args.yaml_file, args.json_file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
