#!/usr/bin/env python3

import json
from pathlib import Path

tasks_file = Path("data/tasks.json")

def load_tasks():
	if tasks_file.exists():
		with tasks_file.open("r", encoding="utf-8") as f:
			return json.load(f)
	else:
		print(f"The file {tasks_file} was not found!")
		return []

def save_tasks(tasks):
	with tasks_file.open("w", encoding="utf-8") as f:
		json.dump(tasks, f, indent=2, ensure_ascii=False)
