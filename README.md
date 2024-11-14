# ygo-tournment-api

Projeto de um sistema de ranking para torneios de Yu-Gi-Oh! para por em prática conhecimentos de Django e acesso a banco de dados.

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

````bash

```bash
pip install django
#ou
sudo apt install python3-django
````

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

Agora, quando você acessar o painel administrativo do Django (em http://127.0.0.1:8000/admin/), é possível visualizar

Também é possível cadastrar modelos personalizados para apareer apenas oa campos necessários no paineld e admnistrador. No arquivo admin.py crie uma classe antes de registrar no BD:

```python
from django.contrib import admin
from .models import Produto

class PlayerAdmin(admin.ModelAdmin):
    #list display determina quais campos ser'ao exibidos na lista
    list_display = ('name','nickname','email','cossyId', 'contact_number')
    #search_fields mostra quais campos da tabela sao pesquisaveis
    seach_fields= ('name','nickname', "cossyId",'contact_number')

# Register your models here.
admin.site.register(Player, PlayerAdmin)

```

4. **Checar se migrations ocorreram bem**
   Para checar se as migrations aconteceram de forma efetiva, é possível utilizar o comando

```shell
python3 manage.py showmigrations
```

Esse comando mostra quais migration aconteceram e aconteceram com sucesso.

- [x] - indica que a migration foi aplicada com sucesso.
- [ ] - indica que a migration nao aconteceu com sucesso ou ainda não foi realizada.

5. **Criando e deletando um usuário admnistrador**

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

## Criação de forms utilziando Django Forms

No diretório do seu APP é necessário criar um arquivo chamado forms.py e nele exportar todos os models que você deseja criar um formulario para seu preenchimento.

```python
from django import forms
from .models import Player, Tournament  # Substitua com o modelo correspondente

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'nickname', 'email', 'cossyId', 'contact_number']  # Defina os campos que deseja no formulário

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'date', 'modality']  # Defina os campos que deseja no formulário
```

Em seguida é possivel exibir esse formulário em uma ágina e salvar os dados submetidos, é possivel criar uma view para isso:

```python
from django.shortcuts import render, redirect
from .forms import PlayerForm

def criar_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo produto no banco de dados
            return redirect('lista_players')
    else:
        form = PlayerForm()
    return render(request, 'torneios/criar_player.html', {'form': form})
# Create your views here.
```

Agora seria necessário criar uma página simples html para ser chamada e utilizar esses forms, primeiramente dentor do app que será utilizado, crie um diretorio com o nome templates e dentro desse diretodrio o nome do app que será utilizado ou seja: ygo_rankin/torneios/templates/torneios

E la é possivel criar seu formulario simples em html:

```html
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="UTF-8" />
    <title>Criar Player</title>
  </head>
  <body>
    <h1>Criar Novo Player</h1>
    <form method="post">
      {% csrf_token %} {{ form.as_p }}
      <button type="submit">Salvar</button>
    </form>
  </body>
</html>
```

Agora no seu projeto django (nesse caso dentro de ygo_ranking/ygo_ranking existe um arquivo chamado urls.py, la vc pode chamar seus formularios, assim note que para importar a view vc utiliza o nome do seu APP (no caso o nome do meu app criado foi "torneios"):

```python
from django.contrib import admin
from django.urls import path
from torneios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('criar_player/', views.criar_player, name='criar_player'),
]
```

Após todas essas etapas, é possível testar seu formulario rodando o server, e acessando a url do seu server/url cadastrada, nesse caso: http://127.0.0.1:8000/criar_player/

## Sistema de autenticação de usuário

Primeiramente é necessário cirar as URL para autenticação no django no arquivo url.py:

As view de LoginView e LogoutView são padrão do django para autenticação:

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
]
```

É possível criar uma view de registroo de usuário basica pelo proprio django. no arquivo view.py podemos adicionar:

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o registro
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

```

Seguindo a ideia anteriro, é necessário criar uma pasta dentor do diretório template com o nome "registration" e criar os HTML para pagina de Login e de registro. Assim:

registration/login.html

```html
<h2>Login</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Entrar</button>
</form>
```

registration/registro.html

```html
<h2>Login</h2>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Entrar</button>
</form>
```

É possível escolher o redirecionamento após a página de login e a pós a página de logout, é preciso acessar o arquivo de setting.py no seu projeto e adicionar as seguintes variáveis:

```python
# Redireciona para essa página após o login bem-sucedido
LOGIN_REDIRECT_URL = 'criar_player'

# Redireciona para essa página após o logout
LOGOUT_REDIRECT_URL = 'login'
```

Por fim, também é possível selecionar páginas que requerem que o usuario esteja logado/autenticado para acessar dessa forma:

No arquivo _view.py_ é possível colcoar a tag @login_required pra determinar que determinada view so pode ser acessada se o usuario estiver autenticado:

```python
from django.contrib.auth.decorators import login_required

@login_required
def minha_view_protegida(request):
    # Código da view
    return render(request, 'pagina_protegida.html')
```

PROXIMOS PASSOS:

1. lOGOUT
2. LOGOUT REQUIRED
3. CRIAR UMA INTERFACE BONITA PARA TESTES
