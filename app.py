from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route('/')
def home():
    return "Hello Anh Ngoc"
if __name__=='__main__':
    app.run(debug=True)