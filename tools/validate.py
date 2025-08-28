#!/usr/bin/env python3
import sys, json, yaml, os
from jsonschema import validate, Draft202012Validator

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)

SCHEMAS_YAML = {
    "entities.yaml": "schemas/yaml/entities.schema.json",
    "gates.yaml": "schemas/yaml/gates.schema.json",
    "status_model.yaml": "schemas/yaml/status_model.schema.json"
}

CSV_SCHEMAS = {
    "kpi_facts_weekly.csv": "schemas/csv/kpi_facts_weekly.schema.json",
    "awp_packages.csv": "schemas/csv/awp_packages.schema.json"
}

errors = 0

# YAML validation
for fname, schema_path in SCHEMAS_YAML.items():
    with open(os.path.join(REPO, schema_path)) as f:
        schema = json.load(f)
    path = os.path.join(REPO, "_data/yaml", fname)
    with open(path) as f:
        data = yaml.safe_load(f)
    v = Draft202012Validator(schema)
    for err in sorted(v.iter_errors(data), key=str):
        print(f"YAML {fname}: {err.message}")
        errors += 1

# CSV validation (headers only minimal)
for fname, schema_path in CSV_SCHEMAS.items():
    with open(os.path.join(REPO, schema_path)) as f:
        schema = json.load(f)
    headers_required = [field["name"] for field in schema.get("fields", [])]
    path = os.path.join(REPO, "_data/csv", fname)
    with open(path) as f:
        header = f.readline().strip().split(",")
    missing = [h for h in headers_required if h not in header]
    if missing:
        print(f"CSV {fname}: missing headers {missing}")
        errors += 1

if errors:
    print(f"Validation failed with {errors} error(s)")
    sys.exit(1)

print("Validation passed successfully!")