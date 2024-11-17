import hashlib
import uuid

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    # Список для хранения всех пользователей
    users = []

    def __init__(self, username, email, password):
        self.id = str(uuid.uuid4())  # Генерируем уникальный UUID
        self.username = username
        self.email = email
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """
        Хеширует пароль с использованием SHA-256.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля.
        """
        return stored_password == hashlib.sha256(provided_password.encode()).hexdigest()

    def get_details(self):
        return f"ID: {self.id}, User: {self.username}, Email: {self.email}"

class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username:str, email:str, password:str, address:str):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        return f"Клиент: {self.username}, Email: {self.email}, Адрес: {self.address}"

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """

    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """
        return [user.get_details() for user in User.users]

    @staticmethod
    def delete_user(username:str):
        """
        Удаляет пользователя по имени пользователя.
        """
        user = next((u for u in User.users if u.username == username), None)
        if user:
            User.users.remove(user)
            return f"Пользователь {username} удален."
        return f"Пользователь {username} не найден."

    def get_details(self):
        return f"Admin: {self.username}, Email: {self.email}, Admin-Level: {self.admin_level}   "
