# Data Tools

## Шаблоны CSV
```bash
python tools/gen_templates.py --out templates_out
```

## Конвертеры
```bash
# YAML -> JSON
python tools/convert_yaml_json.py _data/yaml/entities.yaml out/entities.json
# CSV -> JSON
python tools/csv_to_json.py _data/csv/awp_packages.csv out/awp_packages.json
```
