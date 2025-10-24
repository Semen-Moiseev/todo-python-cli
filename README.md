# todo-python-cli

`ToDo` — это консольный инструмент, который позволяет следить за выполнением личных задач

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
python -m todo.cli <команда>
```

Аргументы:

- title — название задачи (обязательный) + --priority — приоритет задачи
- list — вывод задач (обязательный) + --pending — только невыполненные + --done — только выполненные
- done — отметить задачу выполненной + --id
- remove — удалить задачу + --id
