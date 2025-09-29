# 📚 Sistema de Monografias - UFVJM

Aplicação web desenvolvida em **Django** para gerenciamento de monografias da UFVJM.  
O sistema contempla **Alunos, Professores, Administradores** e **Bancas Avaliadoras**.

🚀 Tecnologias Utilizadas:
- **Linguagem**<br>
Python 3.x

- **Framework**<br>
Django 5.x

- **Banco de Dados**<br>
PostgreSQL

- **Front-end**<br>
HTML5<br>
CSS3<br>
Bootstrap 5<br>
Font Awesome<br>

- **Controle de versão** <br>
Git & GitHub

---

## 🚀 Como rodar o projeto localmente

### 🔹 1. Clone o repositório
### 🔹 2. Crie o ambiente virtual
LINUX: <br>
python3 -m venv venv <br>
source venv/bin/activate

WINDOWS: <br>
python -m venv venv <br>
venv\Scripts\activate


### 🔹 3. Instale as dependências
pip install -r requirements.txt


### 🔹 4. Configure o banco de dados (PostgreSQL)
No arquivo settings.py, ajuste as credenciais do PostgreSQL:<br>
DATABASES = {<br>
    'default': {<br>
        'ENGINE': 'django.db.backends.postgresql',<br>
        'NAME': 'monografias_db',<br>
        'USER': 'seu_usuário',<br>
        'PASSWORD': 'sua_senha',<br>
        'HOST': 'localhost',<br>
        'PORT': '5432',<br>
    }<br>
}<br>
⚠️ Lembre-se de criar o banco antes:<br>
createdb monografias_db

### 🔹 5. Rode as migrações
python manage.py migrate


### 🔹 6. Crie um superusuário (Administrador)
python manage.py createsuperuser


### 🔹 7. Inicie o servidor
python manage.py runserver

### 🔹 8. Acesse pelo navegador
http://127.0.0.1:8000

## 🧑‍💻 Funcionamento do sistema
- 👨‍🎓 Alunos
  - Criados automaticamente no cadastro do site. <br>
  - Cada aluno tem sua matrícula registrada no perfil.<br>
  - Podem ser vinculados como autores de uma monografia.<br>
  - Conseguem acompanhar as defesas.

- 👨‍🏫 Professores
  - Criados apenas por Administradores.
  - Podem ser designados como Orientadores ou Coorientadores nas monografias.
  - Professores podem criar monografias e editar apenas quando eles mesmos forem orientadores.
  - Professores orientadores e coorientadores podem editar/atribuir nota em bancas que estiverem participando

- 🛠️ Administrador (Superuser)
  - Criado via createsuperuser.
  - Possui acesso total ao sistema.
  - Pode cadastrar professores, criar/editar monografias e agendar bancas.

- 📑 Monografias
  - Contêm título, autor, orientador, coorientador, resumo, abstract, palavras-chave e arquivo PDF.
  - Apenas administradores e professores podem criar ou excluir.

- 📝 Bancas
  - Contêm monografia vinculada, professores avaliadores, data, horário e local.
  - Status: Agendada, Cancelada ou Realizada.
  - Atribuição de nota (0 a 100).
