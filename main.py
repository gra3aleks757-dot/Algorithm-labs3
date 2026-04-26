class Task:
    def __init__(self, task_id, description, priority):
        self.id = task_id
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"[id={self.id}] {self.description} (приоритет: {self.priority})"


class Queue:
    def __init__(self):
        self.items = []
        self.completed_count = 0

    def enqueue(self, task):
        if self._find_by_id(task.id) is not None:
            print(f"Ошибка: задача с id={task.id} уже существует! Не добавлена.")
            return False
        self.items.append(task)
        print(f"Задача добавлена: {task}")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста, нечего удалять")
            return None
        task = self.items.pop(0)
        self.completed_count += 1
        print(f"Задача выполнена и удалена: {task}")
        return task

    def front(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()
        print("Очередь очищена")

    def display_all(self):
        if self.is_empty():
            print("Очередь пуста")
            return
        print("\n=== Все задачи в очереди ===")
        for i, task in enumerate(self.items, 1):
            print(f"{i}. {task}")
        print("===========================\n")

    def find_by_id(self, task_id):
        task = self._find_by_id(task_id)
        if task:
            print(f"Найдена задача: {task}")
        else:
            print(f"Задача с id={task_id} не найдена")
        return task

    def _find_by_id(self, task_id):
        for task in self.items:
            if task.id == task_id:
                return task
        return None

    def remove_by_id(self, task_id):
        task = self._find_by_id(task_id)
        if task is None:
            print(f"Задача с id={task_id} не найдена")
            return None
        self.items.remove(task)
        print(f"Удалена задача: {task}")
        return task

    def count_completed(self):
        return self.completed_count

    def has_id(self, task_id):
        exists = self._find_by_id(task_id) is not None
        print(f"id={task_id} {'присутствует' if exists else 'отсутствует'} в очереди")
        return exists

    def __str__(self):
        if self.is_empty():
            return "Queue[]"
        tasks_str = " -> ".join(str(task) for task in self.items)
        return f"Queue[{tasks_str}]"


def main():
    print("=" * 50)
    print("СИСТЕМА ОБРАБОТКИ ЗАДАЧ")
    print("=" * 50)

    q = Queue()

    print("\n1. Добавление задач:")
    q.enqueue(Task(1, "Сделать лабораторную работу", "высокий"))
    q.enqueue(Task(2, "Написать отчет", "средний"))
    q.enqueue(Task(3, "Загрузить код на Github", "низкий"))

    print("\n2. Попытка добавить задачу с существующим id (id=1):")
    q.enqueue(Task(1, "Повторная задача", "высокий"))

    print("\n3. Вывод всех задач:")
    q.display_all()

    print(f"4. Размер очереди: {q.size()}")

    print(f"\n5. Первая задача в очереди (front): {q.front()}")

    print("\n6. Поиск задачи по id=2:")
    q.find_by_id(2)

    print("\n7. Проверка наличия id=5:")
    q.has_id(5)

    print("\n8. Удаление задачи по id=2:")
    q.remove_by_id(2)
    q.display_all()

    print("\n9. Выполнение задач (dequeue):")
    q.dequeue()
    q.dequeue()

    print(f"\n10. Количество выполненных задач: {q.count_completed()}")

    print(f"\n11. Очередь пуста? {q.is_empty()}")

    print("\n12. Добавим новые задачи:")
    q.enqueue(Task(10, "Сдать работу", "высокий"))
    q.enqueue(Task(11, "Получить оценку", "средний"))
    print(f"\n13. Строковое представление очереди:\n{q}")

    print("\n14. Очистка очереди:")
    q.clear()
    print(f"Очередь пуста? {q.is_empty()}")

if __name__ == "__main__":
    main()
