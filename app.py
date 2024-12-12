from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bye World'

@app.route('/health')
def health():
    return 'OK', 200

@app.route('/user')
def get_user():
    # Unsafe use of user input leading to SQL Injection vulnerability
    user_id = request.args.get('id')
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Vulnerable code
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
