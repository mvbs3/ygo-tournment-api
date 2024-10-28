# ygo-tournment-api
Projeto de um sistema de ranking para torneios de Yu-Gi-Oh! para por em prática conhecimentos de Django e acesso a banco de dados.


## Configuração do Projeto Django
1. **Instalação do Django**

O primeiro passo é instalar o Django no ambiente de desenvolvimento. Isso pode ser feito usando o comando pip:

```bash
pip install django
#ou
sudo apt install python3-django
```
2. **Criação do Projeto Django**

Após instalar o Django, o próximo passo é criar um novo projeto. Um projeto no Django é um contêiner que abrigará todas as configurações e as aplicações específicas.

```bash
django-admin startproject nome_do_projeto
```
3. **Execução do Servidor de Desenvolvimento**

Uma vez criado o projeto, você pode iniciar o servidor de desenvolvimento local para verificar se tudo está funcionando corretamente.

```bash
python3 manage.py runserver
```
Acesse o servidor no navegador através do endereço http://127.0.0.1:8000/.

4. **Criação de uma Aplicação**

No Django, uma aplicação é uma parte independente do projeto, com funcionalidades específicas. Para criar uma aplicação dentro do projeto, use o comando:

```bash
python3 manage.py startapp nome_da_aplicacao
```
## Registro da Aplicação no Projeto

Para que o Django reconheça a nova aplicação, ela deve ser registrada no arquivo settings.py do projeto, dentro da lista INSTALLED_APPS. Na lista:
```python
INSTALLED_APPS[
...
'nome_seu_app',
...
]
```
### Definição dos Modelos
1. **Modelos no Django**

Os modelos em Django são usados para definir a estrutura das tabelas no banco de dados. Cada modelo é uma classe Python que define os campos e comportamentos da tabela.
É necessário criar classes que serão utilizadas como tabelas no arquivo models.py dento da pasta do seu APP. Exemplo de classes:
```python
class Player(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    cossyId = models.CharField(max_length= 12)
    victories = models.IntegerField(default=0)
    defeates = models.IntegerField(default = 0)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Nome Real: {self.name}; Apelido: {self.nickname}; Cossy: {self.cossyId}"
```

2.  **Criação dos Modelos**

Após definir os modelos, é necessário criar e aplicar as migrations, que são instruções de como o banco de dados deve ser modificado.

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Esses comandos vão gerar e aplicar as tabelas no banco de dados, de acordo com os modelos que você criou.

3. **Registro dos Modelos no Admin**

Para gerenciar as tabelas através da interface administrativa do Django, os modelos precisam ser registrados no arquivo admin.py dentro da pagina da aplicação. Exemplo:
```python
from  models  import  Player
admin.site.register(Player)
```

