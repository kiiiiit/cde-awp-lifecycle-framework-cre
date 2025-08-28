#!/usr/bin/env python3
import os, csv
from statistics import mean

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
INFILE = os.path.join(REPO, "_data/csv/systems_readiness.csv")
OUTDIR = os.path.join(REPO, "reports/out")
os.makedirs(OUTDIR, exist_ok=True)

def calculate_system_readiness():
    """Calculate overall system readiness metrics"""
    if not os.path.exists(INFILE):
        print(f"Input file not found: {INFILE}")
        return {}

    systems = []
    total_percent = []
    mc_completed = 0

    with open(INFILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            systems.append(row)
            try:
                percent = float(row['percent_complete'])
                total_percent.append(percent)
                if row.get('mechanical_completion', '').lower() == 'true':
                    mc_completed += 1
            except (ValueError, KeyError):
                continue

    summary = {
        'systems_count': len(systems),
        'mean_percent': round(mean(total_percent), 1) if total_percent else 0,
        'mc_done': mc_completed,
        'systems': systems
    }

    return summary

def save_readiness_summary(summary):
    """Save readiness summary to CSV"""
    outfile = os.path.join(OUTDIR, "system_readiness_summary.csv")

    with open(outfile, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["metric", "value"])
        writer.writerow(["systems_count", summary['systems_count']])
        writer.writerow(["mean_percent", summary['mean_percent']])
        writer.writerow(["mc_done", summary['mc_done']])

    print(f"Readiness summary saved to: {outfile}")

    # Also create detailed report
    detail_file = os.path.join(OUTDIR, "system_readiness_detail.md")
    with open(detail_file, 'w', encoding='utf-8') as f:
        f.write("# System Readiness Detail Report\n\n")
        f.write(f"**Total Systems:** {summary['systems_count']}\n")
        f.write(f"**Average Readiness:** {summary['mean_percent']}%\n")
        f.write(f"**MC Completed:** {summary['mc_done']}\n\n")

        f.write("## System Details\n\n")
        for system in summary['systems']:
            f.write(f"### {system['system_code']} - {system['system_name']}\n")
            f.write(f"- **Readiness:** {system.get('percent_complete', 'N/A')}%\n")
            f.write(f"- **MC Status:** {system.get('mechanical_completion', 'N/A')}\n")
            f.write(f"- **Dependencies:** {system.get('dependencies', 'None')}\n")
            f.write(f"- **Owner:** {system.get('owner', 'N/A')}\n")
            f.write(f"- **Notes:** {system.get('notes', 'None')}\n\n")

    print(f"Detailed report saved to: {detail_file}")

if __name__ == "__main__":
    summary = calculate_system_readiness()
    if summary:
        save_readiness_summary(summary)
        print(f"Processed {summary['systems_count']} systems")
    else:
        print("No systems data found")
