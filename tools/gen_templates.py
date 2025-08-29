#!/usr/bin/env python3
import os, argparse, csv, json

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ROOT)
CSV_DIR = os.path.join(REPO, "_data/csv")
YAML_DIR = os.path.join(REPO, "_data/yaml")

def emit_empty_csv(path: str, headers: list[str]):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
    print(f"Created empty template: {path}")

def emit_empty_yaml(path: str, template: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml_content = json.dumps(template, indent=2, ensure_ascii=False)
        f.write(yaml_content)
    print(f"Created empty template: {path}")

def main():
    ap = argparse.ArgumentParser(description="Generate empty data templates for CDE framework")
    ap.add_argument("--out", default="templates_out",
                   help="Output directory for templates")
    args = ap.parse_args()

    out_dir = args.out
    os.makedirs(out_dir, exist_ok=True)

    # CSV templates with headers
    csv_templates = {
        "awp_packages.csv": ["package_id", "package_type", "iso81346_code", "title", "status", "planned_start", "planned_finish", "ready_to_start", "dependencies", "risk_notes", "owner"],
        "procurement_catalog.csv": ["item_id", "iso81346_code", "gs1_gtin", "title", "tech_attributes", "lcc_energy_kwh_per_year", "lcc_service_interval_months", "spares_included", "doc_status_ifb_ifd_ifc", "lead_time_days", "buffer_days", "owner"],
        "documents_register.csv": ["doc_id", "title", "type", "iso81346_code", "related_package", "status", "revision", "owner", "date_updated", "legal_significance", "link"],
        "kpi_facts_weekly.csv": ["week", "project_id", "system_code", "kpi_code", "value", "unit", "owner", "notes"],
        "raci_matrix.csv": ["artefact_id", "artefact_type", "role_responsible", "role_accountable", "role_consulted", "role_informed"],
        "systems_readiness.csv": ["system_code", "system_name", "mc_packages", "percent_complete", "mechanical_completion", "dependencies", "owner", "notes"],
        "tests_matrix.csv": ["test_id", "system_code", "test_type", "step_no", "step_desc", "expected", "pass_criteria", "tolerance", "owner"],
        "cx_defects_log.csv": ["defect_id", "system_code", "package_id", "date_found", "description", "severity", "status", "owner", "date_target", "root_cause", "countermeasure"],
        "interfaces_register.csv": ["interface_id", "source_area", "target_area", "description", "linked_packages", "deadline", "owner", "status", "notes"]
    }

    # YAML templates
    yaml_templates = {
        "entities.yaml": {"entities": {}},
        "gates.yaml": {"gates": []},
        "status_model.yaml": {"documents": [], "packages": [], "tests": [], "defects": [], "legal_significance": []},
        "awp_templates.yaml": {"awp_templates": {}},
        "policies.yaml": {"policies": {}},
        "pilot_config.yaml": {"pilot": {}},
        "iso81346.yaml": {"iso81346": {}},
        "gs1.yaml": {"gs1": {}},
        "kpi.yaml": {"kpi": []}
    }

    # Generate CSV templates
    for filename, headers in csv_templates.items():
        out_path = os.path.join(out_dir, "csv", filename)
        emit_empty_csv(out_path, headers)

    # Generate YAML templates
    for filename, template in yaml_templates.items():
        out_path = os.path.join(out_dir, "yaml", filename)
        emit_empty_yaml(out_path, template)

    print(f"\nTemplates generated in: {out_dir}")
    print("Use these as starting points for your CDE framework data.")

if __name__ == "__main__":
    main()