class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" completed.')
        else:
            print('Invalid task index.')

    def menu(self):
        while True:
            print('\n==== To-Do List Menu ====')
            print('1. Add Task')
            print('2. View Tasks')
            print('3. Complete Task')
            print('4. Quit')

            choice = input('Enter your choice (1-4): ')

            if choice == '1':
                task = input('Enter the task: ')
                self.add_task(task)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                task_index = int(input('Enter the task index to complete: '))
                self.complete_task(task_index)
            elif choice == '4':
                print('Exiting the To-Do List app. Goodbye!')
                break
            else:
                print('Invalid choice. Please enter a number between 1 and 4.')


# Instantiate the ToDoList class and run the menu
if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.menu()