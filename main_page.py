from flask import Blueprint, render_template


main_pages = Blueprint('main_pages', __name__, template_folder="templates")


@main_pages.route('')
def main_page():
    return render_template("index.html")

