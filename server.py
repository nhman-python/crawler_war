import random
import string
import time
from datetime import datetime

from flask import Flask, render_template_string

app = Flask(__name__)


def generate_title():
    titles = [
        "Python Basics",
        "Data Types in Python",
        "Control Flow and Loops",
        "Functions and Modules",
        "File Handling in Python",
        "Object-Oriented Programming",
        "Exception Handling",
        "Working with Databases in Python",
        "Python Web Development",
        "Python Data Science"
    ]
    return random.choice(titles)


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_html():
    links = [f'<a href="{generate_random_string(10)}">{generate_title()}</a><br>' for _ in range(8)]
    a_tags = '\n'.join(links)
    html_normal = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <title>learn python</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          margin: 20px;
        }}
        h1 {{
          color: #333333;
          text-align: center;
        }}
        a {{
          color: #007bff;
          text-decoration: none;
        }}
        a:hover {{
          text-decoration: underline;
        }}
      </style>
    </head>
    <body>
      <h1>Welcome to the python basic!</h1>
      <p>Explore the following topics:</p>
      {a_tags}
      <footer>
        &copy; {datetime.now().year} python-learn Website. All rights reserved.
      </footer>
    </body>
    </html>
    """

    return html_normal


@app.route('/')
@app.route('/<path:path>')
def index(path=None):
    html_random = generate_html()
    time.sleep(0.2)
    return render_template_string(html_random)


if __name__ == '__main__':
    app.run(debug=False)
