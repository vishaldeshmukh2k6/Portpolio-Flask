from flask import Flask, render_template, request, flash, redirect, url_for
from model import db, Contact

app = Flask(__name__)
app.secret_key = "supersecretkey"


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://vishaldeshmukh2k:Vishal@123@vishaldeshmukh2k6.mysql.pythonanywhere-services.com/vishaldeshmukh2k$blog_app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def project():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        contact_entry = Contact(name=name, email=email, message=message)
        db.session.add(contact_entry)
        db.session.commit()

        flash("Your message has been sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")

@app.route("/messages")
def view_messages():
    messages = Contact.query.all()
    return render_template("messages.html", messages=messages)

@app.route("/team")
def team():
    return render_template("team.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
