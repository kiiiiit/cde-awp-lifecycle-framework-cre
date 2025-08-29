# CDE Lifecycle Methodology (Commercial Real Estate)

> Что это: единый фреймворк управления ЖЦ коммерческих объектов, объединяющий CDE (единый источник данных), ISO 81346/GS1 (коды и прослеживаемость), AWP (EWP/CWP/IWP) и gate‑управление по ГОСТ 59799‑2021. Дает измеримую связку «требования→системы→поставки→монтаж→ПНР→эксплуатация».
> Зачем: сократить простои фронтов и переработки, повысить предсказуемость сроков и качества ввода, снизить TCO/OPEX за счет LCC‑критериев в закупках и корректной передачи данных в эксплуатацию.
> Какие проблемы решает: разрывы между проектированием/закупками/стройкой/ПНР, фрагментация кодов и статусов, «немые» документы без трассируемости, слабая юридическая значимость цифровых копий, отсутствие единых KPI готовности.

> См. обзор: [Framework_CDE-AWP_RealEstate](docs/overview/Framework_CDE-AWP_RealEstate.md)

## Оглавление
- [01_Gates_Methodology](docs/core/)
- [02_CDE_Data_Model](docs/core/)
- [03_Classification_ISO81346](docs/core/)
- [04_AWP_Packaging](docs/core/)
- [05_Procurement_Readiness](docs/core/)
- [06_System_Readiness_and_Cx](docs/core/)
- [07_OandM_AsMaintained](docs/core/)
- [08_KPI_and_Reporting](docs/core/)
- [09_Roles_RACI_and_Policies](docs/core/)
- [10_Commercial_RealEstate_Addendum](docs/core/)

## Вспомогательные
- [Formats_and_Acceptance](docs/supplementary/)
- [LC_Map_and_Gates](docs/supplementary/)
- [CDE_and_Data_Model](docs/supplementary/)
- [AWP_and_Execution_Planning](docs/supplementary/)
- [System_Readiness_and_Cx_Details](docs/supplementary/)
- [OandM_Commercial_RealEstate](docs/supplementary/)
- [KPI_and_Reporting_Details](docs/supplementary/)
- [Roles_and_Responsibility](docs/supplementary/)
- [Ready_Templates_and_Forms](docs/supplementary/)
- [Mini_Implementation_Guide](docs/supplementary/)

## Данные для пилота
- Папка CSV/YAML: `_data/` (см. [Ready_Templates_and_Forms](docs/supplementary/))


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

> Техдок (тезисы): [Technical_Documentation](docs/overview/Technical_Documentation.md)

> One‑Pager: [OnePager_CDE-AWP_Framework](docs/overview/OnePager_CDE-AWP_Framework.md) (PDF будет добавлен при наличии пакета xelatex/wkhtmltopdf)

## Схема СУЖЦО
- Mermaid: [docs/SUJCO_Overview.mmd](docs/SUJCO_Overview.mmd)
- Рендер онлайн: https://mermaid.live/ (вставьте содержимое файла)
