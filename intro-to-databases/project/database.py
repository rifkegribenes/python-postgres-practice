from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1,
                                            10,
                                            database="learning",
                                            user='sarahschneider',
                                            password='Q-@VWfZPUbM3M5xCyRTu',
                                            host="localhost")