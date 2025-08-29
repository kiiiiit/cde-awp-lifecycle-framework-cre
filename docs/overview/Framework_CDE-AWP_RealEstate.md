# CDE‑AWP Lifecycle Framework (Commercial Real Estate)

## Название и назначение

CDE‑AWP Lifecycle Framework — единый каркас управления жизненным циклом коммерческих объектов от предпроектных исследований до эксплуатации и модернизации. Фреймворк соединяет CDE (единый источник данных), классификацию ISO 81346/GS1, пакетирование работ AWP и gate‑управление по ГОСТ 59799‑2021, чтобы обеспечить прослеживаемость, готовность фронтов и измеряемые результаты по срокам/качеству/стоимости.

## Принципы

- Единый источник правды: все артефакты и статусы — в CDE
- Дисциплина статусов: IFB/IFD/IFC, «no data — no gate»
- Системная структура: ISO 81346 + мосты к GS1 (GTIN/SSCC/GIAI)
- Пакет‑ориентированное исполнение: EWP/CWP/IWP, готовность фронтов
- Трассируемость требований: bidirectional links требования→системы→испытания→эксплуатация
- Юридическая значимость: политика версий/выпуска/подписей в CDE

## Архитектура фреймворка

1. CDE и модель данных:

- Пространства Requirements/Design/Procurement/Construction/Commissioning/O&M
- Сущности: Требование, Документ, Спецификация, Пакет работ (EWP/CWP/IWP), Поставка, Тест, Несоответствие, Система
- Метаданные: статус, ревизия, владелец (RACI), ссылки на объекты, юридическая значимость

2. Классификация ISO 81346 и GS1:

- Дерево кодов для МЭП/ядра/фасадов/ИТ
- Правила кодирования и управление словарями
- Мосты к GS1 для изделий и логистики, поля для сквозной прослеживаемости

3. AWP и пакетирование:

- Шаблоны EWP/CWP/IWP, зависимость от поставок и системных границ
- Регистры интерфейсов и готовности фронтов

4. Гейты ЖЦ по ГОСТ 59799‑2021:

- Входы/выходы, RACI, критерии готовности, протокол решения
- Чек‑лист качества данных: Полнота (Completeness), Согласованность (Consistency), Трассируемость (Traceability), Юридическая готовность (Legal readiness)

5. Закупки и готовность:

- Каталог позиций с кодами ISO 81346/GS1 и LCC/TCO
- Процедуры выбора и приёмка документации поставщиков в CDE

6. Системная готовность и ПНР:

- MC‑пакеты, перевод объёмов в % готовности систем
- Матрица SAT/FAT/интеграционных тестов, PASS/FAIL, журнал несоответствий

7. Эксплуатация и as‑maintained:

- Передача данных, SLA/KPI, процесс обратной записи в CDE

8. KPI и отчётность:

- Каталог KPI, макеты отчётов, CSV‑болванки

9. Роли и политика доступа:

- RACI по гейтам, матрица прав, аудит‑лог изменений

## Операционная модель

- Статусная модель документов и пакетов, «заморозка/выпуск»
- Управление изменениями и трассировка решений гейтов
- Контуры интерфейсов: проектирование→закупки→строительство→ПНР→эксплуатация

## Внедрение

- 6 месяцев: настройка CDE/словарей, гейты, AWP, ПНР‑матрица, KPI, as‑maintained контур
- 12 месяцев: масштабирование, автоматизация статусов, контуры ТОиР с KPI доступности/энергоэффективности

## Приёмка и эффекты

- Критерии: комплектность, непротиворечивость ISO 81346, связность артефактов с гейтами, RACI и готовые формы
- Эффекты: сокращение простоев фронтов и переработок, предсказуемость графиков, улучшение CAPEX/OPEX

## Навигация по материалам

- Основные: [01_Gates_Methodology](../core/01_Gates_Methodology.md), [02_CDE_Data_Model](../core/02_CDE_Data_Model.md), [03_Classification_ISO81346](../core/03_Classification_ISO81346.md), [04_AWP_Packaging](../core/04_AWP_Packaging.md), [05_Procurement_Readiness](../core/05_Procurement_Readiness.md), [06_System_Readiness_and_Cx](../core/06_System_Readiness_and_Cx.md), [07_OandM_AsMaintained](../core/07_OandM_AsMaintained.md), [08_KPI_and_Reporting](../core/08_KPI_and_Reporting.md), [09_Roles_RACI_and_Policies](../core/09_Roles_RACI_and_Policies.md), [10_Commercial_RealEstate_Addendum](../core/10_Commercial_RealEstate_Addendum.md)
- Вспомогательные: [Formats_and_Acceptance](../supplementary/Formats_and_Acceptance.md), [LC_Map_and_Gates](../supplementary/LC_Map_and_Gates.md), [CDE_and_Data_Model](../supplementary/CDE_and_Data_Model.md), [AWP_and_Execution_Planning](../supplementary/AWP_and_Execution_Planning.md), [System_Readiness_and_Cx_Details](../supplementary/System_Readiness_and_Cx_Details.md), [OandM_Commercial_RealEstate](../supplementary/OandM_Commercial_RealEstate.md), [KPI_and_Reporting_Details](../supplementary/KPI_and_Reporting_Details.md), [Roles_and_Responsibility](../supplementary/Roles_and_Responsibility.md), [Ready_Templates_and_Forms](../supplementary/Ready_Templates_and_Forms.md), [Mini_Implementation_Guide](../supplementary/Mini_Implementation_Guide.md)
