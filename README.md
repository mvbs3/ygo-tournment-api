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

Agora, quando você acessar o painel administrativo do Django (em http://127.0.0.1:8000/admin/), é possível visualizar as tabelas criadas.
