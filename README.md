# 🔐 Smart Password Generator & Security Auditor

## 📌 Project Overview

The **Smart Password Generator & Security Auditor** is a Python-based command-line application designed to generate secure random passwords and analyze password strength.

The application uses Python's `secrets` module for cryptographically secure password generation and evaluates passwords based on length, character diversity, common password patterns, and estimated entropy.

It also generates CSV security reports without storing the actual passwords.

## 🎯 Objectives

- Generate unpredictable passwords using secure randomness.
- Analyze password strength using multiple criteria.
- Identify common password weaknesses.
- Estimate password entropy.
- Provide useful password improvement suggestions.
- Generate structured CSV security reports.

## ⚙️ Features

- **Secure Password Generation:** Generates passwords using Python's `secrets` module.
- **Custom Password Length:** Allows users to select password lengths between 8 and 64 characters.
- **Character Diversity:** Includes lowercase letters, uppercase letters, digits, and special characters.
- **Password Strength Analysis:** Evaluates passwords using a scoring system.
- **Common Password Detection:** Identifies selected commonly used passwords.
- **Repeated Character Detection:** Flags passwords containing excessive repeated characters.
- **Entropy Estimation:** Estimates password unpredictability in bits.
- **Hidden Password Input:** Uses `getpass()` when analyzing existing passwords.
- **CSV Security Reports:** Saves analysis results without storing actual passwords.

## 🧠 Workflow

1. Launch the command-line application.
2. Select password generation or password analysis.
3. Generate a password or enter an existing password.
4. Evaluate password length and character diversity.
5. Check for common passwords and repeated characters.
6. Calculate an estimated entropy value.
7. Display the password security report.
8. Save the analysis results in a CSV file.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| secrets | Cryptographically secure random generation |
| string | Character sets for password generation |
| math | Entropy calculation |
| getpass | Hidden password input |
| csv | Security report generation |
| datetime | Report timestamps |

## 📊 Security Report Information

The generated `security_report.csv` contains:

- Date and time of analysis
- Password strength
- Security score
- Estimated entropy in bits
- Identified security issues

**Privacy consideration:** Actual passwords are not stored in the generated CSV report.

## 🔍 Technical Concepts

### 1. Secure Random Generation

Uses `secrets.choice()` and `secrets.SystemRandom()` to generate and shuffle password characters securely.

### 2. Password Strength Evaluation

Evaluates passwords using:
- Minimum password length
- Lowercase letters
- Uppercase letters
- Numeric characters
- Special characters
- Common password detection
- Repeated character detection

### 3. Password Entropy

Estimates entropy using password length and the size of the assumed character pool.

The estimate is a simplified calculation and does not account for human password-selection patterns or every possible guessing strategy.

### 4. Python Functions and Conditions

Uses reusable functions, loops, conditional statements, and exception handling to organize the application.

### 5. CSV Report Generation

Uses `csv.DictWriter()` to save structured security analysis results.

## 📁 Project Structure

```text
smart-password-security-auditor/
│
├── main.py
├── password_generator.py
├── password_auditor.py
├── requirements.txt
├── .gitignore
└── security_report.csv    # Generated after execution
```

## 🚀 Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/ayushman-ece/python-smart-password-security-auditor.git
```

### 2. Navigate into the project

```bash
cd python-smart-password-security-auditor
```

### 3. Install dependencies

This project uses only Python's standard library, so no external dependencies are required.

### 4. Run the application

```bash
python main.py
```

### 5. Use the application

Choose from the available options:

1. Generate Secure Password
2. Analyze Existing Password
3. Exit

The security report is generated automatically after a successful analysis.

## 📚 Key Concepts Learned

- Cryptographically secure random generation
- Python `secrets` module
- Python `string` module
- Password strength evaluation
- Character diversity
- Entropy estimation
- Python functions and loops
- Conditional statements
- Exception handling
- Hidden user input with `getpass`
- CSV file handling
- Date and time handling
- Modular Python programming

## ⚠️ Limitations

- Password strength scoring uses a basic rule-based approach.
- Common password detection uses a small predefined list.
- Entropy is an approximate estimate, not a complete security measurement.
- The application does not check passwords against known data breaches.
- It does not evaluate every possible predictable password pattern.
- It does not replace a professional password security assessment.

## 🔮 Future Improvements

- Integrate a larger common-password database.
- Add breached-password checking through a privacy-preserving service.
- Improve password strength evaluation.
- Add graphical user interface support.
- Generate detailed security analytics.
- Support configurable password generation rules.
- Add unit tests for all major functions.

## 👨‍💻 Author

**Ayushman Tiwari**

B.Tech – Electronics and Communication Engineering

GitHub: https://github.com/ayushman-ece

---

⭐ If you find this project useful, consider giving it a star!