from __future__ import annotations

from datetime import datetime

from dataclasses import dataclass, field
from typing import Optional

from enum import IntEnum
class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


from enum import Enum
class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"
class Task:
    def __init__(self, id, titulo, descricao, prioridade: Priority, prazo: datetime, status: Status = Status.PENDENTE):
            self.id = id
            self.titulo = titulo
            self.descricao = descricao
            self.prioridade = prioridade
            self.prazo = prazo
            self.status = status


    def validar(self) -> None:
        """Valida título e prazo. Lança ValueError se inválido."""
        if not isinstance(self.titulo, str) or len(self.titulo.strip()) < 3:
            raise ValueError("Título deve ter pelo menos 3 caracteres.")
        if not isinstance(self.prazo, datetime):
            raise ValueError("Prazo deve ser um datetime válido.")
        now = datetime.now()
        # prazo não pode ser no passado (aceita prazo igual a agora+0? considerando passado estrito)
        if self.prazo <= now:
            raise ValueError("Prazo não pode ser no passado.")
