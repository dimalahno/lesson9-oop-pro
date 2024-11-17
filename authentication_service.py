from users import User


class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """
    current_user = None

    def register(self, user: User) -> bool:
        """
        Регистрация нового пользователя.
        """
        if any(existing_user.username == user.username for existing_user in User.users):
            print(f"Пользователь с именем {user.username} уже существует.")
            return False
        User.users.append(user)
        print(f"Пользователь {user.username} успешно зарегистрирован.")
        return True


    def login(self, username:str, password:str):
        """
        Аутентификация пользователя.
        """
        user = next((u for u in User.users if u.username == username), None)
        if user and User.check_password(user.password, password):
            AuthenticationService.current_user = user
            return f"Добро пожаловать, {user.username}!"
        return "Неверное имя пользователя или пароль."


    def logout(self):
        """
        Выход пользователя из системы.
        """
        if AuthenticationService.current_user:
            user = AuthenticationService.current_user
            AuthenticationService.current_user = None
            return f"Пользователь {user.username} вышел из системы."
        return "Нет активного пользователя для выхода."

    def get_current_user(self):
        """
        Возвращает текущего вошедшего пользователя.
        """
        if AuthenticationService.current_user:
            return AuthenticationService.current_user.get_details()
        return "Нет текущего пользователя."