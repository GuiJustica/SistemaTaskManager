from datetime import datetime,timedelta
import pytest
from ..task_manager.repository import TaskRepository
from ..task_manager.task import Task, Priority
from types import SimpleNamespace


def test_save_atribui_id(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc", Priority.BAIXA, datetime.now() + timedelta(days=1))
    resultado = repo.save(task)
    assert resultado.id == 1
    mock_storage.add.assert_called_once_with(1, resultado)


def test_save_chama_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "T2", "Desc2", Priority.MEDIA, datetime.now() + timedelta(days=1))
    repo.save(task)
    mock_storage.add.assert_called_once()


def test_find_by_id_chama_storage_get(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    # preparar retorno do storage.get
    fake_task = SimpleNamespace(id=1, titulo="X")
    mock_storage.get.return_value = fake_task
    resultado = repo.find_by_id(1)
    mock_storage.get.assert_called_once_with(1)
    assert resultado is fake_task


def test_find_all_retorna_lista(mocker):
    mock_storage = mocker.Mock()
    fake_task1 = SimpleNamespace(id=1, titulo="A")
    fake_task2 = SimpleNamespace(id=2, titulo="B")
    mock_storage.get_all.return_value = [fake_task1, fake_task2]
    repo = TaskRepository(mock_storage)
    resultado = repo.find_all()
    assert isinstance(resultado, list)
    assert len(resultado) == 2
    mock_storage.get_all.assert_called_once()
