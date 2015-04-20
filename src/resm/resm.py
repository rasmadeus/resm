from flask import Flask
from flask import jsonify

def create_fake_db(number_of_res):
    return [["r{id}".format(id=i), None] for i in range(number_of_res)]

def get_options():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-n", "--number", type="int", default=10, help="Number of resources.")
    parser.add_option("-p", "--port", type="int", default=5000, help="Web service port.")
    return parser.parse_args()

options = get_options()[0].__dict__
app = Flask(__name__)
data = create_fake_db(options["number"])

def get_allocated():
    return {value[0]: value[1] for value in data if value[1] is not None}

def get_deallocated():
    return [value[0] for value in data if value[1] is None]

@app.route("/")
def index():
    return "Hello world" 

@app.route('/list', methods=['GET'])
def get_list():
    return jsonify({"allocated": get_allocated(), "deallocated": get_deallocated()}), 200

@app.route('/reset', methods=['GET'])
def reset():
    for value in data:
        value[1] = None
    return "No content", 204
   
@app.errorhandler(404)
def bad_request(error):
    return "Bad request", 400

if __name__ == '__main__':
    app.run(port=options["port"], debug=True)    