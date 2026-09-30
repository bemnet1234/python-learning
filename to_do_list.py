
def add_task(task_list):
    task = input("Enter a new task: ")
    task_list.append(task)
    print(f"Task '{task}' added.")
def view_tasks(task_list):
    if not task_list:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task}")   
def mark_task_complete(task_list):
    view_tasks(task_list)
    if not task_list:
        return
    task_number = int(input("Enter the number of the task to mark as complete: "))
    if 1 <= task_number <= len(task_list):
        completed_task = task_list.pop(task_number - 1)
        print(f"Task '{completed_task}' marked as complete.")
    else:
        print("Invalid task number.")
def remove_task(task_list):
    view_tasks(task_list)
    if not task_list:
        return
    task_number = int(input("Enter the number of the task to remove: "))
    if 1 <= task_number <= len(task_list):
        removed_task = task_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number.")
def main():
    task_list = []
    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_task(task_list)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            mark_task_complete(task_list)
        elif choice == '4':
            remove_task(task_list)
        elif choice == '5':
            print("Exiting the Todo List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
