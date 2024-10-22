# Sistema de Gestão de Livraria Online

## Descrição

Este projeto é um sistema de gestão de livraria online desenvolvido em Python utilizando o framework FastAPI. O objetivo do sistema é permitir a gestão de livros, autores e categorias e implementar um sistema de recomendação de livros baseado em gêneros.

## Funcionalidades

- CRUD completo para livros, autores e categorias.
- Sistema de recomendação de livros com base em categorias.

## Pré-requisitos

- Python 3.7 ou superior
- Dependências listadas em `requirements.txt`

## Como Executar

1. **Criar e ativar o ambiente virtual:**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate

2. **Instalar as dependências:**
    ```venv
    pip install -r requirements.txt
    ```

3. **Executar a aplicação:**
    ```venv
    uvicorn app.main:app --reload
    ```

4. **Acessar a API:**

**Abra seu navegador e vá para http://127.0.0.1:8000/docs para visualizar a documentação automática da API.**

**Como Usar:**
Adicionar Autores:
    Endpoint: POST /authors/
    Payload: {"name": "Nome do Autor"}

Listar Autores:
    Endpoint: GET /authors/

Adicionar Categorias:
    Endpoint: POST /categories/
    Payload: {"name": "Nome da Categoria"}

Listar Categorias:
    Endpoint: GET /categories/

Adicionar Livros:
    Endpoint: POST /books/
    Payload: {"title": "Título do Livro", "author_id": 1, "category_id": 1}

Listar Livros:
    Endpoint: GET /books/