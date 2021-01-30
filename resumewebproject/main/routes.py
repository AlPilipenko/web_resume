from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request,send_from_directory


main = Blueprint('main', __name__)


@main.route('/home', methods=["GET","POST"])
@main.route('/', methods=["GET","POST"])
def home():
    return render_template('home.html',title="Home")





@main.route('/about', methods=["GET","POST"])
def about():
    return render_template('about.html', title="About")


@main.route('/work_experience', methods=["GET","POST"])
def work_experience():
    return render_template('work_experience.html',title="Work experience")


@main.route('/education', methods=["GET","POST"])
def education():
    return render_template('education.html',title="Education")


@main.route('/contact', methods=["GET","POST"])
def contact():
    return render_template('contact.html',title="Contact")

"<path:path>  -  convert to path(string)"
@main.route('/download/<path:filename>')
def download_cv(filename):
    path = 'static/'

    try:
        return send_from_directory(path, filename=filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)
