#!/usr/bin/env python3

from datetime import datetime
from .storage import load_tasks, save_tasks

def add_task(title, priority="normal"):
	tasks = load_tasks()
	task_id = max([t["id"] for t in tasks], default=0) + 1
	task = {
		"id": task_id,
		"title": title,
		"priority": priority,
		"status": "pending",
		"created_at": datetime.now().isoformat()
	}

	tasks.append(task)
	save_tasks(tasks)
	print(f"Task added {title} (ID: {task_id})")

def list_tasks(show_status=None):
	tasks = load_tasks()
	if show_status:
		tasks = [t for t in tasks if t["status"] == show_status]
	if not tasks:
		print("Task list is empty!")
		return
	for t in tasks:
		status = "✅" if t["status"] == "done" else "❌"
		print(f"[{status}] ID {t['id']}: {t['title']} (Priority: {t['priority']})")

def mark_done(task_id):
	tasks = load_tasks()
	for t in tasks:
		if t["id"] == task_id:
			t["status"] = "done"
			save_tasks(tasks)
			print(f"Task ID {task_id} completed!")
			return
	print(f"Task ID {task_id} not found!")

def remove_task(task_id):
	tasks = load_tasks()
	new_task_list = [t for t in tasks if t["id"] != task_id]
	if len(new_task_list) == len(tasks):
		print(f"Task id {task_id} not found!")
	else:
		save_tasks(new_task_list)
		print(f"Task ID {task_id} deleted!")