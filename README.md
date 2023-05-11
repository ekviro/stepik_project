# Учебный проект по автоматизации тестирования (курс на степике)

## _Не клонировать в папку с дефисами в имени (тесты не запустятся)_

## Версия интерпретатора python
Python 3.10

## Браузер и драйвер
Протестировано на версиях Google Chrome	и ChromeDriver 112.0.5615.49 и 113.0.5672.93


## Запуск тестов с разными параметрами
pytest -v --tb=line --language=en test_main_page.py

pytest -s test_product_page.py

### Запуск итоговых тестов для ревью:
pytest -v --tb=line --language=en -m need_review


