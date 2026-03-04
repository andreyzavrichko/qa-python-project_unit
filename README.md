# Stellar Burgers — Юнит-тесты

Юнит-тесты для программы заказа бургеров. Покрывают классы `Bun`, `Burger`, `Ingredient`, `Database`.

## Структура

```
├── praktikum/       # код программы
├── tests/           # тесты
├── htmlcov/         # отчёт покрытия (генерируется)
├── conftest.py
├── pytest.ini
└── requirements.txt
```

## Запуск

```bash
pip install -r requirements.txt
pytest --cov=praktikum --cov-report=html
```

Отчёт покрытия: `htmlcov/index.html`
