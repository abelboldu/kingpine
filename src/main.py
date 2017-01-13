from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('result.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
