from flask import Blueprint, render_template, request
from scanner import sql_injection, xss, directory_traversal

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    results = {
        'sql_injection': sql_injection.scan(url),
        'xss': xss.scan(url),
        'directory_traversal': directory_traversal.scan(url)
    }
    return render_template('index.html', results=results)
