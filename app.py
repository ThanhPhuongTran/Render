from flask import Flask, render_template
import socket

app = Flask(__name__, template_folder='template')

def get_static_ip():
    hostname = socket.gethostname()
    static_ip = socket.gethostbyname(hostname)
    return static_ip

def save_static_ip(ip_address):
    with open('static_ip.txt', 'w') as file:
        file.write(ip_address)

static_ip = get_static_ip()
save_static_ip(static_ip)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', static_ip=static_ip)

if __name__ == '__main__':
    app.run(debug=True)
