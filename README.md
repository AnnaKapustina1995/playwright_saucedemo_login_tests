## SauceDemo Login Tests (Playwright)

Проект с автотестами для страницы логина сайта https://www.saucedemo.com/  
Тесты написаны на Python с использованием Playwright и pytest.

## Структура проекта

- `pages/` — Page Object классы
  - `base_page.py` — базовая страница с общими методами и базовым URL
  - `login_page.py` — Page Object страницы логина SauceDemo
- `tests/` — автотесты
  - `test_login.py` — тесты авторизации
- `conftest.py` — pytest-фикстуры
- `pytest.ini` — настройки pytest
- `requirements.txt` — зависимости проекта
- `README.md` — описание проекта

## Покрытые тест-кейсы

- Авторизация с корректными данными  
- Авторизация с неверным паролем  
- Авторизация с пустыми полями  

## Запуск тестов

1. Установить зависимости:
```bash
pip install -r requirements.txt
playwright install
