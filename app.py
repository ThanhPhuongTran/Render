# from flask import Flask, render_template
# import socket

# app = Flask(__name__, template_folder='template')

# def get_static_ip():
#     hostname = socket.gethostname()
#     static_ip = socket.gethostbyname(hostname)
#     return static_ip

# def save_static_ip(ip_address):
#     with open('static_ip.txt', 'w') as file:
#         file.write(ip_address)

# static_ip = get_static_ip()
# save_static_ip(static_ip)

# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('index.html', static_ip=static_ip)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request
import subprocess
import random

app = Flask(__name__)
def commit_to_github():
    # Tạo một số ngẫu nhiên để thêm vào commit message
    random_number = random.randint(1, 1000)
    commit_message = f'Update IP addresses #{random_number}'
    # Thực hiện commit với commit message có chứa số ngẫu nhiên
    subprocess.run(['git', 'add', 'static_ip.txt'])
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push','-u','origin','main'])
def save_ip_to_file(ip_address):
    with open('static_ip.txt', 'a') as file:
        file.write(ip_address + '\n')

@app.route('/')
def index():
    ip_address = request.remote_addr
    save_ip_to_file(ip_address)
    print(ip_address)
    # commit_to_github()

    return 'IP đã được lưu vào tệp tin.'

if __name__ == '__main__':
    app.run(debug=True)
