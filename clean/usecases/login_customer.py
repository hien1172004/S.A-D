class LoginCustomerUseCase:
    def __init__(self, customer_repo):
        self.customer_repo = customer_repo

    def execute(self, email, password):
        customer = self.customer_repo.find_by_email(email)
        if not customer or customer.password != password:
            raise Exception("Invalid credentials")
        return customer
