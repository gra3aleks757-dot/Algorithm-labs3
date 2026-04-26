from main import Queue, Task

def test_enqueue_and_size():
    print("Тест 1: Добавление и размер")
    q = Queue()
    q.enqueue(Task(1, "Задача 1", "высокий"))
    q.enqueue(Task(2, "Задача 2", "средний"))
    assert q.size() == 2
    print("Пройдено!\n")

def test_no_duplicate_id():
    print("Тест 2: Запрет одинаковых id")
    q = Queue()
    q.enqueue(Task(1, "Оригинал", "высокий"))
    result = q.enqueue(Task(1, "Дубликат", "низкий"))
    assert result == False
    assert q.size() == 1
    print("Пройдено!\n")

def test_dequeue():
    print("Тест 3: Удаление из очереди")
    q = Queue()
    q.enqueue(Task(1, "Первый", "высокий"))
    q.enqueue(Task(2, "Второй", "средний"))
    deleted = q.dequeue()
    assert deleted.id == 1
    assert q.size() == 1
    assert q.front().id == 2
    print("Пройдено!\n")

def test_front():
    print("Тест 4: Просмотр первого элемента")
    q = Queue()
    q.enqueue(Task(5, "Пятая", "низкий"))
    q.enqueue(Task(6, "Шестая", "средний"))
    assert q.front().id == 5
    assert q.size() == 2
    print("Пройдено!\n")

def test_is_empty():
    print("Тест 5: Проверка пустоты")
    q = Queue()
    assert q.is_empty() == True
    q.enqueue(Task(1, "Задача", "средний"))
    assert q.is_empty() == False
    q.dequeue()
    assert q.is_empty() == True
    print("Пройдено!\n")

def test_find_by_id():
    print("Тест 6: Поиск по id")
    q = Queue()
    q.enqueue(Task(10, "Десять", "высокий"))
    q.enqueue(Task(20, "Двадцать", "средний"))
    found = q.find_by_id(20)
    assert found.id == 20
    not_found = q.find_by_id(99)
    assert not_found == None
    print("Пройдено!\n")

def test_remove_by_id():
    print("Тест 7: Удаление по id")
    q = Queue()
    q.enqueue(Task(1, "Первый", "высокий"))
    q.enqueue(Task(2, "Второй", "средний"))
    q.enqueue(Task(3, "Третий", "низкий"))
    removed = q.remove_by_id(2)
    assert removed.id == 2
    assert q.size() == 2
    assert q.front().id == 1
    print("Пройдено!\n")

def test_count_completed():
    print("Тест 8: Счетчик выполненных")
    q = Queue()
    assert q.count_completed() == 0
    q.enqueue(Task(1, "Задача 1", "высокий"))
    q.enqueue(Task(2, "Задача 2", "средний"))
    q.dequeue()
    q.dequeue()
    assert q.count_completed() == 2
    print("Пройдено!\n")

def test_has_id():
    print("Тест 9: Проверка наличия id")
    q = Queue()
    q.enqueue(Task(100, "Сотая", "высокий"))
    assert q.has_id(100) == True
    assert q.has_id(200) == False
    print("Пройдено!\n")

def test_clear():
    print("Тест 10: Очистка очереди")
    q = Queue()
    q.enqueue(Task(1, "Один", "низкий"))
    q.enqueue(Task(2, "Два", "низкий"))
    q.enqueue(Task(3, "Три", "низкий"))
    q.clear()
    assert q.is_empty() == True
    assert q.size() == 0
    print("Пройдено!\n")

def test_string_representation():
    print("Тест 11: Строковое представление")
    q = Queue()
    assert str(q) == "Queue[]"
    q.enqueue(Task(1, "Первый", "высокий"))
    q.enqueue(Task(2, "Второй", "средний"))
    result = str(q)
    assert "id=1" in result
    assert "id=2" in result
    print("Пройдено!\n")

def run_all_tests():
    print("\n" + "=" * 50)
    print("ЗАПУСК ТЕСТОВ")
    print("=" * 50 + "\n")
    
    test_enqueue_and_size()
    test_no_duplicate_id()
    test_dequeue()
    test_front()
    test_is_empty()
    test_find_by_id()
    test_remove_by_id()
    test_count_completed()
    test_has_id()
    test_clear()
    test_string_representation()
    
    print("=" * 50)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    print("=" * 50)

if __name__ == "__main__":
    run_all_tests()
