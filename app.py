from app.api.v1 import application


if __name__ == "__main__":
    application.run()

app = application


def app():
    return application.run()