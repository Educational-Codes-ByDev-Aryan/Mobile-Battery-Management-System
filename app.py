from flask import Flask, render_template, request
from mobile import Mobile

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    mobile_data = None

    if request.method == "POST":

        model = request.form["model"]
        battery = int(request.form["battery"])
        charge = int(request.form["charge"])
        company = request.form["company"]

        # Create Mobile Object
        mobile = Mobile(model, battery)

        # Change Company
        Mobile.change_company(company)

        # Charge Battery
        mobile.charge_battery(charge)

        # Send data to HTML
        mobile_data = mobile.get_details()

    return render_template("index.html", mobile=mobile_data)


if __name__ == "__main__":
    app.run(debug=True)