from flask import Flask, request, jsonify
import random


app = Flask(__name__)

@app.route('/getRandomNumber')
def randomNumber():
    num = str(random.randint(0,900000))
    #num = str(random.random())
    output = "Benvenuti!" + "\n" + " Numero random: " + num
    return output

@app.route('/getSquare/<number>')
def square(number):
    num = str(number)
    result = str(int(number) * int(number))
    return "Il quadrato del numero " + num + " è:  " + result