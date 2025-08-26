#!/usr/bin/env python3
import os, argparse, csv, json
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
CSV_DIR = os.path.join(REPO, _data/csv)
YAML_DIR = os.path.join(REPO, _data/yaml)

def emit_empty_csv(path: str, headers: list[str]):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, w, newline=) as f:
        w = csv.writer(f)
        w.writerow(headers)
    print(f"Created empty template: {path}")

def main():
    ap = argparse.ArgumentParser(description=Generate