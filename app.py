from flask import Flask, render_template, request
import calculator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        operation = request.form["operation"]
        if operation == "add":
            result = calculator.add(a, b)
        elif operation == "subtract":
            result = calculator.subtract(a, b)
        elif operation == "multiply":
            result = calculator.multiply(a, b)
        elif operation == "divide":
            result = calculator.divide(a, b)
    return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)
