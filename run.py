from sys import path
path.append("src/main/python")

from helloapp.webapp import application

if __name__ == "__main__":
    application.run(debug=True)