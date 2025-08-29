# Интеграция с BI (Power BI / Metabase)

## Files
- KPI facts: `_data/csv/kpi_facts_weekly.csv`
- Сводные данные (CI‑генерация): `reports/out/kpi_weekly_agg.csv`
- Сводка готовности (CI‑генерация): `reports/out/system_readiness_summary.csv`

## Power BI (Desktop)
1. Get Data → Web → paste raw URL to CSV (e.g., `https://raw.githubusercontent.com/kiiiiit/cde-awp-lifecycle-framework-cre/main/_data/csv/kpi_facts_weekly.csv`).
2. Set delimiter: Comma. Encoding: UTF-8. Confirm headers as first row.
3. При необходимости используйте сводные данные из `reports/out/` (если опубликованы артефакты) или локальные копии.
4. Model: relate `system_code` and `kpi_code` as needed; create visuals.

## Metabase
1. Add a Database → ‘CSV/External’ via ‘Upload a file’ or point to cloned repo path.
2. Загрузите `_data/csv/kpi_facts_weekly.csv` и `reports/out/*.csv`.
3. Сохраните вопросы и дашборды по еженедельным сводным KPI и готовности.

## Notes
- Prefer raw.githubusercontent links for public data or clone locally for private.
- Keep date fields normalized (ISO 8601); weeks as `YYYY-Www`.
