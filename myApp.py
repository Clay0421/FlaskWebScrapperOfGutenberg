import flask, WebScrappingPractice2
from WebScrappingPractice2 import Gutenburg
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

#variables from webscapper 



@app.route('/')
@app.route('/home')
def home():
    bookAuthor, bookUrl, bookTitle = Gutenburg()
    def aboutRedirect():
        return redirect(url_for("about"))
    return render_template("home.html", bookTitle=bookTitle, bookUrl=bookUrl, bookAuthor=bookAuthor)

@app.route('/about')
def about():
    def homeRedirect():
        return redirect(url_for("home"))
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)