Agora, quando você acessar o painel administrativo do Django (em http://127.0.0.1:8000/admin/), é possível visualiza
## Configuração do Projeto Django
1. **Instalação do Django**

O primeiro passo é iniciar uma VirtualEnv e instalar o Django no ambiente de desenvolvimento. Isso pode ser feito usando o comando pip:

Para instalar a VirtualEnv:
```bash
#Para criar uma virtualEnv utilize o comando:
python3 -m venv nome_da_env
#para acessar uma venv ja criada ou a que vc acabou de criar:
source nome_da_env/bin/activate
```
Para instalar django dentro da virtualEnv:
```bash
pip install django
#ou
sudo apt install python3-django
```
2. **Criação do Projeto Django**

Após instalar o Django, o próximo passo é criar um novo projeto. Um projeto no Django é um contêiner que abrigará todas as configurações e as aplicações específicas.

```bash
django-admin startproject nome_do_projeto
```
3. **Execução do Servidor de Desenvolvimento**

Uma vez criado o projeto, você pode iniciar o servidor de desenvolvimento local para verificar se tudo está funcionando corretamente.

```bash
python3 manage.py runserver
```
Acesse o servidor no navegador através do endereço http://127.0.0.1:8000/.

4. **Criação de uma Aplicação**

No Django, uma aplicação é uma parte independente do projeto, com funcionalidades específicas. Para criar uma aplicação dentro do projeto, use o comando:

```bash
python3 manage.py startapp nome_da_aplicacao
```
## Registro da Aplicação no Projeto

Para que o Django reconheça a nova aplicação, ela deve ser registrada no arquivo settings.py do projeto, dentro da lista INSTALLED_APPS. Na lista:
```python
INSTALLED_APPS[
...
'nome_seu_app',
...
]
```
### Definição dos Modelos
1. **Modelos no Django**

Os modelos em Django são usados para definir a estrutura das tabelas no banco de dados. Cada modelo é uma classe Python que define os campos e comportamentos da tabela.
É necessário criar classes que serão utilizadas como tabelas no arquivo models.py dento da pasta do seu APP. Exemplo de classes:
```python
class Player(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    cossyId = models.CharField(max_length= 12)
    victories = models.IntegerField(default=0)
    defeates = models.IntegerField(default = 0)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Nome Real: {self.name}; Apelido: {self.nickname}; Cossy: {self.cossyId}"
```

2.  **Criação dos Modelos**

Após definir os modelos, é necessário criar e aplicar as migrations, que são instruções de como o banco de dados deve ser modificado.

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Esses comandos vão gerar e aplicar as tabelas no banco de dados, de acordo com os modelos que você criou.

3. **Registro dos Modelos no Admin**

Para gerenciar as tabelas através da interface administrativa do Django, os modelos precisam ser registrados no arquivo admin.py dentro da pagina da aplicação. Exemplo:
```python
from  models  import  Player
admin.site.register(Player)
```

Agora, quando você acessar o painel administrativo do Django (em http://127.0.0.1:8000/admin/), é possível visualizar as tabelas criadas.

4. **Criando e deletando um usuário admnistrador**

Para criar um super user é necessário utilizar o comando abaixo
```shell
python manage.py createsuperuser
```
Para deletar um super user é mais complicado, é necessário entrar na shell do seu app django, Nessa shell é possível realizar comandos python no ambiente python do seu projeto, por exemplo utilizar os comandos de adicionar usuarios em uma tabela, ver os uusarios cadastrados, etc.

Para entrar na shell de django utilziamos o comando:
```shell
python manage.py shell
#Para deletar o super user é só utilizar os comandos:
from django.contrib.auth.models import User

# Substitua 'nome_do_superusuario' pelo nome do usuário que deseja deletar
usuario = User.objects.get(username='nome_do_superusuario')
usuario.delete()
```
## Configuração do Projeto Django
1. **Instalação do Django**

O primeiro passo é instalar o Django no ambiente de desenvolvimento. Isso pode ser feito usando o comando pip:

```bash
pip install django
#ou
sudo apt install python3-django
```
2. **Criação do Projeto Django**

Após instalar o Django, o próximo passo é criar um novo projeto. Um projeto no Django é um contêiner que abrigará todas as configurações e as aplicações específicas.

```bash
django-admin startproject nome_do_projeto
```
3. **Execução do Servidor de Desenvolvimento**

Uma vez criado o projeto, você pode iniciar o servidor de desenvolvimento local para verificar se tudo está funcionando corretamente.

```bash
python3 manage.py runserver
```
Acesse o servidor no navegador através do endereço http://127.0.0.1:8000/.

4. **Criação de uma Aplicação**

No Django, uma aplicação é uma parte independente do projeto, com funcionalidades específicas. Para criar uma aplicação dentro do projeto, use o comando:

```bash
python3 manage.py startapp nome_da_aplicacao
```
## Registro da Aplicação no Projeto

Para que o Django reconheça a nova aplicação, ela deve ser registrada no arquivo settings.py do projeto, dentro da lista INSTALLED_APPS. Na lista:
```python
INSTALLED_APPS[
...
'nome_seu_app',
...
]
```
### Definição dos Modelos
1. **Modelos no Django**

Os modelos em Django são usados para definir a estrutura das tabelas no banco de dados. Cada modelo é uma classe Python que define os campos e comportamentos da tabela.
É necessário criar classes que serão utilizadas como tabelas no arquivo models.py dento da pasta do seu APP. Exemplo de classes:
```python
class Player(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    cossyId = models.CharField(max_length= 12)
    victories = models.IntegerField(default=0)
    defeates = models.IntegerField(default = 0)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Nome Real: {self.name}; Apelido: {self.nickname}; Cossy: {self.cossyId}"
```

2.  **Criação dos Modelos**

Após definir os modelos, é necessário criar e aplicar as migrations, que são instruções de como o banco de dados deve ser modificado.

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Esses comandos vão gerar e aplicar as tabelas no banco de dados, de acordo com os modelos que você criou.

3. **Registro dos Modelos no Admin**

Para gerenciar as tabelas através da interface administrativa do Django, os modelos precisam ser registrados no arquivo admin.py dentro da pagina da aplicação. Exemplo:
```python
from  models  import  Player
admin.site.register(Player)
```

Agora, quando você acessar o painel administrativo do Django (em http://127.0.0.1:8000/admin/), é possível visualizar as tabelas criadas.

4. Checar se migrations ocorreram bem
Para checar se as migrations aconteceram de formae fetiva, é possível utilizar o comando

```shell
python3 manage.py showmigrations
```

Esse comando mostra quais migration aconteceram e aconteceram com sucesso. 
- [X] - indica que a migration foi aplicada com sucesso.
- [ ] -  indica que a migration nao aconteceu com sucesso ou ainda não foi realizada. 


## Comandos para manipulação de banco de dados:

1. Comandos de inserção:

Podemos instanciar um objeto e inseri-lo no banco de dados:
```python
from .models import Produto

novo_produto = Produto(nome="Carta Azul", preco=20.00)
novo_produto.save()
```

Para inserir diretamente no BD se instanciar um objeto é possível fazer assim:
```python
Produto.objects.create(nome="Carta Vermelha", preco=15.00)
```

2. Comandos de atualização

Para atualizar o regist no BD é necessárioprmeiro encontrar o registro então é necessário filtrar para encontrar o objeto desejado, aterar o objeto e em seguida altera-lo:
```python
produto = Produto.objects.get(id=1)
produto.preco = 25.00
produto.save()
```
Também é possível fazer uma atualização ao emsmo tempo que a filtragem pelo registro é feita:

```python
Produto.objects.filter(nome="Carta Vermelha").update(preco=18.00)
```

3. Comandos de exclusão

É possível deletar um regist em específico utilizando o comando:
```python
produto = Produto.objects.get(id=2)
produto.delete()
```
Também é possível deletar em lote utilizando filtros:
```python
Produto.objects.filter(preco__lt=10.00).delete()
```

## Comandos de Visualição de dados

1. Todos registr de uma tabela:

Para retornar todos os registros de uma tabela:
```python
from .models import Produto

# Retorna todos os registros de Produto
todos_produtos = Produto.objects.all()
print(todos_produtos)
```

2. Contar registr em uma Tabela

Para contar o númer de registos dent de uma tabela podemos utiliza o comando Count():
```python
total_produtos = Produto.objects.count()
print(f"Total de produtos: {total_produtos}")
```

3. Para listar os campos de um modelo, ou seja quais são as colunas de uma tabela:

```python
for field in Produto._meta.fields:
    print(field.name, field.get_internal_type())
```

4. Mostrar todos os regists mas selecionar quais colunas ver

Comando para ver todos os registros de um determinada tabela, mas visualizar apenas determinadas colunas:

```python
# Retorna uma lista de dicionários com apenas os campos 'nome' e 'preco'
produtos_resumidos = Produto.objects.values('nome', 'preco')
print(produtos_resumidos)
```

5. Ordenar registos:

Para ordenar registros sem modificar a tabela original, a ordenação é feita baseada em uma determinada coluna:
```python
# Lista todos os produtos ordenados pelo campo 'preco' em ordem crescente
produtos_ordenados = Produto.objects.all().order_by('preco')
```
Para ordenar de forma decrescente é necessário colocar um "-" no nome da coluna que vai ser a causa da ordenação:

```python
# Ordena em ordem decrescente
produtos_ordenados_desc = Produto.objects.all().order_by('-preco')
```

6. Filtrar registros:

Para filtrar os registos que serão utilizados que serão mostrados na tela, é necessário utilizar filter:

```python
# Lista todos os produtos com preço acima de 50
produtos_caros = Produto.objects.filter(preco__gt=50)
print(produtos_caros)
```

