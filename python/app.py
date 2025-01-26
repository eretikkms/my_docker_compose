import psycopg2

# Параметры подключения к PostgreSQL
db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "db",
    "port": 5432
}

# Запрос для нахождения минимального и максимального возраста
query = """
SELECT MIN(age) AS min_age, MAX(age) AS max_age
FROM test_table
WHERE LENGTH(name) < 6;
"""

try:
    # Подключение к базе данных
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Выполнение запроса
    cursor.execute(query)
    result = cursor.fetchone()

    # Вывод результата
    print(f"Минимальный возраст: {result[0]}")
    print(f"Максимальный возраст: {result[1]}")

    # Закрытие соединения
    cursor.close()
    conn.close()
except Exception as e:
    print("Ошибка при подключении к базе данных:", e)

