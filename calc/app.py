from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def add():
    """Adds a and b and returns result as the body."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(a + b)


@app.route("/sub")
def sub():
    """Same, subtracting b from a."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(a - b)


@app.route("/mult")
def mult():
    """multiplying a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(a * b)


@app.route("/div")
def div():
    """Same, dividing a by b."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return str(a / b)


@app.route("/math/<operation>")
def math(operation):
    """Basic math operations."""

    def add(a, b):
        """Add a and b."""

        return a + b

    def sub(a, b):
        """Substract b from a."""

        return a - b

    def mult(a, b):
        """Multiply a and b."""

        return a * b

    def div(a, b):
        """Divide a by b."""

        return a / b

    operations = {"add": add, "sub": sub, "mult": mult, "div": div}

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = operations[operation](a, b)

    return str(result)
