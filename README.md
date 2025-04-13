
# Clínica Web App

Este é um sistema web desenvolvido com Flask para gerenciamento de uma clínica. O sistema permite a criação de contas, autenticação de usuários, gerenciamento de perfis e busca de informações.

---

## 📁 Estrutura do Projeto

```
clinica/
│
├── static/                # Arquivos estáticos (CSS, imagens, etc.)
│   ├── css/estilos.css
│   └── img/logo.png
│
├── templates/             # Templates HTML
│   ├── criarconta.html
│   ├── homepage.html
│   ├── perfil.html
│   └── resultado_busca.html
│
├── __init__.py            # Inicialização do app Flask
├── forms.py               # Formulários com Flask-WTF
├── models.py              # Modelos do banco de dados
├── routes.py              # Rotas da aplicação
├── seed.py                # Inserção de dados iniciais
│
├── criar_banco.py         # Script para criação do banco de dados
├── main.py                # Arquivo principal de execução
├── requirements.txt       # Dependências da aplicação
├── Procfile               # Arquivo para deploy (ex: no Heroku)
└── README.md              # Documentação do projeto
```

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Crie o banco de dados

```bash
python criar_banco.py
```

### 5. (Opcional) Popule com dados de exemplo

```bash
python seed.py
```

### 6. Execute a aplicação

```bash
python main.py
```

Acesse: http://localhost:5000

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Flask** – Framework principal da aplicação
- **Flask-SQLAlchemy** – ORM para manipulação do banco de dados
- **SQLAlchemy** – ORM poderoso e flexível
- **Flask-WTF** – Formulários web integrados com CSRF protection
- **WTForms** – Criação de formulários
- **Flask-Bcrypt** – Hash e verificação de senhas
- **Flask-Login** – Autenticação e gerenciamento de sessões
- **email-validator** – Validação de e-mails nos formulários
- **Jinja2** – Template engine do Flask

---

## ✅ Requisitos

- Python 3.10 ou superior
- Pip (gerenciador de pacotes Python)

---

## 📌 Observações

- O projeto pode ser hospedado no GitHub Pages **somente como repositório de código**, pois é um app Flask (backend), e o GitHub Pages é voltado para **aplicações estáticas**. Para rodar online, considere usar serviços como Heroku, Render, Vercel (com backend), ou VPSs.
