# Onboard - Nicholas Ogata

This project is designed to be a onboard project for a dev internship at Taqtile. This project will developed with the use of different concepts and tecnologies that are used in the backend of real projects of the company. The main goal of this project is to develop a RESTful API that handles HTTP requests with the use of PostgreSQL database.

# Environment and tools

The following tools are essential for the project development:

- Language: Python 3.11.6

- Framework: FastAPI (Modern and high-performance web framework for building APIs with Python)

- Database: PostgreSQL

- Docker: Docker

- Code editor: VS Code

- Version control: Git

# Steps to run and debug

Here's how to set up the project locally, run and debug the backend:

1. Clone the repository

Clone the repository from Github to your machine

```bash
git clone https://github.com/indigotech/onboard-nicholas-ogata.git
cd onboard-nicholas-ogata
```

2. Install dependencies

Use Poetry to install project dependencies and create a virtual environment

```bash
poetry install
```

3. Activate virtual environment

```bash
source {path_to_venv}/bin/activate
```

4. Run the application

```bash
uvicorn main:app --reload
```

The application may be available at:
http://127.0.0.1:8000
