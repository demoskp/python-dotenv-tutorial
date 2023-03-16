import os
from flask import Flask

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

print(os.environ.get("FLASK_DEBUG"))
print(os.environ.get("DATABASE_URI"))

host = os.environ.get("APP_HOST", "0.0.0.0")
port = os.environ.get("FLASK_DEVELOPMENT_PORT", 8000)
debug = os.environ.get("FLASK_DEBUG", False)

if __name__ == "__main__":
    app.run(host=host, port=port, debug=debug)
