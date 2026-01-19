from domain.entities.customer import Customer
from accounts.models import CustomerModel

class DjangoCustomerRepository:
    def create(self, name, email, password):
        obj = CustomerModel.objects.create(
            name=name,
            email=email,
            password=password
        )
        return Customer(obj.id, obj.name, obj.email, obj.password)

    def find_by_email(self, email):
        try:
            obj = CustomerModel.objects.get(email=email)
            return Customer(obj.id, obj.name, obj.email, obj.password)
        except CustomerModel.DoesNotExist:
            return None
