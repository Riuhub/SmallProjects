def View_tasks(ToDoList):
    if not ToDoList:
        print("No tasks yet.")
    else:
        for i, task in enumerate(ToDoList, start=1):
            print(f"{i}. {task}")


def Add_tasks(ToDoList):
    task_input = input("Which task would you like to add: ").strip()
    if not task_input:
        print("Task cannot be empty.")
    else:
        ToDoList.append(task_input)

        print("Task added.")


def Remove_tasks(ToDoList):
    if not ToDoList:
        print("No tasks to remove.")
        return

    for i, task in enumerate(ToDoList, start=1):
        print(f"{i}. {task}")

    task_remove = input("Enter the number of the task you want to remove: ")

    if not task_remove.isdigit():
        print("Please enter a valid number.")
        return

    index = int(task_remove) - 1

    if index < 0 or index >= len(ToDoList):
        print("Task number doesn't exist.")
        return

    confirm = input(f"Are you sure you want to remove '{ToDoList[index]}'? (y/n): ").lower()
    if confirm == 'y':
        removed = ToDoList.pop(index)
        print(f"Removed: {removed}")
    else:
        print("Canceled.")
    

ToDoList = []
choices = ['1', '2', '3', '4']

choice = None

while choice != '4':

    choice = input("1. View tasks , 2. Add task , 3. Remove task, 4. Exit: ")

    if choice not in choices:
        print("Wrong input, try again.")
        continue

    if choice == '1':
        View_tasks(ToDoList)

    elif choice == '2':
        Add_tasks(ToDoList)

    elif choice == '3':
        Remove_tasks(ToDoList)

print("Goodbye!")
