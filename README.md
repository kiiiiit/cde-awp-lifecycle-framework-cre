# CDE Lifecycle Methodology (Commercial Real Estate)

> Что это: единый фреймворк управления ЖЦ коммерческих объектов, объединяющий CDE (единый источник данных), ISO 81346/GS1 (коды и прослеживаемость), AWP (EWP/CWP/IWP) и gate‑управление по ГОСТ 59799‑2021. Дает измеримую связку «требования→системы→поставки→монтаж→ПНР→эксплуатация».
> Зачем: сократить простои фронтов и переработки, повысить предсказуемость сроков и качества ввода, снизить TCO/OPEX за счет LCC‑критериев в закупках и корректной передачи данных в эксплуатацию.
> Какие проблемы решает: разрывы между проектированием/закупками/стройкой/ПНР, фрагментация кодов и статусов, «немые» документы без трассируемости, слабая юридическая значимость цифровых копий, отсутствие единых KPI готовности.

> См. обзор: [Framework_CDE-AWP_RealEstate](Framework_CDE-AWP_RealEstate.md)

## Оглавление
- [01_Gates_Methodology](01_Gates_Methodology.md)
- [02_CDE_Data_Model](02_CDE_Data_Model.md)
- [03_Classification_ISO81346](03_Classification_ISO81346.md)
- [04_AWP_Packaging](04_AWP_Packaging.md)
- [05_Procurement_Readiness](05_Procurement_Readiness.md)
- [06_System_Readiness_and_Cx](06_System_Readiness_and_Cx.md)
- [07_OandM_AsMaintained](07_OandM_AsMaintained.md)
- [08_KPI_and_Reporting](08_KPI_and_Reporting.md)
- [09_Roles_RACI_and_Policies](09_Roles_RACI_and_Policies.md)
- [10_Commercial_RealEstate_Addendum](10_Commercial_RealEstate_Addendum.md)

## Вспомогательные
- [Formats_and_Acceptance](Formats_and_Acceptance.md)
- [LC_Map_and_Gates](LC_Map_and_Gates.md)
- [CDE_and_Data_Model](CDE_and_Data_Model.md)
- [AWP_and_Execution_Planning](AWP_and_Execution_Planning.md)
- [System_Readiness_and_Cx_Details](System_Readiness_and_Cx_Details.md)
- [OandM_Commercial_RealEstate](OandM_Commercial_RealEstate.md)
- [KPI_and_Reporting_Details](KPI_and_Reporting_Details.md)
- [Roles_and_Responsibility](Roles_and_Responsibility.md)
- [Ready_Templates_and_Forms](Ready_Templates_and_Forms.md)
- [Mini_Implementation_Guide](Mini_Implementation_Guide.md)

## Данные для пилота
- Папка CSV/YAML: `_data/` (см. [Ready_Templates_and_Forms](Ready_Templates_and_Forms.md))


## ISO 81346: схема кодирования (пилот)
- Формат: `=Функция -Изделие +Локация`; префиксы: проект `F1`, объект `BC01`.
- Домены (пример функции): `=F1-EL` электроснабжение; `=F1-HVAC` ОВК; `=F1-BMS` диспетчеризация; `=F1-FS` пожарная безопасность; `=F1-WAT` водоснабжение/канализация; `=F1-FAC` фасады; `=F1-LFT` лифты; `=F1-ITC` ИТ/СКС.
- Изделия (примерные обозначения): `-SWGR-LV1` ГРЩ-НН; `-UPS-01` ИБП; `-PANEL-LV-01` ЩО; `-AHU-01` ПВУ; `-VAV-01` VAV-клапан; `-FCU-01` фанкойл; `-PUMP-CHW-01` насос; `-CTRL-BAC-01` BMS-контроллер; `-FACP-01` ППКП; `-SMOKE-FAN-01` дымосос; `-LIFT-01` лифт; `-CURT-01` пож. штора.
- Локации: `+LVL07` этаж 7; `+Z01` зона 1; `+CORE` ядро; `+RM-0703` помещение 703; `+B1` подвал.
- Примеры (аспектная запись ⇄ объединённый код):
  - AHU-01 на 7 этаже: `=F1-HVAC -AHU-01 +LVL07` ⇄ `F1-HVAC-AHU-01`
  - ИБП-01 в эл.комнате LVL03: `=F1-EL -UPS-01 +LVL03+ELR` ⇄ `F1-EL-UPS-01`
  - BMS-контроллер зоны 1: `=F1-BMS -CTRL-BAC-01 +Z01` ⇄ `F1-BMS-CTRL-BAC-01`
  - ППКП на 1 этаже: `=F1-FS -FACP-01 +LVL01+FCR` ⇄ `F1-FS-FACP-01`
- См. `_data/yaml/iso81346.yaml` и примеры в `_data/csv/*`.

## GS1 идентификаторы (пилот)
- GTIN (01): `(01)04601234567893` — изделие (реальный GTIN производителя)
- SSCC (00): `(00)312345678901234657` — грузоместо/палета
- GIAI (8004): `(8004)BC01-UPS-01-SN12345` — актив (установленный экземпляр)
- GLN (414): `(414)0460001112223` — локация/узел приёмки
- Связь в CDE: документ/спецификация ⇄ позиция закупки (GTIN) ⇄ поставка (SSCC) ⇄ актив (GIAI) ⇄ код ISO 81346
- См. `_data/yaml/gs1.yaml`.

## Роли и RACI (пилот)
- Роли: Sponsor; Project Manager; Design Lead (MEP/Arch); System Engineer (HVAC/EL/BMS); Procurement Lead; Contracts/Legal; Logistics Lead; Construction PM/Superintendent; QA/QC Lead; Cx Lead; HSE Lead; Operations Lead/Facility Manager; BIM/CDE Admin; Finance/Cost; Tenant Coordinator.
- Гейты (пример):
  - G2 Define: R=Design Lead; A=PM; C=Procurement, System Engineers; I=Operations
  - G3 Execute Readiness: R=Construction PM; A=PM; C=Logistics, Design Lead; I=QA/QC, HSE
  - G4 Mechanical Completion: R=Cx Lead; A=PM; C=QA/QC, System Engineers; I=Operations
  - G6 Handover: R=Operations Lead; A=PM; C=Cx Lead, QA/QC; I=Sponsor
- Артефакты (пример):
  - EWP: R=Design Lead; A=PM; C=System Eng, QA/QC; I=Procurement
  - CWP/IWP: R=Construction PM; A=PM; C=System Eng, Logistics; I=QA/QC, HSE
  - Procurement Item: R=Procurement Lead; A=PM; C=System Eng, Operations; I=QA/QC, Finance
  - SAT/FAT: R=Cx Lead; A=PM; C=System Eng, QA/QC, HSE; I=Operations
  - O&M паспорта: R=Operations Lead; A=PM; C=Cx Lead, QA/QC; I=Tenant Coordinator
- См. `_data/csv/raci_matrix.csv`, `_data/yaml/gates.yaml`.

> Техдок (тезисы): [Technical_Documentation](Technical_Documentation.md)

> One‑Pager: [OnePager_CDE-AWP_Framework](OnePager_CDE-AWP_Framework.md) (PDF будет добавлен при наличии пакета xelatex/wkhtmltopdf)

## Схема СУЖЦО
- Mermaid: [docs/SUJCO_Overview.mmd](docs/SUJCO_Overview.mmd)
- Рендер онлайн: https://mermaid.live/ (вставьте содержимое файла)
