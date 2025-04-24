# Product Catalog API

[![Build Status](https://github.com/Bnabdulwasiu/product-catalog-api/actions/workflows/product_testing.yml/badge.svg)](https://github.com/Bnabdulwasiu/product-catalog-api/actions/workflows/product_testing.yml)
![Python Version](https://img.shields.io/badge/python-3.10-blue)

A product catalog API that allows for basic CRUD operations, and has a search functionality.

## Features

- **Product Creation, Update, Delete**: Allows users to create products, view product details, update and delete products.
- **Search Functionality**: Ability for a product from the products catalog

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bnabdulwasiu/product-catalog-api.git

2. Navigate into project directory:
   ```bash
   cd product-catalog-api

3. Create a virtual environment:
    ```bash
    cd py -m venv venv

4. Activate virtual environment:
  •On windows
    ```bash
    venv\scripts\activate
    
  •On Unix/Macos
    ```bash
    source venv/bin/activate
      
5. Install dependencies(using pip):
   ```bash
   pip install -r requirements.txt

6. Set up environment variables:
Create a .env file in the root directory with the following:
   ```bash
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   ALLOWED_HOSTS=127.0.0.1,localhost
 
7. Run migrations:
   ```bash
   python manage.py migrate

8. Start the development server:
   ```bash
   python manage.py runserver


### API Endpoints

| Method | Endpoint           | Description               |
|--------|--------------------|---------------------------|
| GET    | /api/products/     | List all products         |
| POST   | /api/products/     | Create a new product      |
| GET    | /api/products/<id>/| Retrieve product details  |
| PUT    | /api/products/<id>/| Update a product          |
| DELETE | /api/products/<id>/| Delete a product          |
| GET    | /api/products/?search=name | Search by name    |

### Running Tests
```bash
python manage.py test

## Live Demo:
Use tools like Postman or Swagger to explore the API. Live documentation is available at:
<a href="https://product-catalog-api-ho3a.onrender.com/api/schema/swagger-ui/">Click here!</a>


## Technologies Used:
<ul>
 <li>Python 3: Backend Logic</li>
 <li>Django: Web framework for building API endpoints</li>
<li>Django REST framework: API creation and management</li>
<li>SQLite/PostgreSQL: Database for storing products and sales</li>
<li>Render: Deployment using gunicorn</li>
<li>dotenv: To manage environment variables </li>
<li>GitHub Actions: CI/CD workflow setup</li
</ul>
