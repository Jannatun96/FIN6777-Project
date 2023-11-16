from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd

# Initialize Flask Server
app = Flask(__name__)

# Initialize API
api = Api(app)

# Dataset
bank1_path = "/Users/fabianrichard/Documents/Bank1.csv"
bank2_path = "/Users/fabianrichard/Documents/Bank2.csv"
bank3_path = "/Users/fabianrichard/Documents/Bank3.csv"
all_accts_path = ""

@app.route('/')
def home():
    return 'WealthWise'

# Aggregate users' financial data
class financials(Resource):
    # Get data from users' accounts
    def get(self):
        bank1 = pd.read_csv(bank1_path)
        bank1 = bank1.to_dict()
        bank2 = pd.read_csv(bank2_path)
        bank2 = bank2.to_dict()
        bank3 = pd.read_csv(bank3_path)
        bank3 = bank3.to_dict()
        return {'Bank 1': bank1, 
                'Bank 2': bank2,
                'Bank 3': bank3}, 200
    
    # Allow users to input data
    # def post(self):
        acct_data = pd.read_csv(acct_data_path)
        acct_data = acct_data.to_dict()
        parser = reqparse.RequestParser()
        parser.add_argument('Date', required=False)
        parser.add_argument('Transaction Amt', required=False)
        return {}
    
    # def delete(self):
        acct_data = pd.read_csv(acct_data_path)
        acct_data = acct_data.to_dict()
        parser = reqparse.RequestParser()
        parser.add_argument('transaction #', required=True, type=int)
        args = parser.parse_args()

        if args['transaction #'] in acct_data['transaction #']:
            acct_data = acct_data[acct_data['transaction #'] != args['transaction #']]
            acct_data.to_csv(acct_data_path, index=False)
            return {'Transaction Deleted'}, 200
        else:
            return {'Transaction Not Found'}, 404


# Endpoints
api.add_resource(financials, '/financials')

# Run Server
if __name__ == "__main__":
    app.run(debug=True)