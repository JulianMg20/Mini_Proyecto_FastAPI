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
app/
├── main.py                      # Punto de entrada de la aplicación
├── database/
│   └── connection.py            # Configuración de SQLAlchemy y SQLite
├── models/
│   └── product.py               # Modelo de la tabla "products"
├── schemas/
│   └── product.py               # Esquemas de Pydantic (validaciones)
├── repositories/
│   └── product_repository.py    # Acceso a datos (consultas a la BD)
├── services/
│   └── product_service.py       # Lógica de negocio
└── routes/
    └── product_routes.py        # Endpoints de la API
```

## Cómo correr el proyecto en local

1. Crear y activar el entorno virtual:
\ ```bash
python -m venv venv
source venv/Scripts/activate
\```

2. Instalar dependencias:
\ ```bash
pip install -r requirements.txt
\```

3. Ejecutar el servidor:
\ ```bash
uvicorn app.main:app --reload
\```

4. Abrir la documentación interactiva:
\ ```
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

## CAPTURAS DE PANTALLA
<img width="1920" height="1140" alt="422" src="https://github.com/user-attachments/assets/0650fdc0-0623-40e4-8699-3325c57e5010" />
<img width="1920" height="1140" alt="GET_200" src="https://github.com/user-attachments/assets/057e34a9-98bd-4dab-90d5-693cb54c0fc6" />
<img width="1906" height="1136" alt="PUT" src="https://github.com/user-attachments/assets/91f9807a-370e-4719-9d2c-57717a62c44a" />
<img width="1920" height="1140" alt="DELETE" src="https://github.com/user-attachments/assets/ca9365fe-aee6-4005-8b86-be6548615201" />
<img width="1920" height="1140" alt="POST" src="https://github.com/user-attachments/assets/975604cd-9352-4d2e-bbdf-445a84f14a91" />
<img width="1920" height="1140" alt="POSTT" src="https://github.com/user-attachments/assets/c388c5af-ecb9-400e-bcd7-9f11524a4710" />
<img width="1171" height="712" alt="Terminal" src="https://github.com/user-attachments/assets/6695fe8d-a63e-4624-8d02-4ed07e02caa4" />




