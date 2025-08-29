# Отчёты (Reports)

CI генерирует:
- `reports/out/kpi_weekly_agg.csv`
- `reports/out/system_readiness_summary.csv`
- `reports/out/weekly_<project>_<week>.md`

Локально:
```bash
python tools/agg_kpi.py
python tools/calc_readiness.py
python tools/gen_weekly_report.py
```
