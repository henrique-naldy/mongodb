from src.main.server.server import app
from src.models.connection.connection_handler import db_connection_handler

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)