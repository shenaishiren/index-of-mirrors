#!.pyenv/bin/python

import os

curr_path = os.path.abspath(os.curdir)
os.environ["ACTOR_SETTINGS"] = os.path.join(curr_path, "settings.cfg")


from actor import app
from flask import request, redirect


# handle static files for debug
@app.before_request
def add_static():
    if not app.debug:
        return
    path = request.path
    if path == "/":
        return redirect("/static/index.html")


def main():
    app.run(host="127.0.0.1", debug=True)


if __name__ == '__main__':
    main()

