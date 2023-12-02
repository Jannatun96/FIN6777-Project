from rest_framework.response import Response # takes in python or serialized data and renders it as JSON
from rest_framework.decorators import api_view # api view decorator (necessary for function based views)
from .serializers import CombinedSerializer, CombinedPostSerializer # import serializer
import csv
from django.http import Http404


# API view decorator
@api_view(['GET']) # pass in GET method into list of allowed methods

# Create GET View
def getData(request, first_account_number, second_account_number):
    # Financial Institution Data
    user_data1 = '/Users/fabianrichard/user_financial_data1.csv'
    user_data2 = '/Users/fabianrichard/user_financial_data2.csv'

    # Open and read user_data1
    with open(user_data1, 'r') as file1:
        reader1 = csv.DictReader(file1)
        data1 = list(reader1)

    # Open and read user_data2
    with open(user_data2, 'r') as file2:
        reader2 = csv.DictReader(file2)
        data2 = list(reader2)

    # Filter for user's first bank account
    filter_account1 = [row for row in data1 if int(row['bank_account_number']) == int(first_account_number)]
    # Raise error if first account not found
    if not filter_account1:
        raise Http404("First Account Not Found")
   
    # Filter for user's second bank account
    filter_account2 = [row for row in data2 if row['bank_account_number'] == second_account_number]
    # Raise error if second account not found
    if not filter_account2:
        raise Http404("Second Account Not Found")
    
    # Get all variables associated with selected account number
    first_account_info = {key: value for key, value in filter_account1[0].items() if key != 'bank_account_number'}
    second_account_info = {key: value for key, value in filter_account2[0].items() if key != 'bank_account_number'}

    # Each bank balance
    balance1 = float(filter_account1[0]['bank_balance'])
    balance2 = float(filter_account2[0]['bank_balance'])

    # Combine Bank Balances
    total_bank_balance = balance1 + balance2
    
    # Serialize
    serializer = CombinedSerializer({
        'first_account_number': first_account_number,
        'first_account_info': first_account_info,
        'second_account_number': second_account_number,
        'second_account_info': second_account_info,
        'total_bank_balance': total_bank_balance
    })
    
    return Response(serializer.data) # Response object converts data to JSON

# API view decorator
@api_view(['GET', 'POST'])

# Create POST View
def addItem(request, first_account_number, second_account_number):
    # Financial Institution Data
    user_data1 = '/Users/fabianrichard/user_financial_data1.csv'
    user_data2 = '/Users/fabianrichard/user_financial_data2.csv'

    # Open and read user_data1
    with open(user_data1, 'r') as file1:
        reader1 = csv.DictReader(file1)
        data1 = list(reader1)

    # Open and read user_data2
    with open(user_data2, 'r') as file2:
        reader2 = csv.DictReader(file2)
        data2 = list(reader2)

    # Filter for user's first bank account
    filter_account1 = [row for row in data1 if int(row['bank_account_number']) == int(first_account_number)]
    # Raise error if first account not found
    if not filter_account1:
        raise Http404("First Account Not Found")
   
    # Filter for user's second bank account
    filter_account2 = [row for row in data2 if row['bank_account_number'] == second_account_number]
    # Raise error if second account not found
    if not filter_account2:
        raise Http404("Second Account Not Found")
    
    # Get all variables associated with selected account number
    first_account_info = {key: value for key, value in filter_account1[0].items() if key != 'bank_account_number'}
    second_account_info = {key: value for key, value in filter_account2[0].items() if key != 'bank_account_number'}
    
    if request.method == 'POST':
        # Input manual balance
        manual_balance = request.data.get('manual_balance', None)

        # Get user's other account info
        balance1 = float(filter_account1[0]['bank_balance'])
        balance2 = float(filter_account2[0]['bank_balance'])

        # Combine bank balances
        total_bank_balance = balance1 + balance2

        if manual_balance is not None:
            total_bank_balance += float(manual_balance)
        
        # Serialize response
        serializer = CombinedPostSerializer({
            'first_account_number': first_account_number,
            'first_account_info': first_account_info,
            'second_account_number': second_account_number,
            'second_account_info': second_account_info,
            'manual_balance': manual_balance,
            'total_bank_balance': total_bank_balance
        })

        return Response(serializer.data)
    
    # GET
    serializer = CombinedPostSerializer({
        'first_account_number': first_account_number,
        'first_account_info': first_account_info,
        'second_account_number': second_account_number,
        'second_account_info': second_account_info,
        'manual_balance': None,
        'total_bank_balance': float(filter_account1[0]['bank_balance']) + float(filter_account2[0]['bank_balance'])
    })

    return Response(serializer.data)
    
