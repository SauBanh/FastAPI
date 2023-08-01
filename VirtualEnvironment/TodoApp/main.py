from typing import Annotated # cho phép bạn thêm thông tin metadata vào kiểu dữ liệu của một biến, hàm, hay đối tượng trong Python
from sqlalchemy.orm import Session # tạo một phiên làm việc (Session) và sử dụng nó để thực hiện các hoạt động như truy vấn (query), thêm, sửa đổi hoặc xóa dữ liệu.
from fastapi import FastAPI, Depends, HTTPException, Path #Import lớp FastAPI từ thư viện FastAPI để tạo ứng dụng web.
import models # Import module models, giả định là mô hình ORM
from models import Todos #  import (nhập) lớp Todos từ module models.
from database import engine, SessionLocal
from starlette import status
from pydantic import BaseModel, Field

# Import đối tượng engine và SessionLocal từ module database. engine là đối tượng kết nối cơ sở dữ liệu đã được tạo bằng create_engine, và SessionLocal là đối tượng sessionmaker đã được cấu hình để tạo phiên làm việc với cơ sở dữ liệu.
app = FastAPI() # Tạo một đối tượng app làm việc với ứng dụng FastAPI.

models.Base.metadata.create_all(bind=engine)
#  tạo bảng trong cơ sở dữ liệu sử dụng SQLAlchemy ORM. Cụ thể, nó sử dụng đối tượng Base (đã được định nghĩa trong module models) để tạo tất cả các bảng có trong hệ thống (nếu chưa tồn tại) và liên kết chúng với đối tượng engine. Việc này đảm bảo rằng cơ sở dữ liệu sẽ được khởi tạo và sẵn sàng để lưu trữ dữ liệu của ứng dụng.
def get_db(): #Định nghĩa hàm get_db, một generator function được sử dụng làm dependency trong FastAPI.
    db = SessionLocal() # tạo một đối tượng phiên làm việc (db) bằng cách gọi hàm SessionLocal(). Hàm SessionLocal() đã được định nghĩa trong module database.py và tạo ra một phiên làm việc mới với cơ sở dữ liệu
    try: # Bắt đầu một khối try-except để thực hiện các câu lệnh trong khối try
        yield db # Dòng này là lý do chúng ta gọi get_db là một generator function. Thay vì trả về db bằng return, chúng ta sử dụng yield để trả về db nhưng vẫn giữ lại trạng thái của hàm. Tức là, hàm này sẽ trả về db cho API endpoint sử dụng dependency của nó, nhưng nó vẫn giữ lại trạng thái của hàm để tiếp tục thực hiện câu lệnh tiếp theo.
    finally: #  Đây là khối finally của try-except. Một khối finally được thực thi sau khi các câu lệnh trong khối try hoặc khối except hoàn thành.
        db.close() # rong khối finally, chúng ta gọi db.close() để đảm bảo rằng phiên làm việc sẽ được đóng sau khi hoàn thành công việc. Điều này đảm bảo rằng phiên làm việc sẽ được giải phóng và không tốn tài nguyên khi không cần thiết nữa.

db_dependency = Annotated[Session, Depends(get_db)]

# Định nghĩa một class dữ liệu (data class) TodoRequest kế thừa từ BaseModel
class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

@app.get("/", status_code=status.HTTP_200_OK) # 
async def read_all(db: db_dependency): # Định nghĩa hàm read_all là một asynchronous function (hàm không đồng bộ) và sử dụng dependency get_db để nhận vào một database session (db). Chúng ta đã thấy trong đoạn mã trước đó cách sử dụng dependency get_db để tạo một phiên làm việc với cơ sở dữ liệu.
    return db.query(Todos).all() # Trong hàm read_all, chúng ta sử dụng database session db để thực hiện truy vấn (query) trong cơ sở dữ liệu. Chúng ta gọi db.query(Todos) để thực hiện truy vấn trên bảng "todos". Hàm query() là một phương thức của database session, và chúng ta truyền lớp Todos làm tham số để chỉ định rằng chúng ta muốn truy vấn từ bảng "todos". Cuối cùng, chúng ta gọi .all() để trả về tất cả các bản ghi từ cơ sở dữ liệu.

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found.")

@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict())
    db.add(todo_model)
    db.commit()

@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found.")
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete
    db.add(todo_model)
    db.commit()

@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found.")
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()