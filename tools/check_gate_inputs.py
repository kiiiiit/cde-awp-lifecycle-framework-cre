#!/usr/bin/env python3
import os, yaml, csv, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)

with open(os.path.join(REPO, "_data/yaml/status_model.yaml")) as f:
    status_model = yaml.safe_load(f)

with open(os.path.join(REPO, "_data/yaml/gates.yaml")) as f:
    gates = yaml.safe_load(f)["gates"]

errors = 0

# R and A present; data quality pillars
for g in gates:
    raci = g.get("raci", {})
    if "R" not in raci or "A" not in raci:
        print(f"Gate {g.get('id')}: RACI must include R and A")
        errors += 1
    dq = set(map(str, g.get("data_quality", [])))
    req = {"Completeness", "Consistency", "Traceability", "Legal"}
    if not req.issubset(dq):
        print(f"Gate {g.get('id')}: data_quality must include {req}")
        errors += 1

# documents register status validation
p = os.path.join(REPO, "_data/csv/documents_register.csv")
if os.path.exists(p):
    with open(p) as f:
        r = csv.DictReader(f)
        allowed = set(status_model["documents"])
        for i, row in enumerate(r, start=2):
            st = (row.get("status") or "").strip()
            if st and st not in allowed:
                print(f"documents_register.csv:{i} invalid document status '{st}' not in {allowed}")
                errors += 1

# awp packages status validation
p = os.path.join(REPO, "_data/csv/awp_packages.csv")
if os.path.exists(p):
    with open(p) as f:
        r = csv.DictReader(f)
        allowed = set(status_model["packages"])
        for i, row in enumerate(r, start=2):
            st = (row.get("status") or "").strip()
            if st and st not in allowed:
                print(f"awp_packages.csv:{i} invalid package status '{st}' not in {allowed}")
                errors += 1

if errors:
    print(f"Gate/Data validation failed with {errors} error(s)")
    sys.exit(1)

print("Gate/Data validation passed successfully!")