from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Merhaba! Kalıp Takip Uygulaması yayında.'

if __name__ == '__main__':
    app.run()


