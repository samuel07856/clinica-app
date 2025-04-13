from clinica import app

if __name__ == "__main__":
    app.run(debug=True)
    # Bibliotecas obrigatórias para o projeto Flask funcionar:

# Flask - Framework web principal
# Flask-SQLAlchemy - ORM para banco de dados relacional (ex: SQLite, PostgreSQL)
# Flask-WTF - Integração do Flask com formulários WTForms
# WTForms - Criação e validação de formulários HTML
# Flask-Bcrypt - Hashing seguro de senhas
# Flask-Login - Gerenciamento de autenticação e sessão de usuários
# email_validator - Validação de e-mails (usado junto com WTForms)

# Instale com:
# pip install Flask Flask-SQLAlchemy Flask-WTF WTForms Flask-Bcrypt Flask-Login email_validator
