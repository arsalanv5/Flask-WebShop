# 🛒 Flask WebShop

A simple WebShop web application built using Flask and SQLite.

This project was developed as part of an academic coursework under the supervision of our instructor. The goal was to understand backend web development fundamentals including authentication, session management, database integration, and application structure.

During development, modern AI-assisted tools were used as learning support to explore best practices and improve implementation quality.

---

## 🚀 Features

- User Registration & Login
- Session-based Authentication
- Product Management (Admin Panel)
- Shopping Cart System
- Checkout Logic
- SQLite Database Integration
- Template Inheritance (Jinja2)
- Basic UI Styling (CSS)

---

## 🛠 Technologies Used

- Python
- Flask
- SQLite
- SQLAlchemy
- HTML / CSS
- Jinja2
- Git

---

## 📂 Project Structure
```
  webshop/
  │
  ├── app.py
  ├── models.py
  ├── webshop.db
  ├── templates/
  │ ├── base.html
  │ ├── login.html
  │ ├── register.html
  │ ├── products.html
  │ ├── cart.html
  │ └── admin.html
  │
  ├── static/
  │ └── style.css
  │
  └── .gitignore
```


---

## ⚙️ Setup Instructions

1. **Clone the repository:**
```bash
  git clone <your-repo-url>
  cd Flask-WebShop
```

2. **Create virtual environment (optional but recommended):**
```bash
  python -m venv venv
  venv\Scripts\activate
```

3. **Install dependencies:**
```bash
  pip install flask flask_sqlalchemy
```

4. **Run the application:**
```bash
  python app.py
```

5. **Open in browser:**
```bash
  http://127.0.0.1:5000
```

---

## 🎓 Academic Context

This project was implemented as a class assignment to practice backend web development concepts. The implementation was done in the presence of the instructor, with discussions around architecture and design decisions.

AI tools were used as educational support to explore alternative approaches, debug issues, and better understand Flask and database integration concepts.

---

## 📌 Learning Outcomes

- Understanding MVC-style structure in Flask
- Working with relational databases (SQLite)
- Managing user authentication and sessions
- Implementing CRUD operations
- Version control with Git
- Using AI tools responsibly in software development

---

## 📄 License

This project is for educational purposes.
