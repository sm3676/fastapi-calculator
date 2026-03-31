# FastAPI Calculator Application

## 📌 Overview
This project is a simple FastAPI-based calculator application that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.  

It also includes unit tests, integration tests, and end-to-end (E2E) tests using Playwright, along with CI/CD using GitHub Actions.

---

## 🚀 Features
- Add, Subtract, Multiply, Divide operations
- REST API built using FastAPI
- Interactive API documentation (Swagger UI)
- Unit Testing with pytest
- Integration Testing for API endpoints
- End-to-End Testing using Playwright
- Logging for operations and errors
- Continuous Integration using GitHub Actions

---

## 🛠️ Technologies Used
- Python
- FastAPI
- Uvicorn
- Pytest
- Playwright
- GitHub Actions

---

## 📂 Project Structure

fastapi-calculator/
│
├── app/
│ ├── main.py
│ ├── operations.py
│ └── init.py
│
├── tests/
│ ├── test_operations.py
│ ├── test_main.py
│ └── test_e2e.py
│
├── requirements.txt
└── README.md


---

## ▶️ How to Run the Application

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/fastapi-calculator.git
cd fastapi-calculator

2. Create virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies:

pip install -r requirements.txt
playwright install

4. Run the application:

uvicorn app.main:app --reload

5. Open in browser:

http://127.0.0.1:8000/docs

🧪 Running Tests

pytest

⚙️ Continuous Integration

GitHub Actions is configured to:

Install dependencies
Run all tests automatically on each push

📸 Screenshots
1. FastAPI Application

Swagger UI showing all endpoints.

2. GitHub Actions

Successful CI pipeline execution.

🎯 Learning Outcomes

Build REST APIs using FastAPI
Write unit, integration, and E2E tests
Implement logging
Use GitHub for version control
Set up CI/CD pipelines



👩‍💻 Author

Sharvani Rao