class Task:
    def __init__(self, id, description, priority):
        self.id = id
        self.description = description
        self.priority = priority


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, task):
        for existing_task in self.items:
            if existing_task.id == task.id:
                print(f"Ошибка: Задача с id {task.id} уже существует")
                return False
        self.items.append(task)
        return True

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    queue = Queue()
    task1 = Task(1, "Сделать домашнее задание", 2)
    task2 = Task(2, "Помыть посуду", 1)
    task3 = Task(3, "Выгулять собаку", 3)
    
    queue.enqueue(task1)
    queue.enqueue(task2)
    queue.enqueue(task3)
    
    task_duplicate = Task(1, "Повторная задача", 5)
    queue.enqueue(task_duplicate)  
    
    print(queue.front())
    
    
    print(queue.dequeue()) 
    print(queue.dequeue()) 
    
    
    print(f"Осталось задач: {len(queue.items)}")  # 1
    
    print(queue.dequeue()) 
    print(queue.is_empty()) 
