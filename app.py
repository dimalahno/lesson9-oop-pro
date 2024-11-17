# Пример использования
from authentication_service import AuthenticationService
from users import Customer, Admin, User

auth_service = AuthenticationService()
customer1 = Customer("user1", "user1@example.com", "password123", "Address 1")
customer2 = Customer("user2", "user2@example.com", "password456", "Address 2")
admin1 = Admin("admin", "admin@example.com", "adminpass", 1)

print(customer1.get_details())
print(customer2.get_details())
print(admin1.get_details())

# Регистрация пользователей
print(auth_service.register(customer1))
print(auth_service.register(customer2))
print(auth_service.register(admin1))

# Аутентификация
print(auth_service.login("user1", "password123"))
print(auth_service.get_current_user())

# Список пользователей (доступен только админам)
admin = next((u for u in User.users if isinstance(u, Admin)), None)
if admin:
    print(Admin.list_users())

# Удаление пользователя
print(Admin.delete_user("user1"))