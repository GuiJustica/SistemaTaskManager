from typing import List, Optional
from .repository import TaskRepository
from .task import Task, Status
from datetime import datetime


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def criar_tarefa(self, titulo: str, descricao: str, prioridade, prazo: datetime) -> Task:
        task = Task(None, titulo, descricao, prioridade, prazo)
        task.validar()
        return self.repository.save(task)

    def listar_todas(self) -> List[Task]:
        return self.repository.find_all()

    def atualizar_status(self, id: int, status: Status) -> Optional[Task]:
        task = self.repository.find_by_id(id)
        if not task:
            return None
        task.status = status
        self.repository.storage.add(task.id, task)
        return task

    def deletar(self, id: int) -> bool:
        return self.repository.delete(id)

    def buscar_por_id(self, id: int) -> Optional[Task]:
        return self.repository.find_by_id(id)
