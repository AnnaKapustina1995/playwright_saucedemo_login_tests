## SauceDemo UI Tests (Playwright)

Проект с автотестами для сайта https://www.saucedemo.com/  
Тесты покрывают авторизацию, работу с корзиной и полный процесс оформления заказа.

Используется Playwright + pytest.  
Поддерживается генерация Allure-отчетов для анализа результатов тестирования.

---

## Структура проекта

- `pages/` — Page Object классы
  - `base_page.py` — базовая страница с общими методами и базовым URL
  - `login_page.py` — Page Object страницы логина
  - `inventory_page.py` — Page Object страницы со списком товаров
  - `cart_page.py` — Page Object страницы корзины
  - `checkout_page.py` — Page Object страницы оформления заказа
  - `checkout_complete_page.py` — Page Object страницы успешного оформления заказа
- `tests/` — автотесты
  - `test_login.py` — тесты авторизации
  - `test_cart.py` — тесты корзины
  - `test_checkout.py` — тест полного сценария покупки
- `conftest.py` — pytest-фикстуры
- `pytest.ini` — настройки pytest
- `requirements.txt` — зависимости проекта

---

## Покрытые тест-кейсы

- Авторизация с корректными данными  
- Авторизация с неверными данными  
- Авторизация с пустыми полями  
- Добавление товаров в корзину  
- Удаление товара из корзины  
- Полный процесс оформления заказа  

---

## Запуск тестов и Allure отчёты

Установка зависимостей:
```bash
pip install -r requirements.txt
playwright install
```

Обычный запуск тестов:
```bash
pytest
```

Запуск тестов с генерацией Allure-результатов:
```bash
pytest --alluredir=allure-results
```

Просмотр Allure-отчета (если установлен Allure CLI):
```bash
allure serve allure-results
```

Папки `allure-results` и `allure-report` исключены из репозитория через `.gitignore`.

---

## Примечание

Проект разделён на ветки:
- `main` — актуальная версия проекта  
- `feature/cart-tests` — тесты корзины  
- `feature/checkout-flow` — тест полного сценария покупки  
- `feature/allure-report` — интеграция Allure отчетов  
