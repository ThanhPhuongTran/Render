from flask import Flask, render_template,request
import socket

app = Flask(__name__, template_folder='template')

def get_static_ip():
    
    visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    # return f'Visitor IP Address: {visitor_ip}'
                
    return visitor_ip

def save_static_ip(ip_address):
    with open('static_ip.txt', 'w') as file:
        file.write(ip_address)


@app.route('/')
@app.route('/home')
def home():
    ip_address=get_static_ip()
    print("ip la: "+str(ip_address))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask,request
# import subprocess
# import random
# import requests
# from werkzeug.middleware.proxy_fix import ProxyFix

# app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

# def commit_to_github():
#     # Tạo một số ngẫu nhiên để thêm vào commit message
#     random_number = random.randint(1, 1000)
#     commit_message = f'Update IP addresses #{random_number}'
#     # Thực hiện commit với commit message có chứa số ngẫu nhiên
#     subprocess.run(['git', 'add', 'static_ip.txt'])
#     subprocess.run(['git', 'commit', '-m', commit_message])
#     subprocess.run(['git', 'push','-u','origin','main'])
# def get_client_ip():
#     # Lấy địa chỉ IP của máy khách từ các trường header
#     visitor_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
#     # return f'Visitor IP Address: {visitor_ip}'
                
#     return visitor_ip
    
# def save_ip_to_file(ip_address):
#     with open('static_ip.txt', 'a') as file:
#         file.write(ip_address + '\n')

# @app.route('/')
# def index():
#     ip_address = get_client_ip()
#     save_ip_to_file(ip_address)
#     print("ip la: "+str(ip_address))
#     # commit_to_github()

#     return 'IP đã được lưu vào tệp tin.'

# if __name__ == '__main__':
#     app.run(debug=True)
