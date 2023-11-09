from faker import Faker
from faker.providers import BaseProvider
import random
import re
import csv

class FinancialProvider(BaseProvider):
    def bank_account_number(self):
        # Generate random bank acc number
        length = random.randint(8, 12)  # Choose a length between 8 and 12
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
    
    def investment_portfolio_value(self):
        # Generate a random value for an investment portfolio
        return self.generator.pyfloat(left_digits=5, right_digits=2, positive=True)

class ExtendedFinancialProvider(FinancialProvider):
    def other_bank_account_number(self):
        # Generate a different bank account number
        return self.generator.iban()

    def other_bank_balance(self, original_balance):
        # Generate a bank balance for another bank
        variation_percentage = random.uniform(-0.3, 0.3)  # can decrease/increase by 30%
        return original_balance * (1 + variation_percentage)

# Function to generate user_id
def generate_user_id(name):
    # Remove spaces and lowercase the name for the user_id
    user_id = re.sub(r'\s+', '', name).lower()
    # Add a random number to ensure uniqueness
    user_id += str(random.randint(1000, 9999))
    return user_id

# Function to generate email from name
def generate_email(name):
    # Remove all non-alphanumeric characters from name
    simple_name = re.sub(r'\W+', '', name).lower()
    # Randomly choose between two email domains
    domain = random.choice(['@yahoo.com', '@gmail.com'])
    # Concatenate with a random number and a chosen domain
    email = f"{simple_name}{random.randint(10, 99)}{domain}"
    return email

# Create a new Faker instance
fake = Faker()

# Add the FinancialProvider to faker object
fake.add_provider(FinancialProvider)

# Add the ExtendedFinancialProvider to faker object
fake.add_provider(ExtendedFinancialProvider)

# Generate data for 100 users
users = []
for _ in range(100):
    name = fake.name()
    user = {
        'user_id': generate_user_id(name),
        'name': name,
        'email': generate_email(name),
        'address': fake.address(),
        'routing_number': fake.routing_number(),
        'bank_account_number': fake.bank_account_number(), 
        'bank_balance': fake.bank_balance(),
        'credit_card_debt': fake.credit_card_debt(),
        'mortgage_value': fake.mortgage(),
        'car_loan': fake.car_loan(),
        'student_loan': fake.student_loan(),
        'investment_portfolio_value':fake.investment_portfolio_value()
    }
    users.append(user)

# Extend user data with accounts at different financial institutions
for user in users:
    user['other_account_number'] = fake.other_bank_account_number()
    user['other_bank_balance'] = fake.other_bank_balance(user['bank_balance'])

# Iterate over users to see the generated data
for user in users:
    print(user)
    
# Export as csv file
filename = "user_financial_data.csv"

# Open the file in write mode
with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=users[0].keys())

    # Write the header (field names)
    writer.writeheader()

    # Write the user data
    for user in users:
        writer.writerow(user)