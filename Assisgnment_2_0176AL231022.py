import json
import os

USERS_FILE = "students.json"

def safe_input(prompt):
    """Safely get user input."""
    try:
        return input(prompt)
    except EOFError:
        return ""

def load_json(filename):
    """Load JSON file, return empty dict if not found."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

def save_json(filename, data):
    """Save data to JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def ensure_file_exists(filename, default):
    """Ensure file exists with default content."""
    if not os.path.exists(filename):
        save_json(filename, default)

def register():
    users = load_json(USERS_FILE)
    enroll = safe_input("Enter enrollment/username: ").strip()
    if not enroll:
        print("Enrollment cannot be empty.")
        return
    if enroll in users:
        print("User already exists! Try logging in.")
        return
    password = safe_input("Enter password: ").strip()
    name = safe_input("Enter name: ").strip()
    email = safe_input("Enter email: ").strip()
    branch = safe_input("Enter branch: ").strip()
    year = safe_input("Enter year: ").strip()
    contact = safe_input("Enter contact number: ").strip()
    # Add more fields as needed (at least 10):
    dob = safe_input("Enter date of birth: ").strip()
    gender = safe_input("Enter gender: ").strip()
    address = safe_input("Enter address: ").strip()
    users[enroll] = {
        "password": password,
        "name": name,
        "email": email,
        "branch": branch,
        "year": year,
        "contact": contact,
        "dob": dob,
        "gender": gender,
        "address": address,
        "role": "user"
    }
    save_json(USERS_FILE, users)
    print("Registration successful!")

def login():
    users = load_json(USERS_FILE)
    enroll = safe_input("Enter enrollment/username: ").strip()
    password = safe_input("Enter password: ").strip()
    if enroll in users and users[enroll].get("password") == password:
        print(f"Welcome, {users[enroll].get('name')}, {enroll}!")
        return enroll
    print("Invalid credentials.")
    return None

def view_profile(enroll):
    users = load_json(USERS_FILE)
    user = users.get(enroll)
    if not user:
        print("User not found.")
        return
    print("--- PROFILE ---")
    for k, v in user.items():
        if k != "password":
            print(f"{k.capitalize()}: {v}")

def update_profile(enroll):
    users = load_json(USERS_FILE)
    user = users.get(enroll)
    if not user:
        print("User not found.")
        return
    print("Leave blank to keep current value.")
    for field in ["name", "email", "branch", "year", "contact", "dob", "gender", "address"]:
        current = user.get(field, "")
        newval = safe_input(f"{field.capitalize()} ({current}): ").strip()
        if newval:
            user[field] = newval
    users[enroll] = user
    save_json(USERS_FILE, users)
    print("Profile updated successfully!")

def user_menu(enroll):
    while True:
        print("--- USER MENU ---")
        print("1. View Profile")
        print("2. Update Profile")
        print("3. Logout")
        choice = safe_input("Enter choice: ").strip()
        if choice == "1":
            view_profile(enroll)
        elif choice == "2":
            update_profile(enroll)
        elif choice == "3":
            print("Logged out.")
            break
        else:
            print("Invalid, try again")

def main():
    ensure_file_exists(USERS_FILE, {})
    print("Welcome to the Student System!")
    while True:
        print("Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = safe_input("Enter choice: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid, try again")

if __name__ == "__main__":
    main()
