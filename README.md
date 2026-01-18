## SauceDemo Login Tests (Playwright)

Проект с автотестами для страницы логина сайта https://www.saucedemo.com/  
Тесты написаны на Python с использованием Playwright и pytest.

## Структура проекта

- `pages/` — Page Object классы
  - `base_page.py` — базовая страница с общими методами
  - `login_page.py` — Page Object страницы логина SauceDemo
- `tests/` — автотесты
  - `test_login.py` — тесты авторизации
- `conftest.py` — фикстуры pytest
- `pytest.ini` — настройки pytest
- `README.md` — описание проекта

## Покрытые тест-кейсы

- **SD-001** — Авторизация с корректными данными  
- **SD-002** — Авторизация с неверным паролем  
- **SD-003** — Авторизация с пустыми полями  

## Запуск тестов

1. Установить зависимости:
```bash
pip install pytest-playwright
playwright install
