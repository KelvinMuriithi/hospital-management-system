# 🏥 Hospital Management System (Python + SQLAlchemy)

This is a simple hospital management system built with **Python** and **SQLAlchemy ORM**. The system models key entities such as **Doctors**, **Patients**, **Departments**, and the treatments that link doctors to patients. It demonstrates practical implementations of **Object-Oriented Programming (OOP)**, **database relationships**, and **ORM concepts**.

---

## 📁 Project Structure

```
hospital_management/
├── db.py              # Database engine, session & Base declaration
├── models.py          # SQLAlchemy ORM models (Doctor, Patient, Department)
├── main.py            # Sample data population and main logic
├── requirements.txt   # Python dependencies
└── README.md          # Project overview and instructions
```

---

## 🔧 Features

- Models hospital structure using:
  - Departments (one-to-many with doctors)
  - Doctors (many-to-many with patients)
  - Patients
- Demonstrates:
  - SQLAlchemy relationships: one-to-many, many-to-many
  - ORM inheritance
  - Declarative base usage
- Populates a SQLite database with test data
- Logs SQL statements to the console (`echo=True`)

---

## 🧠 Concepts Covered

- Python Classes & Inheritance
- Instance Methods & Object Relationships in OOP
- SQL Basics & Relationships
- SQLAlchemy ORM
- Declarative Table Definitions
- Many-to-Many and One-to-Many Relationships
- Database Session Management

---

## ⚙️ Installation & Setup

1. **Clone this repository** or download the files.

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the program to generate and populate the database:**
   ```bash
   python main.py
   ```

   > This will create a `hospital.db` SQLite database and populate it with sample doctors, patients, and department data.

---

## 🗃️ Sample Relationships

- **One Department** ➝ **Many Doctors**
- **One Doctor** ➝ **Many Patients**
- **One Patient** ➝ **Many Doctors**  
  _(via many-to-many association table `treatments_made`)_

---

## 📚 Requirements

- Python 3.7+
- SQLAlchemy

---

## ✅ Example Requirements File (`requirements.txt`)

```txt
SQLAlchemy==2.0.29
```

---

## 🤝 Contributions

If you want to expand this project (e.g., with FastAPI or Flask), feel free to fork and submit a pull request!

---

## 📬 Contact

For suggestions or contributions, reach out via email or GitHub.