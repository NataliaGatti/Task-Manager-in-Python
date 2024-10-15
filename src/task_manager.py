class Task:
  def __init__(self, description):
    self.description = description
    self.is_completed = False

  def mark_completed(self):
    self.is_completed = True
    
  def __str__(self):
    status = "✔️" if self.is_completed else "❌"
    return f"{self.description} {status}"

class ToDoList:
  def __init__(self):
    self.tasks = []

  def add_task(self):
    description = input("Enter the task description: ")
    new_task = Task(description)
    self.tasks.append(new_task)
    print(f'Task "{description}" added successfully.\n')

  def complete_task(self):
    self.view_tasks()
    if not self.tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to complete: "))
        if 1 <= task_num <= len(self.tasks):
            self.tasks[task_num - 1].mark_completed()
            print(f'Task "{self.tasks[task_num - 1].description}" marked as completed.\n')
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

  def view_tasks(self):
    if not self.tasks:
        print("No tasks available.\n")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
        print()
          
  def run(self):
    while True:
      print("1. Add a new task")
      print("2. Complete a task")
      print("3. View all tasks")
      print("4. Exit")
      choice = input("Choose an option: ")

      if choice == "1":
          self.add_task()
      elif choice == "2":
          self.complete_task()
      elif choice == "3":
          self.view_tasks()
      elif choice == "4":
          print("Exiting the Task Manager. Goodbye!")
          break
      else:
          print("Invalid option, please choose again.\n")


if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()