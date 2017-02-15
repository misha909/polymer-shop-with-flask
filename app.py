from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')
#app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:the_path>')
def all_other_routes(the_path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100, debug=True)
