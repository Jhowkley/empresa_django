# Empresa Django

Este é um projeto Django de exemplo.

## Como rodar o projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/empresa_django.git
    cd empresa_django
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações:
    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

## Acesso ao Django Admin

Acesse [http://localhost:8000/admin](http://localhost:8000/admin) com as seguintes credenciais de exemplo:

- **Usuário:** fabricio
- **Senha:** joaovitor0205

> Para criar um superusuário personalizado, execute:
> ```bash
> python manage.py createsuperuser
> ```

## Licença

Este projeto está sob a licença MIT.