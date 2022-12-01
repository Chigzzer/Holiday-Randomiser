from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/country", methods=['GET'])
def countryPage():
    print(request.args.get('country'))

    if not request.args.get('country'):
        country = 'Turkey'
    country = request.args.get('country')
    return render_template("country.html", country = country)