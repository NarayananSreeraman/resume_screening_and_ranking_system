def validate_login(email, password):
    # Hardcoded credentials (Replace with Database in future)
    valid_users = {
        "abc@gmail.com": "Test123#",
        "user2@gmail.com": "user2@123"
    }

    if email in valid_users and valid_users[email] == password:
        return True
    return False
