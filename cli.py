#!/usr/bin/env python3

import argparse
from todo.tasks import add_task, list_tasks, mark_done, remove_task

def main():
	parser = argparse.ArgumentParser(description="CLI To-Do list")
	subparsers = parser.add_subparsers(dest="command")

	# Добавить задачу
	parser_add = subparsers.add_parser("add", help="Add a new task")
	parser_add.add_argument("title", type=str, help="Task name")
	parser_add.add_argument("--priority", type=str, default="normal", help="Task priority")

	# Просмотр задач
	parse_list = subparsers.add_parser("list", help="Show tasks")
	parse_list.add_argument("--pending", help="Show only uncompleted tasks")
	parse_list.add_argument("--done", help="Show only completed tasks")

	# Отметить задачу как выполненную
	parse_done = subparsers.add_parser("done", help="Reply the task as completed")
	parse_done.add_argument("id", type=int, help="Task ID")

	# Удалить задачу
	parse_remove = subparsers.add_parser("remove", help="Delete task")
	parse_remove.add_argument("id", type=int, help="Task ID")

	args = parser.parse_args()

	if args.command == "add":
		add_task(args.title, args.priority)
	elif args.command == "list":
		status = None
		if args.pending:
			status = "pending"
		elif args.done:
			status = "done"

		list_tasks(status)
	elif args.command == "done":
		mark_done(args.id)
	elif args.command == "remove":
		remove_task(args.id)
	else:
		parser.print_help()

if __name__ == "__main__":
	main()