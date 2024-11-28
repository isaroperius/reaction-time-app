from flask import Flask, render_template, request, jsonify
import time
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_timer():
    # Simulate a delay before changing color
    delay = random.randint(2, 5)
    time.sleep(delay)
    return jsonify({'status': 'green'})

@app.route('/reaction', methods=['POST'])
def reaction_time():
    user_time = float(request.json['user_time'])
    reaction_time = time.time() - user_time
    return jsonify({'reaction_time': reaction_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
