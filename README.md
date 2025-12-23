# FastAPI MongoDB Mini E-commerce

A mini e-commerce application built with **FastAPI**, **MongoDB**, and **Tailwind CSS**.  
This project demonstrates how to build a RESTful API with FastAPI and consume it from a simple frontend.

---

## 🚀 Features

- Add products using a FastAPI REST API
- View products from MongoDB
- Product attributes:
  - Name
  - Price
  - Description
  - Image
- Asynchronous MongoDB access using Motor
- Simple and clean UI with Tailwind CSS

---

## 🛠 Tech Stack

**Backend**
- FastAPI
- Python
- MongoDB
- Motor (async MongoDB driver)
- Pydantic

**Frontend**
- HTML
- JavaScript (Fetch API)
- Tailwind CSS

---

## 📂 Project Structure

fastapi-mongo-ecommerce/
├── app/
│ ├── main.py
│ ├── database.py
│ ├── routes/
│ │ └── product.py
│ └── schemas/
│ └── product.py
├── frontend/
│ ├── index.html # Admin page (add products)
│ └── products.html # Public products page
├── .gitignore
└── README.md


---

## ⚙️ Setup & Installation

```bash
## Clone the repository
git clone https://github.com/medYass19/fastapi-mongo-products.git   
cd fastapi-mongo-ecommerce
---

## Install dependencies
pip install fastapi uvicorn motor pydantic
Start MongoDB
Make sure MongoDB is running locally:
mongod
Run the backend
uvicorn app.main:app --reload
Backend runs at:
http://127.0.0.1:8000
 Run the frontend
cd frontend
python3 -m http.server 5500


