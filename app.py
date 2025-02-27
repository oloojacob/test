# Import the Flask class and request module from flask
from flask import Flask, request

# Create a Flask application instance
app = Flask(__name__)  # '__name__' is the name of the current module

# Define a route to add two numbers
@app.route('/add', methods=['GET'])
def add_numbers():
    """This function adds two numbers passed as query parameters."""
    
    # Get the 'num1' and 'num2' parameters from the URL query string
    num1 = request.args.get('num1', type=float)  # Convert to float
    num2 = request.args.get('num2', type=float)  # Convert to float
    
    # Check if both numbers are provided
    if num1 is None or num2 is None:
        return "Please provide both 'num1' and 'num2' parameters in the URL.", 400

    # Calculate the sum
    result = num1 + num2

    # Return the result as a string
    return f"The sum of {num1} and {num2} is {result}"

# Run the Flask app when the script is executed
if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask development server with debugging enabled
