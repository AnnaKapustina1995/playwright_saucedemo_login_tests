# playwright_saucedemo_login_tests

## SauceDemo Login Tests (Playwright)

Проект с автотестами для страницы логина сайта https://www.saucedemo.com/  
Тесты написаны на Python с использованием Playwright и pytest.

## Структура проекта

- `pages/` — Page Object модули  
  - `base_page.py` — базовый класс страницы  
  - `login_page.py` — Page Object для страницы логина
- `tests/` — автотесты
  - `test_login.py` — тесты авторизации
- `conftest.py` — фикстуры pytest
- `.gitignore` — исключения для Git

## Покрытые тест-кейсы

- **SD-001** — Авторизация с корректными данными  
- **SD-002** — Авторизация с неверным паролем  
- **SD-003** — Авторизация с пустыми полями  

## Запуск тестов

1. Установить зависимости:
```bash
pip install pytest-playwright
playwright install
