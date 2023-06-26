import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
    return "<h1> My name is Kristofferson</h1>"

app.run()

