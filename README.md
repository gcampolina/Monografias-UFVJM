# 📚 Sistema de Monografias - UFVJM

Aplicação web desenvolvida em **Django** para gerenciamento de monografias da UFVJM.  
O sistema contempla **Alunos, Professores, Administradores** e **Bancas Avaliadoras**.

🚀 Tecnologias Utilizadas:
- **Linguagem**<br>
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

- **Framework**<br>
![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)

- **Banco de Dados**<br>
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)

- **Front-end**<br>
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)<br>
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)<br>
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)<br>
![FontAwesome](https://img.shields.io/badge/Font%20Awesome-339AF0?logo=fontawesome&logoColor=white)<br>

- **Controle de versão** <br>
![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white) & ![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)

---

## 🚀 Como rodar o projeto localmente

### 🔹 1. Clone o repositório

Instale o Git se não tiver.<br>
- sudo apt update<br>
- sudo apt install git<br>
- git clone https://github.com/gcampolina/Monografias-UFVJM<br>

### 🔹 2. Crie o ambiente virtual
**LINUX:** <br>
- python3 -m venv venv <br>
- source venv/bin/activate

**WINDOWS:** <br>
- python -m venv venv <br>
- venv\Scripts\activate


### 🔹 3. Ative a Venv e instale as dependências
**LINUX:** <br>
- python3 -m venv venv <br>
- source venv/bin/activate <br>
- pip install -r requirements.txt

**WINDOWS:**<br>
- .venv\Scripts\activate<br>
- pip install -r requirements.txt

⚠️Lembre-se que o Postgree também precisa ser instalado no SO<br>
- sudo apt install postgresql postgresql-contrib <br>
*O PostgreSQL é um software externo, não é um pacote Python, então nunca vai aparecer no requirements.txt.*

### 🔹 4. Configure o banco de dados (PostgreSQL)
sudo -u postgres psql<br>
CREATE DATABASE monografias;<br>
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';<br>
GRANT ALL PRIVILEGES ON DATABASE monografias TO seu_usuario;<br>
\q

No arquivo settings.py, ajuste as credenciais do PostgreSQL:<br>
DATABASES = {<br>
    'default': {<br>
        'ENGINE': 'django.db.backends.postgresql',<br>
        'NAME': 'monografias',<br>
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
  - Agendadas pelo Administrador
