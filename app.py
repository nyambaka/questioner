from app.api.v1 import application

app = application

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
