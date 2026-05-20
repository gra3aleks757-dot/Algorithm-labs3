import unittest
from main import Task, Queue


class TestQueue(unittest.TestCase):
    
    def test_enqueue_and_dequeue(self):
        queue = Queue()
        task = Task(1, "Тестовая задача", 1)
        
        queue.enqueue(task)
        result = queue.dequeue()
        
        self.assertEqual(result, task)
        self.assertTrue(queue.is_empty())
    
    def test_front(self):
        queue = Queue()
        task1 = Task(1, "Первая задача", 1)
        task2 = Task(2, "Вторая задача", 2)
        
        queue.enqueue(task1)
        queue.enqueue(task2)
        
        self.assertEqual(queue.front(), task1)
        self.assertFalse(queue.is_empty())  
        self.assertEqual(queue.dequeue(), task1)  
    
    def test_is_empty(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        task = Task(1, "Задача", 1)
        queue.enqueue(task)
        self.assertFalse(queue.is_empty())
        queue.dequeue()
        self.assertTrue(queue.is_empty())
    
    def test_fifo_order(self):
        queue = Queue()
        task1 = Task(1, "Задача 1", 1)
        task2 = Task(2, "Задача 2", 2)
        task3 = Task(3, "Задача 3", 3)
        queue.enqueue(task1)
        queue.enqueue(task2)
        queue.enqueue(task3)
        self.assertEqual(queue.dequeue(), task1)
        self.assertEqual(queue.dequeue(), task2)
        self.assertEqual(queue.dequeue(), task3)
    
    def test_dequeue_from_empty_queue(self):
        queue = Queue()
        result = queue.dequeue()
        self.assertIsNone(result)
    
    def test_front_from_empty_queue(self):
        queue = Queue()
        result = queue.front()
        self.assertIsNone(result)
    
    def test_no_duplicate_id(self):
        queue = Queue()
        task1 = Task(1, "Первая задача", 1)
        task2 = Task(1, "Задача с тем же id", 2)
        task3 = Task(2, "Задача с другим id", 3)
        result1 = queue.enqueue(task1)
        self.assertTrue(result1)
        self.assertEqual(len(queue.items), 1)
        result2 = queue.enqueue(task2)
        self.assertFalse(result2)
        self.assertEqual(len(queue.items), 1)  
        result3 = queue.enqueue(task3)
        self.assertTrue(result3)
        self.assertEqual(len(queue.items), 2)
    
    def test_enqueue_multiple_unique_ids(self):
        queue = Queue()
        task1 = Task(1, "Задача 1", 1)
        task2 = Task(2, "Задача 2", 2)
        task3 = Task(3, "Задача 3", 3)
        queue.enqueue(task1)
        queue.enqueue(task2)
        queue.enqueue(task3)
        self.assertEqual(len(queue.items), 3)
        self.assertEqual(queue.items[0], task1)
        self.assertEqual(queue.items[1], task2)
        self.assertEqual(queue.items[2], task3)
    
    def test_duplicate_id_does_not_change_queue(self):
        queue = Queue()
        task1 = Task(1, "Оригинал", 1)
        task2 = Task(2, "Другой", 2)
        task_duplicate = Task(1, "Дубликат", 3)
        queue.enqueue(task1)
        queue.enqueue(task2)
        original_length = len(queue.items)
        original_front = queue.front()
        queue.enqueue(task_duplicate)
        self.assertEqual(len(queue.items), original_length)
        self.assertEqual(queue.front(), original_front)
    
    def test_enqueue_return_value(self):
        queue = Queue()
        task1 = Task(1, "Новая задача", 1)
        task2 = Task(1, "Дубликат", 2)
        result1 = queue.enqueue(task1)
        self.assertTrue(result1)
        result2 = queue.enqueue(task2)
        self.assertFalse(result2)


def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestQueue)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*50)
    print(f"ИТОГ: Запущено тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Ошибок: {len(result.errors)}")
    print(f"Неудач: {len(result.failures)}")
    print("="*50)
    
    return result


if __name__ == "__main__":
    run_tests()
