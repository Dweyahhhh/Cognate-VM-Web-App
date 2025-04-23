from flask import Flask, render_template, request

app = Flask(__name__)

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
        email = request.form.get("email", "")
        message = request.form.get("message", "")
        return f"""
        <html>
        <head>
            <title>Thank You</title>
            <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css
' rel='stylesheet'>
            <style>
                body {{
                    background-color: #e6ecff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    font-family: 'Segoe UI', sans-serif;
                }}
                .thank-box {{
                    text-align: center;
                    padding: 30px;
                    background-color: #f0f4ff;
                    border: 2px solid #4169e1;
                    border-radius: 20px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                }}
                h1 {{
                    color: #4169e1;
                    margin-bottom: 20px;
                }}
                .btn-blue {{
                    background-color: #4169e1;
                    color: white;
                    border: none;
                    margin: 5px;
                    padding: 10px 20px;
                    border-radius: 10px;
                }}
                .btn-blue:hover {{
                    background-color: #365acb;
                }}
            </style>
        </head>
        <body>
            <div class="thank-box">
                <h1>💙 Thank you, {name}! 😊</h1>
                <p>💌 We received your message.</p>
                <a href="/contact" class="btn btn-blue">Send Another</a>
                <a href="/" class="btn btn-blue">Go to Home</a>
            </div>
        </body>
        </html>
        """
    return render_template("contact.html")

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)