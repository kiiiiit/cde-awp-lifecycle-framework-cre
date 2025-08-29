#!/usr/bin/env python3
import csv, os, collections
from statistics import mean

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
INFILE = os.path.join(REPO, "_data/csv/kpi_facts_weekly.csv")
OUTDIR = os.path.join(REPO, "reports/out")
os.makedirs(OUTDIR, exist_ok=True)

AggKey = collections.namedtuple("AggKey", ["week", "project_id", "kpi_code"])

def aggregate_kpi_facts():
    """Aggregate KPI facts by week/project/kpi"""
    if not os.path.exists(INFILE):
        print(f"Input file not found: {INFILE}")
        return {}

    data = collections.defaultdict(list)

    with open(INFILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = AggKey(
                week=row['week'],
                project_id=row['project_id'],
                kpi_code=row['kpi_code']
            )
            try:
                value = float(row['value'])
                data[key].append(value)
            except (ValueError, KeyError):
                continue

    # Calculate means
    aggregated = {}
    for key, values in data.items():
        if values:
            aggregated[key] = mean(values)

    return aggregated

def save_aggregated_data(aggregated):
    """Save aggregated data to CSV"""
    outfile = os.path.join(OUTDIR, "kpi_weekly_agg.csv")

    if not aggregated:
        print("No data to aggregate")
        return

    # Get unique weeks and projects for structuring
    weeks = sorted(set(k.week for k in aggregated.keys()))
    projects = sorted(set(k.project_id for k in aggregated.keys()))
    kpis = sorted(set(k.kpi_code for k in aggregated.keys()))

    with open(outfile, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Write header
        header = ["week", "project_id"] + kpis + ["value_mean"]
        writer.writerow(header)

        # Write data
        for week in weeks:
            for project in projects:
                row = [week, project]
                for kpi in kpis:
                    key = AggKey(week, project, kpi)
                    value = aggregated.get(key, "")
                    row.append(value)
                # Calculate overall mean for the week/project
                week_values = [aggregated[k] for k in aggregated.keys()
                             if k.week == week and k.project_id == project]
                mean_value = mean(week_values) if week_values else ""
                row.append(mean_value)
                writer.writerow(row)

    print(f"Aggregated KPI data saved to: {outfile}")

if __name__ == "__main__":
    aggregated = aggregate_kpi_facts()
    save_aggregated_data(aggregated)
    print(f"Processed {len(aggregated)} KPI aggregations")