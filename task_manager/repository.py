from typing import List, Optional
from .storage import InMemoryStorage
from .task import Task


class TaskRepository:
    def __init__(self, storage: InMemoryStorage) -> None:
        self.storage = storage
        self._next_id: int = 1

    def save(self, task: Task) -> Task:
        task.id = self._next_id
        self._next_id += 1
        self.storage.add(task.id, task)
        return task

    def find_by_id(self, id: int) -> Optional[Task]:
        return self.storage.get(id)

    def find_all(self) -> List[Task]:
        return self.storage.get_all()

    def delete(self, id: int) -> bool:
        return self.storage.delete(id)
