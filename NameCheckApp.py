from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # getting username from the index html using request
    lower_letter = False
    upper_letter = False
    num_end = False
    username = request.args.get('username')

    # Check the user name for the 3 requirements.
    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    report = lower_letter and upper_letter and num_end

    return render_template('report.html', report = report, lower = lower_letter, upper = upper_letter, num= num_end)

    # Return the information to the report page html.
    return render_template('report.html', username = username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('06-404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)