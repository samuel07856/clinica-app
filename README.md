# Sistema de Marcação de Consultas - Clínica

Este projeto é uma aplicação web desenvolvida com **Flask** que permite o cadastro de usuários, login, e marcação de consultas em uma clínica.

## 🚀 Tecnologias Utilizadas

- Python 3.13
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Bcrypt
- Flask-Login
- SQLite

## 📁 Estrutura de Pastas

```
clinica/
├── __init__.py
├── models.py
├── routes.py
├── forms.py
├── seed.py
├── static/
│   ├── css/
│   │   └── estilos.css
│   └── img/
│       └── logo.png
├── templates/
│   ├── homepage.html
│   ├── criarconta.html
│   ├── perfil.html
│   └── resultado_busca.html
instance/
└── comunidade.db
main.py
criar_banco.py
requirements.txt
README.md
```

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Crie o banco de dados

```bash
python criar_banco.py
```

### 5. Execute a aplicação

```bash
python main.py
```

A aplicação ficará disponível em: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Usuários de Teste

Você pode usar o script `seed.py` para popular o banco com dados de teste (opcional):

```bash
python seed.py
```

---

## 📌 Observações

- O campo CPF é único. Cadastros duplicados não são permitidos.
- Os dados são salvos localmente em um banco SQLite (`instance/comunidade.db`).
- O projeto ainda não está preparado para deploy na web (como no Heroku ou GitHub Pages).
