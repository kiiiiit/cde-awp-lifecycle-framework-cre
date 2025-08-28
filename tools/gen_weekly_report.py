#!/usr/bin/env python3
import os, csv
from jinja2 import Template

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
TEMPLATE = os.path.join(REPO, "reports/templates/weekly_report.md.j2")
OUTDIR = os.path.join(REPO, "reports/out")
os.makedirs(OUTDIR, exist_ok=True)

# Load KPI agg if present
kpi_file = os.path.join(OUTDIR, "kpi_weekly_agg.csv")
kpi = {}
if os.path.exists(kpi_file):
    with open(kpi_file, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            k = (row["week"], row["project_id"], row["kpi_code"])
            kpi[k] = row["value_mean"]

# Load readiness summary
ready_file = os.path.join(OUTDIR, "system_readiness_summary.csv")
ready = {"systems_count": 0, "mean_percent": 0, "mc_done": 0}
if os.path.exists(ready_file):
    with open(ready_file, encoding="utf-8") as f:
        next(f)  # Skip header
        parts = next(f, "").strip().split(",")
        if len(parts) == 3:
            ready["systems_count"] = parts[0]
            ready["mean_percent"] = parts[1]
            ready["mc_done"] = parts[2]

# Pick last week present in kpi or fallback
week = None
project_id = None
if kpi:
    week, project_id, _ = sorted(kpi.keys())[-1]
else:
    week = "2025-W40"
    project_id = "CRE-PILOT-01"

context = {
    "project_id": project_id,
    "week": week,
    "ontime_rate": kpi.get((week, project_id, "SCH_ONTIME_AWP"), "NA"),
    "cx_pass_first": kpi.get((week, project_id, "CX_PASS_FIRST"), "NA"),
    "systems_count": ready["systems_count"],
    "mean_percent": ready["mean_percent"],
    "mc_done": ready["mc_done"],
    "open_interfaces": "TBD",
    "notes": "Generated automatically"
}

with open(TEMPLATE, encoding="utf-8") as f:
    tpl = Template(f.read())

content = tpl.render(**context)
outfile = os.path.join(OUTDIR, f"weekly_{project_id}_{week}.md")
with open(outfile, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Wrote weekly report: {outfile}")
