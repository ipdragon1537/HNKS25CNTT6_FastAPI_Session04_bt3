"""
1. Input của bài toán
API: GET /products
Query Parameters
key:str
max_price:float
2.Output mong muốn 
API trả về danh sách sản phẩm sau khi áp dụng các điều kiện tìm kiếm/lọc.
3. Đề xuất giải pháp xử lý bài toán
Ý tưởng
Khởi tạo danh sách kết quả bằng toàn bộ sản phẩm.
Nếu có keyword:
Chuyển tên sản phẩm và từ khóa về chữ thường bằng lower().
Kiểm tra từ khóa có xuất hiện trong tên sản phẩm hay không.
Nếu có max_price:
Kiểm tra giá trị có âm không.
Nếu âm ⇒ phát sinh lỗi HTTPException.
Nếu hợp lệ ⇒ chỉ giữ lại sản phẩm có giá nhỏ hơn hoặc bằng max_price.
Trả về danh sách kết quả sau khi lọc.
4. Thiết kế các bước xử lý
Bước 1: Nhận request GET /products
Bước 2: Đọc keyword và max_price
Bước 3: Kiểm tra max_price
        |
        |-- max_price < 0
        |      → Trả lỗi
        |
        |-- Hợp lệ
               ↓
Bước 4: Lấy toàn bộ products
Bước 5: Nếu có keyword
        → Lọc theo tên (không phân biệt hoa thường)
Bước 6: Nếu có max_price
        → Lọc theo giá <= max_price
Bước 7: Trả về danh sách kết quả
""" 
from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]
@app.get("/products")
def get_product(keyword:str = None,max_price:float = None):
    if max_price is not None and max_price < 0:
        return {"message":"Giá ko hợp lệ"}
    if keyword is not None:
        result = [product for product in products if keyword.lower() in product["name"].lower()]
    return result
    if max_price is not None:
        result = [product for product in products if product["price"] <= max_price]
    return result

