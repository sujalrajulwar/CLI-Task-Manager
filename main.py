from task_manager.task_manager import (
    add_task,
    view_tasks,
    mark_task_completed,
    delete_task,
)

from storage.storage import load_tasks


tasks = load_tasks()


while True:
    print("===== TASK MANAGER =====")
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Mark Task Completed")
    print("4.Delete Task")
    print("5.Exit")

    try:
        choice = int(input("Enter the choice : "))

    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print("1.Add Tasks Selected")
        title = input("Enter task title : ")
        add_task(tasks, title)

    elif choice == 2:
        if not tasks:
            print("No Tasks Available")
        else:
            view_tasks(tasks)

    elif choice == 3:
        print("3.Mark Task Completed Selected")
        try:
            if not tasks:
                print("No Tasks Available")

            else:
                view_tasks(tasks)
                task_choice = int(input("Enter task number to mark as completed : "))

                if task_choice >= 1 and task_choice <= len(tasks):
                    mark_task_completed(tasks, task_choice)
                else:
                    print("Invalid Task Number")

        except ValueError:
            print("Invalid input, Please Enter the number ")

    elif choice == 4:
        print("4.Delete Task Selected")

        try:
            if not tasks:
                print("No task available")
            else:
                view_tasks(tasks)
                delete_choice = int(input("Enter task number you have to delete : "))

                if delete_choice >= 1 and delete_choice <= len(tasks):
                    delete_task(tasks, delete_choice)
                else:
                    print("Enter a valid number ")

        except ValueError:
            print("Invalid input ,Please Enter the number ")

    elif choice == 5:
        print("Exit The Program")
        break

    else:
        print("Invalid Choice! ")
