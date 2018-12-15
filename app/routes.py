from app import app
import RPi.GPIO as GPIO
OUTPUT_PIN = 23

from flask import render_template


@app.route('/', methods=['GET', 'POST'])
@app.route('/high', methods=['GET', 'POST'])
def on():
    GPIO.output(OUTPUT_PIN, GPIO.HIGH)
    return "set to high"


@app.route('/low', methods=['GET', 'POST'])
def off():
    GPIO.output(OUTPUT_PIN, GPIO.LOW)
    return "set to low"


@app.route('/uni-bonn/raum1049/temp', methods=['GET', 'POST'])
def temperature():
    return "Hello world"


