# Database to Google Sheets Sync Automation

**English** | [Русский](#Русский)

## Description

A Python service that automates data synchronization from a client's PostgreSQL database to Google Sheets. Running autonomously on a Linux server, it ensures that managers always have access to an up-to-date view of the product assortment directly from the database, eliminating manual data export and reducing errors.

## Key Functionalities

*   **Scheduled Data Extraction:** Connects to a PostgreSQL database to fetch the latest product assortment data.
*   **Secure Connection:** Establishes a reliable and secure connection, potentially using SSH tunneling for enhanced security.
*   **Google Sheets API Integration:** Automatically updates predefined Google Sheets with the new data, keeping them synchronized.
*   **Telegram Monitoring:** Sends status reports on script execution, successful updates, and any errors to a dedicated Telegram channel for operational transparency.

## Tech Stack

*   Python
*   Psycopg2 (PostgreSQL adapter)
*   SSHTunnel
*   Gspread & Google API Client
*   Telegram Bot API

## Project Context & Development Notes

This automation was developed in 2023 to replace a manual and error-prone process of exporting and copying database information into spreadsheets. The goal was to provide the management team with a real-time, "single source of truth" for the product catalog.

The service was designed to be "set and forget." After the initial setup and deployment on the client's Linux server, it has required zero maintenance and continues to run reliably, demonstrating the robustness of the implementation.

The architecture handles the entire pipeline securely: from connecting to the database (using an SSH tunnel if required) to authenticating with the Google Sheets API and performing the structured data update.

## Why It's Here

This repository showcases my ability to:

*   Automate business workflows to replace manual, repetitive tasks and improve data accuracy.
*   Build reliable, long-running data pipeline services for production environments.
*   Integrate diverse systems (PostgreSQL, Google Workspace) via their APIs.
*   Implement secure authentication and connection methods (OAuth 2.0, SSH tunneling).
*   Develop solutions that empower non-technical teams by providing them with easy access to complex data.

---

# Русский

## Описание

Сервис на Python, который автоматизирует синхронизацию данных из PostgreSQL базы данных клиента в Google Таблицы. Работая автономно на Linux-сервере, он гарантирует, что менеджеры всегда имеют доступ к актуальным данным о товарном ассортименте прямо из базы данных, что исключает ручной экспорт и снижает количество ошибок.

## Ключевые функции

*   **Плановое извлечение данных:** Подключается к PostgreSQL базе данных для получения актуальных данных о товарном ассортименте.
*   **Безопасное соединение:** Устанавливает надежное и безопасное соединение, с возможностью использования SSH-туннеля для повышенной безопасности.
*   **Интеграция с Google Sheets API:** Автоматически обновляет заранее определённые Google Таблицы новыми данными, поддерживая их в актуальном состоянии.
*   **Мониторинг в Telegram:** Отправляет отчеты о статусе выполнения скрипта, успешных обновлениях и возникающих ошибках в выделенный Telegram-канал для обеспечения прозрачности операций.

## Стек технологий

*   Python
*   Psycopg2 (адаптер для PostgreSQL)
*   SSHTunnel
*   Gspread & Google API Client

## Контекст проекта и заметки о разработке

Данная автоматизация была разработана в 2023 году для замены ручного и подверженного ошибкам процесса экспорта и копирования информации из базы данных в электронные таблицы. Целью было предоставить управленческой команде единый и актуальный источник информации о товарном каталоге.

Сервис был спроектирован по принципу "установил и забыл". После первоначальной настройки и развертывания на Linux-сервере клиента он не потребовал никакого обслуживания и продолжает стабильно работать, что демонстрирует надежность реализации.

Архитектура безопасно обрабатывает весь пайплайн: от подключения к базе данных (с использованием SSH-туннеля при необходимости) до аутентификации в Google Sheets API и выполнения структурированного обновления данных.

## Почему этот проект здесь

Этот репозиторий демонстрирует мои способности:

*   Автоматизировать бизнес-процессы для замены ручных, повторяющихся задач и повышения точности данных.
*   Создавать надежные, долгоиграющие сервисы для передачи данных в production-окружении.
*   Интегрировать разнородные системы (PostgreSQL, Google Workspace) через их API.
*   Реализовывать безопасные методы аутентификации и соединения (OAuth 2.0, SSH tunneling).
*   Разрабатывать решения, которые дают возможность нетехническим командам легко работать со сложными данными.