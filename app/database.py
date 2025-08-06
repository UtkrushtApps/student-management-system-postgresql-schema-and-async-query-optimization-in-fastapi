import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="student_db",
        user="student_user",
        password="student_pass",
        host="postgres",
        port=5432
    )
