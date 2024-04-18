# RDBMS, SQL 쿼리 처리
# class SQLInterface:
#     def query_db(self):
#         # TODO: SQL 쿼리 처리 구현
#         pass

import sqlite3  # SQLite 라이브러리

# 데이터베이스 생성 함수
def create_db():
    # 데이터베이스에 연결
    conn = sqlite3.connect('langdb.db')
    # 커서를 생성
    c = conn.cursor()
    # 데이터베이스에 테이블을 생성. 이미 존재하는 경우에는 생성하지 않음
    c.execute('''CREATE TABLE IF NOT EXISTS my_table (
                id INTEGER PRIMARY KEY,
                title TEXT,
                summary TEXT)
              ''')
    # 변경사항을 저장
    conn.commit()
    # 연결을 닫음
    conn.close()

# 데이터 삽입 함수
def insert_data(title, summary):
    # 데이터베이스에 연결
    conn = sqlite3.connect('langdb.db')
    # 커서를 생성
    c = conn.cursor()
    # 데이터를 삽입하는 SQL 쿼리를 실행
    c.execute("INSERT INTO my_table (title, summary) VALUES (?, ?)", (title, summary))
    # 변경사항을 저장
    conn.commit()
    # 연결을 닫음
    conn.close()

# 데이터베이스에 예제 데이터 추가하는 함수 정의
# def add_example_data():
#     # 예제 데이터 생성
#     example_data = [
#         ("제목1", "요약1"),
#         ("제목2", "요약2"),
#         ("제목3", "요약3"),
#         ("제목4", "요약4"),
#         ("제목5", "요약5")
#     ]
#     # 예제 데이터를 하나씩 가져와서 데이터베이스에 추가
#     for data in example_data:
#         insert_data(data[0], data[1])

# 데이터베이스 생성
create_db()

# 예제 데이터 삽입
# add_example_data()

# 예제 쿼리 실행
conn = sqlite3.connect('langdb.db')
cur = conn.cursor()
sql = "SELECT * FROM my_table where "
cur.execute(sql)
rows =cur.fetchall()
for row in rows:
    print(row)