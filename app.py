
from flask import Flask, render_template, request
from tools import calculate_leave_days

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    start_date = ""
    end_date = ""

    if request.method == "POST":
        start_date = request.form.get("start_date", "").strip()
        end_date = request.form.get("end_date", "").strip()

        result = calculate_leave_days(start_date, end_date)

    return render_template(
        "index.html",
        result=result,
        start_date=start_date,
        end_date=end_date
    )


if __name__ == "__main__":
    app.run(debug=True)
