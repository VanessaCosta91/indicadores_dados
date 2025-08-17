# Indicadores Dados - Projeto Flask

Este é meu primeiro projeto web com Flask, SQLAlchemy e HTML, feito para aprendizado e portfólio.

Ele permite:
- Cadastro de usuários
- Login e autenticação
- Cadastro de companhias
- Visualização de perfil do usuário e suas companhias

---

## Tecnologias usadas
- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [WTForms](https://wtforms.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/) (para o front-end)

---

## Como rodar localmente

1. Clone o repositório:
   ```
   git clone https://github.com/vanessa91/indicadores_dados.git
   cd indicadores_dados
    ```
   
2. Crie e ative um ambiente virtual:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```

3. Instale as dependências:
    ```
    pip install -r requirements.txt 
    ```

4. Rode a aplicação:
    ```
    python main.py
    ```

---

## Deploy no Render

1. Suba o código no GitHub com requirements.txt e Procfile.
2. Vá em Render, crie um New Web Service.
3. Conecte seu repositório GitHub.
4. No campo "Start Command", use:
     ```
    gunicorn main:app
     ```
5. Render vai instalar as dependências e rodar seu app.

---

## Autora
Projeto desenvolvido por **Vanessa Costa**.
- Primeiro projeto full stack com Flask + SQLAlchemy.
- Focado em aprendizado de back-end, front-end e banco de dados.

