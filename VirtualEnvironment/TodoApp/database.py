from sqlalchemy import create_engine # sử dụng để tạo đối tượng kết nối cơ sở dữ liệu.
from sqlalchemy.orm import sessionmaker # cho phép bạn tạo các phiên làm việc với cơ sở dữ liệu.
from sqlalchemy.ext.declarative import declarative_base #  từ SQLAlchemy, một lớp cơ sở mà tất cả các lớp đối tượng (ORM) của bạn sẽ được dựa trên nó
# Định nghĩa một biến 
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db" # chứa URL cơ sở dữ liệu cho ứng dụng. Trong trường hợp này, URL là "sqlite:///./todos.db", nghĩa là sử dụng SQLite database lưu trữ trong tệp "todos.db" tại thư mục hiện tại.

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:0962147976@localhost/TodoApplicationDatabase"

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:0962147976@127.0.0.1:3306/todoaplicationdatabase"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)
#  Tạo một đối tượng engine làm việc với cơ sở dữ liệu bằng cách gọi hàm create_engine. Đối số connect_args={'check_same_thread': False} được sử dụng trong trường hợp SQLite để tránh lỗi "SQLite objects created in a thread can only be used in that same thread".
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Tạo một sessionmaker được gọi là SessionLocal. SessionLocal là một hàm, và khi nó được gọi, nó sẽ tạo ra một đối tượng phiên làm việc (Session) dựa trên cơ sở dữ liệu đã cấu hình trong engine. Các đối số autocommit=False và autoflush=False được sử dụng để tắt tự động commit và tự động flush, giúp quản lý giao dịch một cách rõ ràng hơn.
Base = declarative_base()
# Tạo một đối tượng cơ sở gọi là Base bằng cách gọi declarative_base(). Base là một lớp cơ sở mà tất cả các lớp đối tượng (ORM) khác trong ứng dụng của bạn sẽ kế thừa từ nó. Việc này giúp bạn định nghĩa các lớp đối tượng mô hình dễ dàng và truy vấn cơ sở dữ liệu bằng cách sử dụng các lớp này mà không cần viết SQL trực tiếp.