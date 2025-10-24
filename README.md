# todo-python-cli

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/<your-username>/todo-python-cli.git
cd todo-python-cli
```

### 2. Создайте и активируйте виртуальное окружение

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux / macOS
```

## Использование

```bash
python cli.py <команда>
```

Аргументы:

- check — Проверка API, + config — путь к файлу с эндпоинтами
- stats — Вывод и сохранение в файл статистики проверок
