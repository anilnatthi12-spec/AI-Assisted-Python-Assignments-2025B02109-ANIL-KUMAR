import hashlib
import secrets
import logging
from typing import Dict, Tuple

class LoginSystem:
    def __init__(self):
        self.users: Dict[str, Tuple[bytes, bytes]] = {}  # username -> (salt, hashed_password)
        self.max_attempts = 3
        self.attempt_count = {}

        # Set up logging
        logging.basicConfig(
            filename='login_activity.log',
            level=logging.INFO,
            format='%(asctime)s:%(levelname)s:%(message)s'
        )

    def register(self, username: str, password: str) -> bool:
        if username in self.users:
            return False

        # Generate random salt
        salt = secrets.token_bytes(32)

        # Hash password with salt
        hashed = self._hash_password(password, salt)

        # Store user data
        self.users[username] = (salt, hashed)
        logging.info(f"New user registered: {username}")
        return True

    def login(self, username: str, password: str) -> bool:
        # Check if user exists
        if username not in self.users:
            logging.warning(f"Login attempt for non-existent user: {username}")
            return False

        # Check attempt count
        if self.attempt_count.get(username, 0) >= self.max_attempts:
            logging.warning(f"Account locked due to too many attempts: {username}")
            return False

        salt, stored_hash = self.users[username]

        # Successful login
        if self._hash_password(password, salt) == stored_hash:
            self.attempt_count[username] = 0
            logging.info(f"Successful login: {username}")
            return True

        # Failed login → increment attempts
        self.attempt_count[username] = self.attempt_count.get(username, 0) + 1
        logging.warning(f"Failed login attempt for user: {username}")
        return False

    def _hash_password(self, password: str, salt: bytes) -> bytes:
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000  # Number of iterations
        )


# ============================
# Example usage
# ============================

if __name__ == "__main__":
    login_system = LoginSystem()

    # Register user
    print("Registering user1:", login_system.register("user1", "mypassword"))

    # Login attempts
    print("Login success:", login_system.login("user1", "mypassword"))
    print("Login fail:", login_system.login("user1", "wrongpass"))
