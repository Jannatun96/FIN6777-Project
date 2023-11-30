import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wealthwise.settings")
import django
django.setup()
from django.core.exceptions import ObjectDoesNotExist
from faker import Faker
from faker.providers import BaseProvider
import random
import re
import secrets
import string
from django.contrib.auth.models import User
from wealthwiseapp.models import ExpenseCategory, UserProfile, Expense, OtherBankAccount

class FinancialProvider(BaseProvider):
    def bank_account_number(self):
        # Generate random bank acc number
        length = random.randint(8, 12)
        account_number = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        return account_number

    def routing_number(self):
        # Generate a 9-digit routing number
        return ''.join([str(random.randint(0, 9)) for _ in range(9)])

    def bank_balance(self, min_value=20, max_value=10000):
        # Generate a random bank account balance
        return self.generator.pyfloat(left_digits=4, right_digits=2, positive=True, min_value=min_value, max_value=max_value)

    def credit_card_debt(self):
        # Generate a random credit card debt value
        return self.random_int(min=0, max=10000)

    def mortgage(self, min_value=1, max_value=500000):
        # Generate a random mortgage value
        return self.generator.pyfloat(left_digits=6, right_digits=2, positive=True, min_value=min_value, max_value=max_value)

    def car_loan(self):
        # Generate a random car loan value
        return self.random_int(min=1, max=40000)

    def student_loan(self):
        # Generate a random student loan value
        return self.random_int(min=1, max=100000)


class ExtendedFinancialProvider(FinancialProvider):
    def other_bank_account_number(self):
        # Generate a different bank account number
        return self.generator.iban()

    def other_bank_balance(self, original_balance):
        # Generate a bank balance for another bank
        variation_percentage = random.uniform(-0.3, 0.3)
        return original_balance * (1 + variation_percentage)
    def account_type(self):
        # Generate a random account type
        return self.random_element(['Checking', 'Savings'])
    def bank_name(self):
        # Generate a random bank name
        return self.random_element(['Bank of America', 'Wells Fargo', 'JPMorgan Chase Bank NA', 'HSBC'])
    def salary(self, min_value=50000, max_value=150000):
        # Generate a random salary value
        return self.generator.pyfloat(left_digits=6, right_digits=2, positive=True, min_value=min_value, max_value=max_value)

    def cryptocurrency_balance(self):
        # Generate a random cryptocurrency balance
        return self.generator.pyfloat(left_digits=5, right_digits=2, positive=True)
    def stocks_value(self):
        # Generate a random value for stocks
        return self.generator.pyfloat(left_digits=4, right_digits=2, positive=True)

    def bonds_value(self):
        # Generate a random value for bonds
        return self.generator.pyfloat(left_digits=4, right_digits=2, positive=True)
# Function to generate user_id
def generate_user_id(name):
    user_id = re.sub(r'\s+', '', name).lower()
    user_id += str(random.randint(1000, 9999))
    user_id = re.sub(r"[^a-zA-Z0-9]", '', user_id)[:30]
    return user_id

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (
            any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in string.punctuation for char in password) and
            not password.isdigit() and
            not password.isalpha()
        ):
            return password

# Function to generate email from name
def generate_email(name):
    simple_name = re.sub(r'\W+', '', name).lower()
    domain = random.choice(['@yahoo.com', '@gmail.com'])
    email = f"{simple_name}{random.randint(10, 99)}{domain}"
    return email

# Create a new Faker instance
fake = Faker()

# Add the FinancialProvider to faker object
fake.add_provider(FinancialProvider)

# Add the ExtendedFinancialProvider to faker object
fake.add_provider(ExtendedFinancialProvider)

# Create Expense Categories
def generate_category_description(category):
    category_descriptions = {
        'Food': ['Restaurant', 'Grocery', 'Food'],
        'Clothing': ['Clothing', 'Apparel', 'Fashion'],
        'Entertainment': ['Movies', 'Concert', 'Entertainment'],
        'Utilities': ['Utilities', 'Bills', 'Electricity', 'Water'],
        'Rent': ['Rent', 'Housing'],
        'Other': ['Miscellaneous', 'Other']
    }

    return fake.random_element(category_descriptions.get(category, ['Random expense']))

# Generate data for 100 users with expenses
for _ in range(10):
    name = fake.name().split()
    first_name = name[0]
    last_name = ' '.join(name[1:])
    username = generate_user_id(first_name)
    email = generate_email(first_name)
    password = generate_random_password()

    # Create user and set password correctly
    user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()
    print(f"Generated Password for {username}: {password}")
    user_profile = UserProfile.objects.create(
        user=user,
        routing_number=fake.routing_number(),
        bank_account_number=fake.bank_account_number(),
        balance=fake.bank_balance(),
        credit_card_debt=fake.credit_card_debt(),
        mortgage_value=fake.mortgage(),
        car_loan=fake.car_loan(),
        student_loan=fake.student_loan(),
        salary=fake.salary(),
        cryptocurrency_balance=fake.cryptocurrency_balance(),
        stocks_value=fake.stocks_value(),
        bonds_value=fake.bonds_value(),
    )

    for _ in range(5):
        category_name = fake.random_element(['Food', 'Clothing', 'Entertainment', 'Utilities', 'Rent', 'Other'])
        amount = fake.random_int(min=5, max=100)
        description = generate_category_description(category_name)
        try:
            category = ExpenseCategory.objects.get(name=category_name)
        except ObjectDoesNotExist:
            category = ExpenseCategory.objects.create(name=category_name)

        expense = Expense.objects.create(
            user=user,
            amount=amount,
            category=category,
            description=description,
            date=fake.date_this_month()
        )

    # Create other bank accounts
    for _ in range(4):  # Assuming you want to create 2 additional bank accounts
        account_type = fake.account_type()
        bank_name = fake.bank_name()
        other_account_number = fake.other_bank_account_number()
        other_account_balance = fake.other_bank_balance(user_profile.balance)

        # Save the other bank account details to the database
        other_account = OtherBankAccount.objects.create(
            user_profile=user_profile,
            account_type=account_type,
            bank_name=bank_name,
            account_number=other_account_number,
            account_balance=other_account_balance
        )

