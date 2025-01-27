from flask import Flask
from app import create_app

if __name__ == "__main__":
    app: Flask = create_app()
    app.run(debug=True, host="0.0.0.0", port=3000)
