from usecases.register_customer import RegisterCustomerUseCase
from usecases.login_customer import LoginCustomerUseCase
from infrastructure.repositories.customer_repository import DjangoCustomerRepository

class AccountController:
    def register(self, data):
        uc = RegisterCustomerUseCase(DjangoCustomerRepository())
        return uc.execute(data["name"], data["email"], data["password"])

    def login(self, data):
        uc = LoginCustomerUseCase(DjangoCustomerRepository())
        return uc.execute(data["email"], data["password"])
