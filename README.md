# Product Catalog API

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
    ```bash
    venv\scripts\activate
      
5. Install dependencies(using pip):
   ```bash
   pip install -r requirements.txt

6. Run migrations:
   ```bash
   python manage.py migrate

7. Start the development server:
   ```bash
   python manage.py runserver

8. Follow the provided link to work with the API using any API tool like postman

## Usage:

Provided in this URL is the link to the live documentation of the project:
<a href="https://product-catalog-api-ho3a.onrender.com/api/schema/swagger-ui/">Click here!</a>


## Technologies Used:
<ul>
 <li>Python 3: Backend Logic</li>
 <li>Django: Web framework for building API endpoints</li>
<li>Django REST framework: API creation and management</li>
<li>SQLite/PostgreSQL: Database for storing products and sales</li>
<li>Render: Deployment using gunicorn</li>
</ul>

## Contributing
 Feel free to open an issue or submit a pull request if you would like to contribute to this project.
