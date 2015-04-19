from flask import Flask

def create_fake_db(number_of_res):
    return [{"r{id}".format(id=i): None} for i in range(number_of_res)]

def get_options():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-n", "--number", type="int", default=10, help="Number of resources.")
    parser.add_option("-p", "--port", type="int", default=5000, help="Web service port.")
    return parser.parse_args()

options = get_options()[0].__dict__
app = Flask(__name__)
data = create_fake_db(options["number"])

@app.route("/")
def index():
    return "Hello world"    

if __name__ == '__main__':
    app.run(port=options["port"])    