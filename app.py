from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        try:
            number = int(number)
            if number < 1 or number > 100:
                raise ValueError()
            return render_template('index.html', result=number)
        except ValueError:
            pass
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)

