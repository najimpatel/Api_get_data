from flask import Flask

import requests

app = Flask(__name__)



@app.route("/book-info")
def show_book_info():
    """Return page about book."""

    isbn = requests.args["isbn"]

    resp = requests.get("http://some-book-api.com/search",
        params={"isbn": isbn})

    book_data = resp.json()

    print(book_data)

     # using the APIs JSON data, return that to browser
    # return jsonify(book_data)

    # using the APIs JSON data, render full HTML page
    # return render_template("book_info.html", book=book_data)



if __name__ == '__main__':
    app.run(debug=True)
