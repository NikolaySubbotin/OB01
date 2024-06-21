# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task:
    tasks = []

    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status
        Task.tasks.append(self)

    def mark_completed(self):
        self.status = True

    @staticmethod
    def add_task(task_description, due_date):
        new_task = Task(task_description, due_date)
        print(f"Задача '{new_task.description}' успешно добавлена.")

    @staticmethod
    def show_current_tasks():
        print("Текущие задачи (не выполненные):")
        for task in Task.tasks:
            if not task.status:
                print(f"{task}")

    @staticmethod
    def show_completed_tasks():
        print("Выполненные задачи:")
        for task in Task.tasks:
            if task.status:
                print(f"{task}")

    def __str__(self):
        status = "Выполнено" if self.status else "Не выполнено"
        return f"{self.description} (Срок: {self.deadline}) - Статус: {status}"


# Пример использования:
Task.add_task("Сделать ужин", "2024-06-22")
Task.add_task("Купить продукты", "2024-06-23")
Task.add_task("Проверить дз", "2024-06-24")

# Отметим некоторые задачи как выполненные
Task.tasks[0].mark_completed()  # Сделать ужин выполнено
Task.tasks[2].mark_completed()  # Проверить дз выполнено

# Вывод списка текущих задач
Task.show_current_tasks()

# Вывод списка выполненных задач
Task.show_completed_tasks()