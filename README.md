# ygo-tournment-api
Ygo-Tournment-api é um aplicativo Django Full Stack que conecta duelistas em uma plataforma organizada para gerenciamento de torneios. Os usuários podem criar contas, editar seus perfis e decks, se inscrever em torneios, e visualizar informações detalhadas desse torneio, quem ta inscrito, horario, local, etc. Administradores têm permissões adicionais para criar e gerenciar torneios.

### Funcionalidade
- Criação de Usuário: Cadastre-se e gerencie seu perfil.
- Gerenciamento de Decks: Crie, edite e liste seus decks.
- Inscrição em Torneios: Participe de torneios listados na plataforma.
Informações dos Torneios: Visualize detalhes como:

    - Nome do torneio
    - Data de início
    - Data-limite de inscrição
    - Taxa de inscrição
    - Local do evento
### Para administradores:

- Criação e Gerenciamento de Torneios: Crie torneios, defina os detalhes e gerencie as inscrições.
## 2. Tecnologias Utilizadas
- __Back-end:__ Django 4.x
- __Front-end:__ Templates Django (HTML, CSS, JS)
- __Banco de Dados:__ SQLite (ou MySQL/PostgreSQL para produção)
- __Outros:__ Bootstrap para estilização

## 3. Como Rodar o Projeto localmente:

### Pré-requisitos
- Python 3.9 ou superior
- Virtualenv (opcional, mas recomendado)
- Git
- Pip

### Passos:

1. Clone o repositório:
```
git clone https://github.com/seu-usuario/duelist-hub.git
cd duelist-hub
```

2. Crie e ative o ambiente virtual:
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Realize as migrações do banco de dados:
```
python manage.py makemigrations
python manage.py migrate
```

5. Inicie o servidor local:
```
python manage.py runserver
```

6. Acesse o app no navegador:
```
http://127.0.0.1:8000
```