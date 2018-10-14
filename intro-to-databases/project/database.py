from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1,
                                            1,
                                            database="learning",
                                            user='sarahschneider',
                                            password='Q-@VWfZPUbM3M5xCyRTu',
                                            host="localhost")


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:  # e.g. TypeError, AttributionError, ValueError
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)
