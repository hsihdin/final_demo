from flask import Flask, jsonify
import subprocess

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


@app.route('/')
def hello_world():
    return 'Hello From Adiyodi ECS Container!'


@app.route('/main_route')
def main_route_data():
    output = subprocess.check_output(['netstat', '-rn']).decode('utf-8')
    return jsonify({'main_route_data': output})


@app.route('/host_route')
def host_route_data():
    output = subprocess.check_output(['netstat', '-rn']).decode('utf-8')
    host_route_data = [line for line in output.split('\n') if 'default' in line]
    return jsonify({'host_route_data': host_route_data})


@app.route('/ip_route')
def ip_route_data():
    output = subprocess.check_output(['netstat', '-rn']).decode('utf-8')
    ip_route_data = [line for line in output.split('\n') if '0.0.0.0' in line]
    return jsonify({'ip_route_data': ip_route_data})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
