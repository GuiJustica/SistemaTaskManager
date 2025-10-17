import pytest
from datetime import datetime, timedelta
from ..task_manager.task import Task, Priority, Status


def test_task_valida():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Estudar", "Python", Priority.ALTA, prazo)
    # não deve lançar
    task.validar()
    assert task.titulo == "Estudar"
    assert task.status == Status.PENDENTE


def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Desc", Priority.BAIXA, prazo)
    with pytest.raises(ValueError):
        task.validar()


def test_prazo_no_passado_invalido():
    prazo = datetime.now() - timedelta(days=1)
    task = Task(None, "Tarefa", "Desc", Priority.MEDIA, prazo)
    with pytest.raises(ValueError):
        task.validar()


# Teste extra (requisito 2: adicionar pelo menos 3 testes)
def test_prazo_tipo_invalido():
    # prazo deve ser datetime
    task = Task(None, "Titulo válido", "Desc", Priority.BAIXA, "2025-01-01")
    with pytest.raises(ValueError):
        task.validar()
