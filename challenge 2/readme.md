---

# Kitchen Buddy API Documentation

This API is designed to manage ingredients and recipes and includes a chatbot integration for recipe suggestions based on available ingredients. The backend uses SQLite for database management and is powered by Flask and Google Generative AI for the chatbot functionality.

---

## Table of Contents
1. [Setup](#setup)
2. [API Endpoints](#api-endpoints)
   - [Ingredient Management](#ingredient-management)
   - [Recipe Management](#recipe-management)
   - [Chatbot](#chatbot)
3. [Database Schema](#database-schema)

---

## Setup

1. Clone the repository and navigate to the project folder.
2. Install the required dependencies:
   ```bash
   pip install flask google-generativeai python-dotenv
   ```
3. Run the application:
   ```bash
   python app.py
   ```

---

## API Endpoints

### 1. Ingredient Management

#### **`GET /ingredients`**
- **Description**: Retrieves all ingredients from the database.
- **Response**:
    ```json
    {
        "ingredients": [
            {
                "id": 1,
                "name": "Tomato",
                "quantity": "2"
            },
            {
                "id": 2,
                "name": "Onion",
                "quantity": "1"
            }
        ]
    }
    ```

#### **`POST /ingredients`**
- **Description**: Adds a new ingredient to the database.
- **Request Body**:
    ```json
    {
        "name": "Tomato",
        "quantity": "2"
    }
    ```
- **Response**:
    ```json
    {
        "message": "Ingredient added successfully!"
    }
    ```

---

### 2. Recipe Management

#### **`GET /recipes`**
- **Description**: Retrieves all recipes from the database.
- **Response**:
    ```json
    {
        "recipes": [
            {
                "id": 1,
                "name": "Tomato Soup",
                "details": "Use tomatoes, onions, and spices."
            },
            {
                "id": 2,
                "name": "Pancakes",
                "details": "Flour, eggs, milk, sugar. Mix and cook."
            }
        ]
    }
    ```

#### **`POST /recipes`**
- **Description**: Adds a new recipe to the database.
- **Request Body**:
    ```json
    {
        "name": "Tomato Soup",
        "details": "Use tomatoes, onions, and spices."
    }
    ```
- **Response**:
    ```json
    {
        "message": "Recipe added successfully!"
    }
    ```

---

### 3. Chatbot

#### **`POST /chatbot`**
- **Description**: Interacts with the user to suggest recipes based on available ingredients.
- **Request Body**:
    ```json
    {
        "input": "I want something sweet"
    }
    ```
- **Response**:
    ```json
    {
        "response": "You can make Pancakes with flour, eggs, milk, and sugar."
    }
    ```

---

## Database Schema

1. **`ingredients` Table**:
    - `id` (INTEGER, Primary Key)
    - `name` (TEXT, Not Null)
    - `quantity` (TEXT, Not Null)

2. **`recipes` Table**:
    - `id` (INTEGER, Primary Key)
    - `name` (TEXT, Not Null)
    - `details` (TEXT, Not Null)

---