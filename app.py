from flask import Flask
from flask import render_template
from flask import request
from credit_card import CreditCardValidator
from gas_station import InputParser, Router, Car

app = Flask(__name__)

TEMPATE_NAME = 'template.html'


@app.route('/')
@app.route('/credit-card', methods=['GET', 'POST'])
def credit_card():
    # just render a form
    page_name = "credit_card_validation"
    title = "Credit Card Validation"
    form_action = '/credit-card'
    if request.method == 'GET':
        return render_template(
            TEMPATE_NAME,
            page_name=page_name,
            title=title,
            form_action=form_action
        )
    else:
        # validate file
        try:
            user_input = request.files['input-file']
            validator = CreditCardValidator(user_input)
            result = validator.validate()
        except ValueError:
            result = (u'Invalid File',)
        return render_template(
            TEMPATE_NAME,
            page_name=page_name,
            title=title,
            form_action=form_action,
            result=result
        )


@app.route('/gas-station', methods=['GET', 'POST'])
def gas_station():
    # just render a form
    page_name = "gas_station"
    title = "Gas Station"
    form_action = '/gas-station'
    if request.method == 'GET':
        return render_template(
            TEMPATE_NAME,
            page_name=page_name,
            title=title,
            form_action=form_action
        )
    else:
        # validate file
        try:
            user_input = request.files['input-file']
            results = []
            router = Router()
            inputs = InputParser(user_input).inputs
            for _input in inputs:
                route, start_index = router.trace_route(_input.gas_stations)
                car = Car()
                try:
                    car.traverse_route(route)
                    # convert list position(starts in 0) to
                    #   input position (starts in 1)
                    results.append(start_index + 1)
                except RuntimeError:
                    results.append('impossible')
        except ValueError:
            results = (u'Invalid File',)
        return render_template(
            TEMPATE_NAME,
            page_name=page_name,
            title=title,
            form_action=form_action,
            result=results
        )
