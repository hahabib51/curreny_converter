from flask import Flask, render_template, request, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'hush-little-one'

# redirect debugging false
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

# Setup forex python
rates = CurrencyRates()
codes = CurrencyCodes()


@app.route('/')
def get_home():
    """ Display the home page with the currency form """

    return render_template('index.html')


@app.route('/error')
def get_error():
    """ Display the home page with error message """

    msg = session['msg']
    return render_template('error.html', msg=msg)


@app.route('/convert', methods=['POST'])
def convert_currency():
    """ Convert the currencies from the currency form """

    from_curr = request.form['from-curr'].upper()
    to_curr = request.form['to-curr'].upper()

    # Error handling if the amount is not a number
    try:
        amount = float(request.form['amount'])
    except ValueError:
        session['msg'] = 'Not a valid amount.'
        return redirect('/error')

    # Checking to see which currency is the one with the issue and updating the message
    try:
        result = rates.convert(from_curr, to_curr, amount)
    except RatesNotAvailableError:

        if codes.get_symbol(from_curr) is None:
            session['msg'] = f'Not a valid code: {from_curr}'
        else:
            session['msg'] = f'Not a valid code: {to_curr}'
        return redirect('/error')

    symbol = codes.get_symbol(to_curr)
    session['result'] = result
    session['symbol'] = symbol
    return redirect('/result')


@app.route('/result')
def get_result():
    """ Display the result of the conversion """

    result = session['result']
    formatted_float = "{:.2f}".format(result)
    symbol = session['symbol']

    return render_template('result.html', result=formatted_float, symbol=symbol)


# Needed for Replit flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)