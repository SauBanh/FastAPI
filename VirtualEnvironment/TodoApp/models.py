from database import Base
# Import lớp Base từ module database. Base là một lớp cơ sở đã được định nghĩa trong database.py bằng Base = declarative_base() 

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# Import các lớp cơ sở từ SQLAlchemy để định nghĩa các cột trong bảng.

class Users(Base):
    __tablename__ = 'users' # Thuộc tính __tablename__ định nghĩa tên của bảng trong cơ sở dữ liệu mà lớp User tương ứng với. Trong trường hợp này, bảng tương ứng có tên "

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True) #unique=True email là duy nhất
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)

class Todos(Base): #  Định nghĩa lớp Todos, kế thừa từ lớp Base, tức là lớp này là một lớp đối tượng mô hình được định nghĩa bởi SQLAlchemy.
    __tablename__ = 'todos' # Thuộc tính __tablename__ định nghĩa tên của bảng trong cơ sở dữ liệu mà lớp Todos tương ứng với. Trong trường hợp này, bảng tương ứng có tên "todos".
    
    id = Column(Integer, primary_key=True, index=True) #  Định nghĩa cột "id" trong bảng "todos". Cột này là kiểu số nguyên (Integer), là khóa chính (primary key) của bảng và có chỉ số (index) để tăng tốc tìm kiếm.
    title = Column(String) # Định nghĩa cột "title" trong bảng "todos". Cột này là kiểu chuỗi (String).
    description = Column(String) # Định nghĩa cột "description" trong bảng "todos". Cột này cũng là kiểu chuỗi (String).
    priority = Column(Integer) # Định nghĩa cột "priority" trong bảng "todos". Cột này là kiểu số nguyên (Integer).
    complete = Column(Boolean, default=False) # Định nghĩa cột "complete" trong bảng "todos". Cột này là kiểu Boolean (True hoặc False) và có giá trị mặc định là False (chưa hoàn thành).
    owner_id = Column(Integer, ForeignKey("users.id"))
# Với định nghĩa trên, lớp Todos có thể được sử dụng như một mô hình để tương tác với bảng "todos" trong cơ sở dữ liệu. Bạn có thể thêm, sửa đổi, truy vấn và xóa dữ liệu trong bảng "todos" thông qua các thao tác với đối tượng Todos này.