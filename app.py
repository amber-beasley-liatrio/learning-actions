from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Bye World'

@app.route('/health')
def health():
    return 'OK', 200

@app.route('/execute')
def execute():
    # Critically finding: using eval() with unsanitized user input
    command = request.args.get('cmd')
    result = eval(command)  # Never use eval() with untrusted input
    return str(result)

if __name__ == '__main__':
    # should be a high finding
    app.run(debug=True)
