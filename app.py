from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "My super key is nothing"


# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

#create form
class NameForm(FlaskForm):
    name = StringField("User Name", validators= [DataRequired()])
    submit = SubmitField("Submit")

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = name.form.data
        name.form.data = ''

    return render_template("name.html", form = form, name = name)

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/user/<name>')
def user(name):
    bold="This is the <strong>bold</strong> text"
    return render_template("user.html", user_name=name, bold=bold)

#Create custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Create internal server error page
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == 'main':
    app.run(debug=True)
