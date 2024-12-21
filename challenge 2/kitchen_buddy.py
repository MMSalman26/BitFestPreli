import os
import sqlite3
from flask import Flask, request, jsonify
import google.generativeai as genai

genai.configure(api_key="AIzaSyCD7u6DD6-pZ6pqfxSlA-sT6N9akpClBFY")
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Flask app
app = Flask(__name__)

# Database Setup
DATABASE = 'kitchen_buddy.db'


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Create ingredients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity TEXT NOT NULL
        )
    ''')
    # Create recipes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            details TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Initialize Database
init_db()

# Ingredient Management API
@app.route('/ingredients', methods=['POST', 'GET'])
def ingredients():
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        quantity = data.get('quantity')
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
        conn.commit()
        conn.close()
        return jsonify({"message": "Ingredient added successfully!"})
    elif request.method == 'GET':
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ingredients")
        ingredients = cursor.fetchall()
        conn.close()
        return jsonify({"ingredients": ingredients})


# Recipe Retrieval API
@app.route('/recipes', methods=['POST', 'GET'])
def recipes():
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        details = data.get('details')
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO recipes (name, details) VALUES (?, ?)", (name, details))
        conn.commit()
        conn.close()
        return jsonify({"message": "Recipe added successfully!"})
    elif request.method == 'GET':
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM recipes")
        recipes = cursor.fetchall()
        conn.close()
        return jsonify({"recipes": recipes})


# Recipe Parsing and Storage
def parse_recipes(file_path):
    with open(file_path, 'r') as file:
        recipes = file.readlines()
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        for recipe in recipes:
            name, details = recipe.split(':', 1)
            cursor.execute("INSERT INTO recipes (name, details) VALUES (?, ?)", (name.strip(), details.strip()))
        conn.commit()
        conn.close()


# Chatbot Integration
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('input')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity FROM ingredients")
    ingredients = cursor.fetchall()
    ingredient_list = ', '.join([f"{name} ({quantity})" for name, quantity in ingredients])
    prompt = f"You are a helpful cooking assistant. Suggest a recipe using these ingredients: {ingredient_list}. User asks: {user_input}"
    try:
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)})





# Start Flask app
if __name__ == '__main__':
    app.run(debug=True)
