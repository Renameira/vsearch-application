import mysql.connector


class UseDatabase:
    def __init__(self, configuration: dict):
        self.configuration = configuration

    def __enter__(self) -> "cursor":
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
