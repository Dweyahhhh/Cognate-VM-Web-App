from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        return f"<h1 style='color:#4169E1;'>Thank you, {name}!</h1><p>Your message has been received.</p><a href='/'>Back</a>"
    return render_template("contact.html")

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000