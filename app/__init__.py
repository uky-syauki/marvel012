from flask import FLask

app = Flask(__name__)

@app.route('/')
def index():
	return "Bismillah"


