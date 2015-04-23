from flask import Flask
from flask import jsonify
from flask import Response
from model import FakeDataBase
from tools import get_options


options = get_options()
app = Flask(__name__)
data = FakeDataBase(options["number"])

@app.route("/")
def index():    
    return "Hello world", 200

@app.route('/list', methods=['GET'])
def get_list():
    return jsonify({"allocated": data.get_allocated(), "deallocated": data.get_deallocated()}), 200

@app.route('/reset', methods=['GET'])
def reset():
    return Response(status=204)
   
@app.errorhandler(404)
def bad_request(error):
    return "Bad request", 400

@app.route('/allocate/<owner>', methods=['GET'])
def allocate_res(owner):
    return ("Created", 201) if data.allocate(owner) else ("Out of resources", 503)

if __name__ == '__main__':
    app.run(port=options["port"], debug=True)    