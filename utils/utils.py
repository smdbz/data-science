# utils.py
import os
from pathlib import Path

from abc import ABC, abstractmethod


def find_project_root(markers=("pyproject.toml", "README.md", ".git"), root_name="data-science"):
    """Find the project root by searching for marker files or root directory name."""
    current = Path.cwd().resolve()
    for directory in [current, *current.parents]:
        if any((directory / marker).exists() for marker in markers) or directory.name == root_name:
            return directory
    return current


def setup_project_root():
    """Change to the project root and return the path."""
    root = find_project_root()
    os.chdir(root)
    return root


class BaseNotification(ABC):
    def send(self, user, message):
        """
        The 'Template Method'. It defines the workflow
        that every subclass MUST follow.
        """
        self.connect()
        formatted_msg = self.format_message(message)
        self.dispatch(user, formatted_msg)
        self.log_success(user)

    @abstractmethod
    def connect(self):
        pass

    def format_message(self, message):
        # Default formatting, can be overridden if needed
        return f"[ALERT] {message}"

    @abstractmethod
    def dispatch(self, user, message):
        pass

    def log_success(self, user):
        print(f"Successfully notified {user}")


class EmailNotification(BaseNotification):
    def connect(self):
        print("Connecting to SMTP server...")
    def dispatch(self, user, message):
        print(f"Sending email to {user.email}: {message}")


class SMSNotification(BaseNotification):
    def connect(self):
        print("Connecting to Twilo...")

    def dispatch(self, user, message):
        print(f"Sending SMS to {user.phone}: {self.format_message(message)}")

    def format_message(self, message):
        return f"[ALERT] {message[:160]}"


# A dummy User class for context
class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def __str__(self): return self.name

# The Loop
notifications = [
    EmailNotification(),
    SMSNotification()
]

user_obj = User("Alice", "alice@example.com", "555-0199")

for service in notifications:
    # This is Polymorphism: One interface, many forms.
    service.send(user_obj, "Your server is melting down!")
