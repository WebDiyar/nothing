import unittest
import timeit
from task_manager import Task, TaskManager

class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.is_completed = False

    def complete(self):
        self.is_completed = True

    def __repr__(self):
        status = "Done" if self.is_completed else "Pending"
        return f"Task({self.task_id}, {self.description}, {status})"


class TaskManager:
    def __init__(self):
        self.tasks = {}   # Dictionary to store tasks with task_id as key.
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            raise ValueError("Task not found")

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].complete()
        else:
            raise ValueError("Task not found")

    def get_all_tasks(self):
        return list(self.tasks.values())

# -------------------------------
# Test A
# -------------------------------
class TestA(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_and_complete_task_integration(self):
        task = self.manager.add_task("Write integration tests")
        self.manager.complete_task(task.task_id)
        self.assertTrue(task.is_completed)

    def test_remove_task_integration(self):
        task = self.manager.add_task("Task to remove")
        self.manager.remove_task(task.task_id)
        self.assertNotIn(task.task_id, self.manager.tasks)


# -------------------------------
# Test B
# -------------------------------
class TestB(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_full_task_flow(self):
        task1 = self.manager.add_task("Buy groceries")
        task2 = self.manager.add_task("Call John")
        task3 = self.manager.add_task("Pay bills")
        self.manager.complete_task(task2.task_id)
        tasks = self.manager.get_all_tasks()
        self.assertEqual(len(tasks), 3)
        completed_tasks = [t for t in tasks if t.is_completed]
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(completed_tasks[0].task_id, task2.task_id)


# -------------------------------
# Test C
# -------------------------------
class TestC(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_tasks_performance(self):
        # Measure performance of adding 10,000 tasks.
        def add_tasks():
            for i in range(10000):
                self.manager.add_task(f"Task {i}")

        elapsed = timeit.timeit(add_tasks, number=1)
        # Arbitrary performance threshold (e.g., under 1 second)
        self.assertLess(elapsed, 1.0, f"Adding tasks took too long: {elapsed} seconds")


# -------------------------------
# Test D
# -------------------------------
class TestD(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_remove_nonexistent_task_regression(self):
        with self.assertRaises(ValueError):
            self.manager.remove_task(999)

    def test_complete_nonexistent_task_regression(self):
        with self.assertRaises(ValueError):
            self.manager.complete_task(888)


if __name__ == '__main__':
    unittest.main()

