import psycopg2
import time

# Настройки подключения к базе данных
DB_SETTINGS = {
    "dbname": "serbin",
    "user": "postgres",
    "password": "postgres",
    "host": "db",
    "port": 5432
}

def connect_to_db():
    """Ожидание готовности БД и подключение."""
    while True:
        try:
            conn = psycopg2.connect(**DB_SETTINGS)
            print("Подключение к базе данных успешно!")
            return conn
        except psycopg2.OperationalError:
            print("База данных не готова. Повторная попытка через 3 секунды...")
            time.sleep(15)

def query_test_table(conn):
    """Выполнение запроса: минимальный и максимальный возраст для имен < 6 символов."""
    with conn.cursor() as cursor:
        query = """
        SELECT MIN(age) AS min_age, MAX(age) AS max_age
        FROM test_table
        WHERE LENGTH(name) < 6;
        """
        cursor.execute(query)
        result = cursor.fetchone()
        print(f"Минимальный возраст: {result[0]}")
        print(f"Максимальный возраст: {result[1]}")

def main():
    conn = connect_to_db()
    query_test_table(conn)
    conn.close()

if __name__ == "__main__":
    main()

