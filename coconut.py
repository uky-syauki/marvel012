from flask import FLask

app = Flask(__name__)

@app.route('/')
def index():
	return "Bismillah"


if __name__ == "__main__":
	app.run()
