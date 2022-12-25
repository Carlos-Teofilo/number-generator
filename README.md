# Gerador números

## Meu primeiro projeto do zero com o framework django
Um gerador de números aleatórios inteiros

#### Baixando o repositório
<pre>
<code> $ git clone https://github.com/Carlos-Teofilo/number-generator.git </code>
</pre>
<br>

#### Criando um ambiente virual e ativando
<pre>
<code> $ python -m venv venv</code>
<code> $ source venv/bin/activate</code>
</pre>
<br>

#### Instalando as dependência
<pre>
<code> $ pip install requirements.txt</code>
</pre>
<br>

### Inicializando o servidor
Dentro do diretório <code> number_generator/manage.py </code> digite o comando:

<pre>
<code> $ python manage.py runserver</code>
</pre>

A seguinte mensagem aparecerá no terminal:

<pre>
<code>
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
December 25, 2022 - 16:45:48
Django version 4.1.4, using settings 'number_generator.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
</code>
</pre>

Insira o endereço <code> http://127.0.0.1:8000 </code> no browser para acessar a aplicação