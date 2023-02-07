from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submissions
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Do something with the form data, e.g. send an email
        return 'Form submitted successfully!'
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
