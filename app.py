from flask import Flask, request, jsonify

app = Flask(__name__)

class LoanProcessor:
    def __init__(self):
        pass

    def process_loan(self, user_data):
        """
        Unique loan processing algorithm for each user.
        This is a dummy implementation, replace it with your actual algorithm.
        """
        age = user_data.get('age', 0)
        income = user_data.get('income', 0)

        if age >= 18 and income >= 50000:
            return {'status': 'approved', 'message': 'Congratulations! Your loan is approved.'}
        else:
            return {'status': 'rejected', 'message': 'Sorry, your loan application is rejected.'}

loan_processor = LoanProcessor()

@app.route("/", methods=["POST", "GET"])
def home():
    return "<h1>This is home page for loan app</h1>"

@app.route('/loan_process', methods=['POST'])
def process_loan():
    """
    API endpoint to process loan requests.
    """
    try:
        user_data = request.json  # Assuming JSON input
        result = loan_processor.process_loan(user_data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
