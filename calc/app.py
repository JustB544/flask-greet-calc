from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
}

@app.route("/<operation>")
def do_operation(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    _return = operators[operation](a, b)
    return str(_return)

@app.route("/math/<operation>")
def do_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    _return = operators[operation](a, b)
    return str(_return)


