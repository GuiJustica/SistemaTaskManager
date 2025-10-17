Sistema Task Manager

Objetivo

Desenvolver um Sistema de Gerenciamento de Tarefas simples em Python, aplicando:

• Arquitetura em camadas

• Testes automatizados com pytest

• Separação de responsabilidades


Instalar dependências:
pip install -r requirements.txt

Executar testes:
pytest -v

Estrutura do Projeto
  -task_manager/
    -task.py
    -storage.py
    -repository.py
    -service.py
  -tests/
    -test_task.py
    -test_repository.py
  -requirements.txt
  -README.md
