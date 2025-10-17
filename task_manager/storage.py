# task_manager/storage.py
from typing import Any, Dict, List, Optional


class InMemoryStorage:
    def __init__(self) -> None:
        self._data: Dict[int, Any] = {}

    def add(self, id: int, item: Any) -> None:
        self._data[id] = item

    def get(self, id: int) -> Optional[Any]:
        return self._data.get(id)

    def get_all(self) -> List[Any]:
        return list(self._data.values())

    def delete(self, id: int) -> bool:
        if id in self._data:
            del self._data[id]
            return True
        return False

    def clear(self) -> None:
        self._data.clear()
