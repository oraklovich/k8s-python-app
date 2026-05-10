from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    version = os.environ.get('APP_VERSION', 'v1.0.0')
    return f"<h3>Hello from Kubernetes!</h3>"            f"<b>Pod:</b> {hostname}<br>"            f"<b>Version:</b> {version}<br>"            f"<b>Cluster:</b> MacBook Air K3s"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
