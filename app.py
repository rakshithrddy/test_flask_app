from flask import Flask, render_template

app = Flask(__name__)

# Define a list of cars
cars = [
    {'make': 'Toyota', 'model': 'Corolla', 'year': 2020},
    {'make': 'Honda', 'model': 'Civic', 'year': 2021},
    {'make': 'Ford', 'model': 'Mustang', 'year': 2019}
]

# Define a route for the home page
@app.route('/')
def home():
    # Render the home page template and pass in the list of cars
    return render_template('home.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)
