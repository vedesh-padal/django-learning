# Chai Lovers

Welcome to the **Chai Lovers** project! This is a Django web application designed to showcase various chai varieties, their details, reviews, and availability at different stores. The application aims to provide chai enthusiasts with a platform to explore and enjoy the rich flavors of chai.

## Table of Contents

- [Chai Lovers](#chai-lovers)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Installation](#installation)
    - [Usage](#usage)

## Features

- **Chai Varieties**: Browse through a list of various chai types with detailed descriptions.
- **Chai Details**: View detailed information about each chai variety, including images, prices, and availability.
- **Reviews**: Users can read and submit reviews for different chai varieties.
- **Responsive Design**: The application is fully responsive and works on both desktop and mobile devices.
- **User-Friendly Interface**: Intuitive navigation and appealing design using Tailwind CSS.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Tailwind CSS**: A utility-first CSS framework for creating custom designs without leaving your HTML. (using django-tailwind python package, and node should be installed for tailwind to work)
- **SQLite**: The default database used for development purposes (can be changed to PostgreSQL or others in production).
- **HTML/CSS/JavaScript**: Standard web technologies for building the frontend.

## Installation

To set up the Chai Lovers project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/<USERNAME>/django-learning.git
   cd django-learning
   ```

2. **Create a Virtual Environment**:
   
   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv .venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   
   Make sure you have pip installed, then run:
   ```bash
   git clone https://github.com/<USERNAME>/django-learning.git
   cd django-learning
   ```

4. **Run Migrations**:
   
   Set up the database by running migrations:
   ```bash
   python manage.py migrate
   ```
5. **Create a Superuser (Optional)**:
   
   To access the Django admin interface, create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
   
   Start the development server:
  
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**:
   
   Open your web browser and go to http://127.0.0.1:8000/ to view the application.

    #### Else, if you want to run it on another port, run:

    ```bash
    python manage.py runserver -<PORT_NO>
    ```

### Usage

Navigate to the home page `/`, and `/chai` to view all available chai varieties.
Click on any Chai variety to see its details, including price, description, reviews, and availability at different stores.
Use the admin interface (accessible at `/admin`) to manage chai varieties, reviews, and stores.
