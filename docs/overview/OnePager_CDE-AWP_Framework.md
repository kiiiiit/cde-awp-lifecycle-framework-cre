---
title: "CDE‑AWP Lifecycle Framework (CRE) — One‑Pager"
author: ""
date: "2025-08-25"
geometry: margin=20mm
fontsize: 10pt
---

# Что это
Единый каркас управления ЖЦ коммерческих объектов: CDE как единый источник данных, ISO 81346/GS1 для кодов и прослеживаемости, AWP (EWP/CWP/IWP) для фронтов работ, гейты по ГОСТ 59799‑2021.

# Зачем (Value)
- Сокращение простоев фронтов и переработок
- Предсказуемые сроки ввода и снижение рисков
- LCC/TCO в закупках → ниже OPEX арендаторов/оператора
- Корректная передача данных в эксплуатацию (as‑maintained)

# Какие проблемы решает
- Разрывы «проектирование→закупки→стройка→ПНР→эксплуатация»
- Фрагментация кодов/статусов и «немые» документы без трассируемости
- Неопределённые критерии готовности (IFB/IFD/IFC, MC/MCCR, PASS/FAIL)
- Слабая юридическая значимость цифровых копий и отсутствие единых KPI

# Область и архитектура (снимок)
- CDE: Requirements, Design, Procurement, Construction, Commissioning, O&M
- Сущности: Requirement, Document, Spec, Package(EWP/CWP/IWP), ProcurementItem, Shipment, System, Test, Defect, Asset
- Метаданные: статус/ревизия/владелец (RACI), юридическая значимость, ссылки (сквозная трассировка)
- Коды: ISO 81346 (= функция, - изделие, + локация) + мосты к GS1 (GTIN/SSCC/GIAI/GLN)
- Исполнение: AWP пакеты, регистры интерфейсов и «готовность фронтов»
- Гейты: чек‑листы входов/выходов, «no data — no gate», протокол решения
- MC/Cx: модель системной готовности, SAT/FAT/интеграции, PASS/FAIL, дефекты и SLA
- O&M: as‑built→as‑maintained, паспорта, точки мониторинга, SLA/KPI
- KPI: каталог, макеты отчётов, CSV‑болванки

# Коды (ISO 81346) — примеры
- AHU‑01 на 7 этаже: `=F1-HVAC -AHU-01 +LVL07` ⇄ `F1-HVAC-AHU-01`
- ИБП‑01 в эл.комнате LVL03: `=F1-EL -UPS-01 +LVL03+ELR` ⇄ `F1-EL-UPS-01`
- BMS контроллер зоны 1: `=F1-BMS -CTRL-BAC-01 +Z01` ⇄ `F1-BMS-CTRL-BAC-01`

# GS1 — связь «изделие→поставка→актив»
- GTIN (01) для позиции закупки, SSCC (00) для грузоместа, GIAI (8004) для установленного актива, GLN (414) для локации
- Цепочка в CDE: документ/спека ⇄ procurement(GTIN) ⇄ shipment(SSCC) ⇄ asset(GIAI) ⇄ ISO81346 код

# Гейты — ориентиры приёмки (пример)
- G3 Execute Readiness: CWP список утверждён; материалы на складе/в пути; интерфейсы закрыты; IWP конвейер на 2 недели; RACI назначен
- G4 Mechanical Completion: % системной готовности по модели; протокол MC; SAT планы готовы; punchlist заведен
- G6 Handover: as‑built комплект; паспорта O&M, серийники/прошивки; отчёт ОПЭ; SLA эксплуатации; as‑maintained базовая запись

# KPI (базовый набор)
- SCH_ONTIME_AWP — доля пакетов в срок
- CX_PASS_FIRST — доля тестов с первого раза
- REWORK_INDEX — переработки / трудозатраты
- OPEX_ENERGY_INT — энергоинтенсивность (kWh/m²)

# Роли и RACI (сводно)
Sponsor; Project Manager; Design Lead; System Engineer (HVAC/EL/BMS); Procurement Lead; Logistics; Construction PM; QA/QC; Cx Lead; HSE; Operations (FM); BIM/CDE Admin; Finance; Tenant Coordinator.
- EWP: R=Design Lead; A=PM; C=System Eng, QA/QC; I=Procurement
- CWP/IWP: R=Construction PM; A=PM; C=System Eng, Logistics; I=QA/QC, HSE
- SAT/FAT: R=Cx Lead; A=PM; C=System Eng, QA/QC, HSE; I=Operations
- Handover: R=Operations Lead; A=PM; C=Cx Lead, QA/QC; I=Sponsor

# План внедрения
- 6 мес.: CDE+словарь, гейты и статусная модель; AWP и регистры интерфейсов; MC/Cx матрица; KPI и отчёты; контур as‑maintained
- 12 мес.: масштабирование, автоматизация статусов/юридической значимости, интеграция ТОиР и KPI доступности/энергоэффективности

# Принятие пилота (acceptance)
- Комплектность по списку артефактов; непротиворечивость кодов ISO 81346; связность артефактов с гейтами; RACI в карточках; рабочие формы AWP/ПНР/эксплуатации; KPI‑отчёты

# Next steps
- Утвердить префикс объекта (например, BC01), этажи/зоны и состав ролей
- Заполнить `_data/yaml/pilot_config.yaml` и справочники `_data/csv/*.csv`
- Запустить еженедельную отчётность и панель гейтов в BI/CDE

# Репозиторий
README, Technical_Documentation, заметки 01–10, `_data/csv`, `_data/yaml`
