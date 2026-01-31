from flask import Flask, request, render_template, redirect, make_response
import jwt
import datetime

app = Flask(__name__)

SECRET_KEY = "secret123" 

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")


        payload = {
            "user": username,
            "role": "user",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        resp = make_response(redirect("/dashboard"))
        resp.set_cookie("token", token)
        return resp

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    token = request.cookies.get("token")

    if not token:
        return redirect("/")

    try:
        
        decoded = jwt.decode(token, SECRET_KEY, algorithms=None, options={"verify_signature": False})
    except:
        return "Invalid token"

    if decoded.get("role") != "admin":
        return "<h3>Access denied. Admin only.</h3>"

    with open("flag.txt") as f:
        flag = f.read()

    return render_template("dashboard.html", flag=flag)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9002)
