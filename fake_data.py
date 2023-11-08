from faker import Faker
from faker.providers import BaseProvider

fake = Faker()
# Generate a random name
name = fake.name()

# Generate a random email
email = fake.email()

# Generate a random address
address = fake.address()
# Generate a random account number
account_number = fake.bban()

# Generate a random balance for a bank account
balance = fake.pyfloat(left_digits=4, right_digits=2, positive=True)

# Generate a random transaction amount
transaction_amount = fake.pyfloat(left_digits=2, right_digits=2, positive=True)

# Generate a random account numberafrom faker import Faker
from faker.providers import BaseProvider

class FinancialProvider(BaseProvider):
    def credit_card_debt(self):
        # Generate a random credit card debt value
        return self.random_int(min=1000, max=5000)

    def mortgage(self, min_value=100000, max_value=500000):
        # Generate a random mortgage value
        return self.generator.pyfloat(left_digits=6, right_digits=2, positive=True, min_value=min_value, max_value=max_value)

# Create a new Faker instance
fake = Faker()

# Add the new provider to our faker object
fake.add_provider(FinancialProvider)

# Now we can use our custom methods
credit_card_debt = fake.credit_card_debt()
mortgage_value = fake.mortgage()

# Generate data for 100 users
users = []
for _ in range(100):
    user = {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'account_number': fake.bban(),
        'bank_balance': fake.pyfloat(left_digits=4, right_digits=2, positive=True),
        'credit_card_debt': fake.credit_card_debt(),
        'mortgage_value': fake.mortgage()
    }
    users.append(user)

# Now you can iterate over users to see the generated data
for user in users:
    print(user)

account_number = fake.bban()

# Generate a random balance for a bank account
balance = fake.pyfloat(left_digits=4, right_digits=2, positive=True)

# Generate a random transaction amount
transaction_amount = fake.pyfloat(left_digits=2, right_digits=2, positive=True)

# Create a new provider class
class FinancialProvider(BaseProvider):
    def credit_card_debt(self):
        return self.random_number(digits=4)

    def mortgage(self, min_value=100000, max_value=500000):
        return self.pyfloat(left_digits=6, right_digits=2, positive=True, min_value=min_value, max_value=max_value)

# Add the new provider to our faker object
fake.add_provider(FinancialProvider)

# Now we can use our custom methods
credit_card_debt = fake.credit_card_debt()
mortgage_value = fake.mortgage()

users = []
for _ in range(100):  # Generate data for 100 users
    user = {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'account_number': fake.bban(),
        'bank_balance': fake.pyfloat(left_digits=4, right_digits=2, positive=True),
        'credit_card_debt': fake.credit_card_debt(),
        'mortgage_value': fake.mortgage()
    }
    users.append(user)

