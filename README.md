# 💒 Wedding Seating Optimization System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-green.svg)
![Genetic%20Algorithm](https://img.shields.io/badge/Algorithm-Genetic%20Algorithm-orange.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

## 📌 Giới thiệu

**Wedding Seating Optimization System** là ứng dụng hỗ trợ sắp xếp chỗ ngồi trong tiệc cưới bằng **Giải thuật Di truyền (Genetic Algorithm - GA)**.

Chương trình giúp tối ưu việc phân chia khách vào các bàn dựa trên mức độ quan hệ giữa các khách mời, nhằm tăng sự thoải mái, gắn kết và tạo không khí vui vẻ trong buổi tiệc.

---

## ✨ Chức năng chính

- 👥 Quản lý danh sách khách mời
- ❤️ Thiết lập quan hệ giữa các khách
- 📂 Import dữ liệu từ file CSV
- 🧬 Tối ưu chỗ ngồi bằng Genetic Algorithm
- 📊 Hiển thị biểu đồ Fitness
- 🪑 Hiển thị kết quả phân chia bàn
- 📈 Theo dõi quá trình hội tụ của thuật toán

---

## 🖥️ Giao diện chương trình

### Trang chính

> Thêm ảnh vào thư mục `screenshots`

```
screenshots/home.png
```

### Kết quả tối ưu

```
screenshots/result.png
```

### Biểu đồ Fitness

```
screenshots/chart.png
```

---

## 🧬 Thuật toán Genetic Algorithm

Quy trình thực hiện:

1. Khởi tạo quần thể ngẫu nhiên
2. Đánh giá Fitness
3. Chọn lọc (Tournament Selection)
4. Lai ghép (Crossover)
5. Đột biến (Mutation)
6. Elitism
7. Lặp đến khi đạt số thế hệ mong muốn
8. Trả về nghiệm tốt nhất

---

## 📂 Cấu trúc Project

```
WeddingGA
│
├── main.py
├── models.py
├── ga.py
├── fitness.py
├── data.py
├── guests.csv
│
├── screenshots/
│   ├── home.png
│   ├── result.png
│   └── chart.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Công nghệ sử dụng

- Python
- CustomTkinter
- Tkinter
- Pandas
- Matplotlib
- Genetic Algorithm

---

## 🚀 Cài đặt

Clone project

```bash
git clone https://github.com/minhducc14/WeddingGA.git
```

Di chuyển vào project

```bash
cd WeddingGA
```

Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## ▶️ Chạy chương trình

```bash
python main.py
```

---

## 📋 Dữ liệu đầu vào

Có thể nhập:

- Thêm từng khách
- Thêm danh sách khách
- Import từ CSV

Ví dụ:

| Khách | Quan hệ |
|--------|----------|
| A | Bạn bè |
| B | Vợ chồng |
| C | Anh chị em |
| D | Không quen |

---

## 📊 Kết quả đầu ra

Sau khi chạy thuật toán, chương trình sẽ:

- Chia khách thành các bàn
- Hiển thị Fitness tốt nhất
- Hiển thị sơ đồ bàn
- Vẽ biểu đồ Fitness theo từng thế hệ

---

## 💡 Ý tưởng tối ưu

Fitness được tính dựa trên tổng điểm quan hệ giữa các khách trong cùng một bàn.

Quan hệ càng thân thiết:

- Vợ chồng
- Cha mẹ - con
- Anh chị em
- Bạn thân

=> Điểm Fitness càng cao.

---

## 📖 Mô hình hoạt động

```
Nhập khách
      │
      ▼
Thiết lập quan hệ
      │
      ▼
Tạo ma trận quan hệ
      │
      ▼
Genetic Algorithm
      │
      ▼
Tối ưu chỗ ngồi
      │
      ▼
Hiển thị kết quả
```

---

## 👨‍💻 Tác giả

**Nguyễn Minh Đức**

Sinh viên ngành Công nghệ Thông tin

---

## 📚 Kiến thức áp dụng

- Genetic Algorithm
- Data Structure
- Object-Oriented Programming
- Python GUI
- Data Processing

---

## 📄 License

Dự án được phát triển phục vụ mục đích học tập và nghiên cứu.

MIT License

---

## ⭐ Nếu dự án hữu ích

Hãy để lại một ⭐ cho repository nhé!
