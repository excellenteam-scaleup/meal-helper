
from flask import Flask, request, abort, jsonify
import random

# Instantiate a new Web app
app = Flask(__name__)

# In reality this would be in a file
jokes = [
    "What do you call a magic dog? A labracadabrador.",
    "Why did the hipster burn his mouth? He drank it before it was cool.",
]

@app.route('/random')
def random_joke():
    return random.choice(jokes)

@app.route('/save', methods=['POST'])
def save_joke():
    jokes.append(request.data.decode())
    return "OK"

@app.route('/joke/<int:id_>')
def get_joke(id_: int):
    if 0 <= id_ < len(jokes):
        return jsonify(joke=jokes[id_])
    abort(404)

@app.route('/joke/<int:id_>', methods=['DELETE'])
def delete_joke(id_: int):
    if 0 <= id_ < len(jokes):
        return jsonify(joke=jokes.pop(id_))
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
