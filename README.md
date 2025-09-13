---
# 🚀 Employee Management API (FastAPI + MongoDB)

A simple API built with **FastAPI** and **MongoDB** to manage employees.  
It supports creating, updating, deleting, and querying employees.

---

## ⚡ Installation & Setup

### 1. Clone this repository
```bash
git clone https://github.com/pkc144/employee_api.git
cd employee_api
````

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

Make sure you have a `requirements.txt` file with:

```
fastapi
uvicorn
pymongo
pydantic
python-jose
passlib[bcrypt]
```

Then install:

```bash
pip install -r requirements.txt
```

### 4. Start MongoDB

Make sure MongoDB server is running on your machine (default: `mongodb://localhost:27017`).
The database `assessment_db` and collection `employees` will be created automatically.

### 5. Run the app

```bash
uvicorn main:app --reload
```

---

## 📖 How to Check Routes

### Swagger UI (interactive API docs)

Open in browser:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Example Endpoints

* **Create Employee**

  ```http
  POST /employees
  ```

  Request body:

  ```json
  {
    "employee_id": "E001",
    "name": "Alice",
    "department": "Engineering",
    "salary": 80000,
    "joining_date": "2023-01-15",
    "skills": ["Python", "FastAPI"]
  }
  ```

* **Get Employee by ID**

  ```http
  GET /employees/E001
  ```

* **Update Employee**

  ```http
  PUT /employees/E001
  ```

  Request body:

  ```json
  {
    "salary": 90000
  }
  ```

* **Delete Employee**

  ```http
  DELETE /employees/E001
  ```

* **List Employees (by department)**

  ```http
  GET /employees?department=Engineering
  ```

* **Average Salary by Department**

  ```http
  GET /employees/avg-salary
  ```

* **Search Employees by Skill**

  ```http
  GET /employees/search?skill=Python
  ```

---

## 🛠 Tech Stack

* **FastAPI** (Python framework)
* **MongoDB** (Database)
* **Uvicorn** (Server)
* **Pydantic** (Validation)

---

## 👨‍💻 Author

* GitHub: [pkc144](https://github.com/pkc144)

