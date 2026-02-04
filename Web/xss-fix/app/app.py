from flask import Flask, request, render_template

app = Flask(__name__)


BLACKLIST = ["<script", "</script"]

def sanitize(s):
    for b in BLACKLIST:
        s = s.replace(b, "")
    return s

@app.route("/", methods=["GET", "POST"])
def index():
    comments = []
    name = ""
    comment = ""

    if request.method == "POST":
        name = request.form.get("name", "")
        comment = request.form.get("comment", "")
    else:
        name = request.args.get("name", "")
        comment = request.args.get("comment", "")

    if name or comment:
        comment = sanitize(comment)
        comments.append({
            "name": name,
            "comment": comment
        })

    return render_template("index.html", comments=comments)

@app.route("/admin")
def admin():
    with open("flag.txt") as f:
        flag = f.read()


    return f"""
    <script>
        document.cookie = "flag={flag}";
    </script>
    <h1>Admin Panel</h1>
    <p>Only admin can see this</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9014)
