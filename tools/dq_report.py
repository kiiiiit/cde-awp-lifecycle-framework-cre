#!/usr/bin/env python3
import os, yaml, csv
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
report = []
# Check data quality pillars per gate
with open(os.path.join(REPO, _data/yaml/gates.yaml)) as f:
    gates = yaml.safe_load(f)[gates]
for g in gates:
    dq = set(map(str, g.get(data_quality, [])))
    missing = {"Completeness","Consistency","Traceability","Legal"} - dq
    if missing:
        report.append(f"Gate {g[id]}: missing DQ {sorted(missing)}")
# Basic CSV completeness checks
csv_checks = [
  (_data/csv/awp_packages.csv,[package_id,package_type,status]),
  (_data/csv/documents_register.csv,[doc_id,status,revision]),
]
for rel, cols in csv_checks:
    p=os.path.join(REPO, rel)
    if not os.path.exists(p):
        report.append(f"Missing file {rel}")
        continue
    with open(p) as f:
        r = csv.DictReader(f)
        for i,row in enumerate(r, start=2):
            missing = [c for c in cols if not row.get(c)]
            if missing:
                report.append(f"{rel}:{i} missing {missing}")
outfile=os.path.join(REPO,reports/out/data_quality_report.md)
with open(outfile,w) as f:
    if report:
        f.write(#