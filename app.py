from flask import render_template
from flask import Flask
import json, os

app = Flask(__name__)

@app.route('/')
def home():
    user = {'name': 'angel', 'username': 'angelvargas'}
    posts = {}
    return render_template('home.html', title='.: Scurri -- Technical assignment :. Menu', user=user, posts=posts, g=None);


@app.route('/multiples')
def multiples():
    def multiples_three_five(below):
        yield (['ThreeFive' if n % 3 == 0 and n % 5 == 0 else 'Three' if n % 3 == 0 else
            'Five' if n % 5 == 0 else n for n in range(1, below + 1)])

    multiples_ = next(multiples_three_five(100))

    return render_template('multiples.html', title='Multiples', multiples=multiples_)


@app.route('/postal-codes')
def postal_codes():
    def format_codes():
        filename = os.path.join(app.static_folder, 'storage/postal_codes.json')
        with open(filename) as postal_codes:
            data = json.load(postal_codes)
        return data

    return render_template('postal-codes.html', title='UK - Postal Codes', postalcodes=format_codes())


if __name__ == '__main__':
    app.run()
