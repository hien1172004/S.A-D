class RegisterCustomerUseCase:
    def __init__(self, customer_repo):
        self.customer_repo = customer_repo

    def execute(self, name, email, password):
        if self.customer_repo.find_by_email(email):
            raise Exception("Email already exists")
        return self.customer_repo.create(name, email, password)
