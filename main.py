
import csv
from datetime import datetime
from getpass import getpass

from password_generator import generate_password
from password_auditor import analyze_password


def save_report(result):
    file_exists = False

    try:
        with open("security_report.csv", "r", newline="",
                  encoding="utf-8") as file:
            file_exists = True
    except FileNotFoundError:
        pass

    with open("security_report.csv", "a", newline="",
              encoding="utf-8") as file:

        fields = [
            "Date",
            "Strength",
            "Score",
            "Entropy",
            "Issues"
        ]

        writer = csv.DictWriter(file, fieldnames=fields)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Strength": result["strength"],
            "Score": result["score"],
            "Entropy": result["entropy"],
            "Issues": "; ".join(result["issues"])
        })


def display_report(result):
    print("\n========== SECURITY REPORT ==========")
    print("Strength:", result["strength"])
    print("Score:", result["score"], "/ 6")
    print("Estimated Entropy:", result["entropy"], "bits")

    print("\nSecurity Suggestions:")

    if result["issues"]:
        for issue in result["issues"]:
            print("-", issue)
    else:
        print("No basic weaknesses detected.")

    save_report(result)
    print("\nSecurity report saved successfully.")


def main():

    while True:

        print("\n====================================")
        print("   SMART PASSWORD SECURITY AUDITOR")
        print("====================================")
        print("1. Generate Secure Password")
        print("2. Analyze Existing Password")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            try:
                length = int(input("Enter password length (8-64): "))

                if not 8 <= length <= 64:
                    print("Please enter a length between 8 and 64.")
                    continue

                password = generate_password(length)

                print("\nGenerated Password:", password)

                result = analyze_password(password)
                display_report(result)

            except ValueError as error:
                print("Invalid input:", error)

        elif choice == "2":

            password = getpass("Enter password to analyze: ")

            if not password:
                print("Password cannot be empty.")
                continue

            result = analyze_password(password)
            display_report(result)

            password = None

        elif choice == "3":
            print("Thank you for using Password Security Auditor!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
