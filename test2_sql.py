# sqlite 라이브러리
import sqlite3


# 0. 사용자 입력을 받아 Gemini API를 이용하여 적절한 SQL로 변환하는 함수
def nl_to_sql(prompt, A):
    # 잼민이가 답변해준 쿼리를 변수로 지정해주고 그 변수를 'A'에 지정
    return A

# 1. SQL 클래스 정의
class SQLInterface:
    def __init__(self, db_name = 'crawldb.db'):
        self.db_name = db_name

    # 2. 데이터베이스 생성 함수
    def create_db(self):
        try:
            # conn 변수에 데이터베이스 연결 선언 (변수 = sqlite3.connect(연결할DB명))
            conn = sqlite3.connect(self.db_name)
            # 연결된 DB에 커서 생성 (커서는 값을 바로보는 위치를 알기 위해 필요)
            c = conn.cursor()
            # 테이블 생성 SQL 쿼리문 작성 및 실행 (만약 'crawldb_table'이 있으면 생략, 없으면 생성)
            # 쿼리문은 별도 변수로 선언해서 c.execute(변수) < 이렇게 넣어줘도 상관없음
            c.execute('''CREATE TABLE IF NOT crawldb_table (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        summary TEXT)
                    ''')
            # 변경사항 커밋
            conn.commit()
            # 연결 종료
            conn.close()
        except Exception as e:
            print("데이터베이스 생성 중 오류가 발생했습니다:", str(e))
    
    # 데이터 삽입 메서드
    def insert_data(self, title, summary):
        try:
            # 다시 DB 연결
            conn = sqlite3.connect(self.db_name)
            # 다시 커서 생성 
            c = conn.cursor()
            # 쿼리 작성
            sql = "INSERT INTO crawldb_table (title, summary) VALUES (?, ?)"
            # 데이터 삽업 쿼리 실행
            c. execute(sql,(title, summary))
            conn.commit()
            conn.close()
        except Exception as e:
            print("데이터 삽입 중 오류가 발생했습니다:", str(e))


    # 3. 데이터 조회 함수
    def insert_data(self, view):
        try:
            # 다시 DB 연결
            conn = sqlite3.connect(self.db_name)
            # 다시 커서 생성 
            c = conn.cursor()
            # SQL 쿼리 실행
            c. execute(view)
            # 결과 가져오기
            rows = c.fetchall()
            # 연결 종료
            conn.close()
        except Exception as e:
            print("쿼리가 잘못 되었는지 확인해보시기 바랍니다.", str(e))
            return None