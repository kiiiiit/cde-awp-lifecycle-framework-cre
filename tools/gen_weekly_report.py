#!/usr/bin/env python3
import os, csv
from jinja2 import Template

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
TEMPLATE = os.path.join(REPO, "reports/templates/weekly_report.md.j2")
OUTDIR = os.path.join(REPO, "reports/out")
os.makedirs(OUTDIR, exist_ok=True)

"""Generate weekly report from aggregated KPI (wide) and readiness summary.

Expected KPI agg format (wide):
  week,project_id, SCH_ONTIME_AWP, CX_PASS_FIRST, ..., value_mean
"""

# Load KPI agg if present (wide format)
kpi_file = os.path.join(OUTDIR, "kpi_weekly_agg.csv")
kpi_wide_by_key = {}
if os.path.exists(kpi_file):
    with open(kpi_file, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            week = row.get("week")
            project = row.get("project_id")
            if not week or not project:
                continue
            kpi_wide_by_key[(week, project)] = row

# Load readiness summary (metric,value rows)
ready_file = os.path.join(OUTDIR, "system_readiness_summary.csv")
ready = {"systems_count": 0, "mean_percent": 0, "mc_done": 0}
if os.path.exists(ready_file):
    with open(ready_file, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            metric = row.get("metric")
            value = row.get("value")
            if metric in ready:
                ready[metric] = value

# Pick last week present in KPI agg or fallback
week = None
project_id = None
if kpi_wide_by_key:
    week, project_id = sorted(kpi_wide_by_key.keys())[-1]
else:
    week = "2025-W40"
    project_id = "CRE-PILOT-01"

row = kpi_wide_by_key.get((week, project_id), {})
context = {
    "project_id": project_id,
    "week": week,
    "ontime_rate": row.get("SCH_ONTIME_AWP", "NA"),
    "cx_pass_first": row.get("CX_PASS_FIRST", "NA"),
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
