from app import app
from flask import request, Response

from app.tools import set_pin_state, get_pin_state, get_cpu_temperature
OUTPUT_PIN = 13


pin_description = {
    1: 'On',
    0: 'Off'
}


@app.route('/', methods=['GET'])
def index():
    msg = '@prefix dcterms: <http://purl.org/dc/terms/>.\n' \
          '@prefix ldp: <http://www.w3.org/ns/ldp#>.\n\n' \
          '<http://semantic-web-lab.org/c1/>\n' \
          '\ta ldp:BasicContainer;\n' \
          '\tdcterms:title "Raspberry Pi container";\n' \
          '\tldp:contains </uni-bonn/devices/external>, ' \
          '</uni-bonn/devices/raspberry/temperature>.'
    return Response(response=msg, status=200, content_type='text/turtle')


@app.route('/uni-bonn/devices/external', methods=['GET', 'PUT'])
def pin_state():
    if request.method == 'PUT':
        app.logger.debug('this is post request to {}'.format(request.base_url))
        if not request.data:
            return "Wrong query", 401
        data = str(request.data)
        if '<ns1:hasEffect>TurnOn</ns1:hasEffect>' in data:
            set_pin_state(OUTPUT_PIN, 1)
            r = Response(response='OK', status=200)
            app.logger.debug(
                'Turning on the pin {}'.format(OUTPUT_PIN)
            )
            return r
        if '<ns1:hasEffect>TurnOff</ns1:hasEffect>' in data:
            set_pin_state(OUTPUT_PIN, 0)
            r = Response(response='OK', status=200)
            app.logger.debug(
                'Turning off the pin {}'.format(OUTPUT_PIN)
            )
            return r

    if request.method == 'GET':
        # pin_state = 1
        pin_state = get_pin_state(OUTPUT_PIN)
        pin_msg = pin_description[pin_state]
        msg = "@prefix qudt: <http://qudt.org/schema/qudt#> . " \
              "@prefix ssn: <http://purl.oclc.org/NET/ssnx/ssn#> . " \
              "@prefix unit: <http://data.nasa.gov/qudt/owl/unit#> ." \
              "<> qudt:QuantityValue {}; qudt:unit unit:Boolean; " \
              "a ssn:ObservationValue . ".format(pin_msg)
        r = Response(response=msg, status=200, content_type='text/turtle')
        return r

    # return 400 if the post query is incorrect
    return 'Bad Request', 400


@app.route('/uni-bonn/devices/raspberry/temperature', methods=['GET'])
def temperature():
    # temp = 30
    temp = get_cpu_temperature()
    msg = "@prefix qudt: <http://qudt.org/schema/qudt#> . " \
          "@prefix ssn: <http://purl.oclc.org/NET/ssnx/ssn#> . " \
          "@prefix unit: <http://data.nasa.gov/qudt/owl/unit#> ." \
          "<> qudt:QuantityValue {}; qudt:unit unit:DegreeCelsius; " \
          "a ssn:ObservationValue . ".format(temp)
    r = Response(response=msg, status=200, content_type='text/turtle')
    return r

