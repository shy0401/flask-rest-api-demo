from app import create_app, db
from sqlalchemy.exc import OperationalError

app = create_app()

if __name__ == '__main__':
    try:
        with app.app_context():
            db.create_all()  # 데이터베이스 테이블 생성
        print("MySQL 연결 성공!")
        app.run(debug=True)
    except OperationalError as e:
        print(f"MySQL 연결 실패: {e}")
