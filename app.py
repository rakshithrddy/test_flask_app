from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    # Render the home page template and pass in the list of cars
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=False)
