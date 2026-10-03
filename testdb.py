import pymysql

print("PyMySQL 접속 시작", flush=True)

try:
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="byby3845//",
        connect_timeout=5
    )

    print("PyMySQL 접속 성공", flush=True)

    conn.close()

except Exception as e:
    print("실패:", repr(e), flush=True)