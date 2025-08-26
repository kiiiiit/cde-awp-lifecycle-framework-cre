# Roadmap — CDE‑AWP Lifecycle Framework

Status: v0.1–v0.4 completed (docs/validation/reports/API/CI). Next: v0.5 pilot data & dashboards.

## Releases
- v0.1 Foundation (docs + validation)
  - GitHub Pages (MkDocs). Навигация по 10 разделам, one‑pager, схемы
  - Схемы валидации: JSON Schema для YAML; Frictionless для CSV
  - CI: проверка схем и линт Markdown
  - Дополнение gates.yaml чек‑листами и RACI‑примерами
  - Дополнительные Mermaid‑схемы (AWP‑поток, Cx‑матрица)
- v0.2 Data pipeline (KPI/отчеты)
  - Скрипты агрегации KPI и шаблоны weekly отчётов
  - Примеры выгрузок для BI + инструкции
  - Обогащение каталога закупок LCC и связями ISO 81346/GS1
  - Генератор пустых болванок (CLI)
- v0.3 Gate readiness toolset
  - Проверка “no data — no gate” для гейтов
  - Расчёт системной готовности по MC‑пакетам
  - Отчёт по качеству данных (C/C/T/L)
- v0.4 Integrations/OpenAPI
  - OpenAPI спека по entities.yaml
  - Экспорт/импорт форматов (YAML/JSON, CSV/Parquet)
  - Рендер Mermaid в SVG и публикация в Pages
  - Примеры мостов ISO 81346↔GS1

## Tasks detail
- Документация и сайт: MkDocs, автогенерация SVG из Mermaid, link‑check
- Валидация данных: JSON Schema и Frictionless + GitHub Actions
- Инструменты расчётов: readiness, gate‑checks, KPI агрегации
- Отчёты: шаблоны Jinja2 и генерация .md/.pdf
- Диаграммы: AWP flow, Cx matrix, RACI
- OpenAPI: `api/openapi.yaml` и мок‑сервер
- DevX/CI: pre‑commit, issue templates, changelog

## Inputs needed
- Бренд/тема сайта
- Финализация KPI и формул
- Веса MC‑пакетов
- Выбор BI для примеров

## Next (v0.5)
- Пилотные данные (ISO 81346/GS1): заполнение каталогов и примеры
- Доп. KPI и словари (normative vs actual)
- Dashboards примеры (Power BI/Metabase файлы)
- Интеграция с внешним CDE (коннектор‑плейсхолдер)
- Автотесты для tools/ (pytest)
