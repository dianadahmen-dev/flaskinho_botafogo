from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')  

@app.route('/policies')
def policies():
    return render_template('policies.html')

@app.route('/socialmedia')
def socialmedia():
    return render_template('socialmedia.html')

if __name__ == '__main__':
    app.run(debug=True)
