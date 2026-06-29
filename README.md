# API Inventario v1

Mini-proyecto hecho como práctica del SENA (Cuarto Trimestre) para aprender a construir una API REST con **FastAPI**, **SQLAlchemy** y **SQLite**.

La API permite administrar un inventario básico de productos: crear, listar, consultar por ID, actualizar y eliminar, con validación de datos usando Pydantic.

## ¿Qué aprendí / herramientas usadas en este proyecto?

- **Python 3** como lenguaje base
- **FastAPI** para construir la API y generar la documentación automática (`/docs`)
- **Uvicorn** como servidor para correr la aplicación
- **SQLAlchemy** como ORM para conectar la API con la base de datos
- **SQLite** como base de datos (archivo `inventario.db`, se crea automáticamente)
- **Pydantic** para validar los datos que entran a la API
- **VS Code** como editor, usando entornos virtuales (`venv`) para aislar las dependencias
- **Git y GitHub** para subir y versionar el proyecto

## Estructura del proyecto

El proyecto está organizado por capas, para separar responsabilidades:

```
inventario_api/
│
├── app/
│   ├── main.py                      # Punto de entrada de la app
│   │
│   ├── database/
│   │   └── connection.py            # Configuración de SQLAlchemy y SQLite
│   │
│   ├── models/
│   │   └── product.py               # Modelo SQLAlchemy (tabla products)
│   │
│   ├── schemas/
│   │   └── product.py               # Esquemas Pydantic (validaciones)
│   │
│   ├── repositories/
│   │   └── product_repository.py    # Acceso a datos (queries SQLAlchemy)
│   │
│   ├── services/
│   │   └── product_service.py       # Lógica de negocio y manejo de errores
│   │
│   └── routes/
│       └── product_routes.py        # Endpoints de la API

```

## Cómo correr el proyecto en local

1. Crear y activar el entorno virtual:
\```bash
python -m venv venv
source venv/Scripts/activate
\```

2. Instalar dependencias:
\```bash
pip install -r requirements.txt
\```

3. Ejecutar el servidor:
\```bash
uvicorn app.main:app --reload
\```

4. Abrir la documentación interactiva:
\```
http://127.0.0.1:8000/docs
\```

| Método | Endpoint | Descripción |
|---|---|---|
| GET | /products/ | Listar todos los productos |
| POST | /products/ | Crear un producto |
| GET | /products/{id} | Consultar un producto por ID |
| PUT | /products/{id} | Actualizar un producto |
| DELETE | /products/{id} | Eliminar un producto |

## 👤 Autor

- **Nombre:** Julián Esneyde Machado Garzón
- **Ficha:** 3228973B
- **GitHub:** [@JulianMg20](https://github.com/JulianMg20)
- **Proyecto:** SENA - Análisis y Desarrollo de Software
- **Trimestre:** 4


