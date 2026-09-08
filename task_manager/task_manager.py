from storage.storage import save_tasks


def add_task(tasks, title):
    task = {"title": title, "status": "Pending"}
    tasks.append(task)
    save_tasks(tasks)
    print("Tasks Added Successfully")


def view_tasks(tasks):
    if not tasks:
        print("No Tasks Available")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['status']}")


def mark_task_completed(tasks, task_number):
    task = tasks[task_number - 1]
    task["status"] = "Completed"
    save_tasks(tasks)
    print("Task marked as Completed")


def delete_task(tasks, task_number):
    tasks.pop(task_number - 1)
    save_tasks(tasks)
    print("Task deleted successfully ")
