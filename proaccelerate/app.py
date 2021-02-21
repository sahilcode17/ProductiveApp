from flask import Flask, render_template, request, jsonify
from drowsee import mainn
app = Flask(__name__)
time=0


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form = request.form
        global time
        time = form['me']
        print(time)
        return render_template('home.html')
    return render_template('index.html')

  

@app.route('/camera')
def camera():
    return render_template('camera.html',camera_trigger=camera_trigger)

@app.route('/home' , methods=["GET", "POST"])
def home():
    if request.method == "POST":
        form = request.form
        my_time = form['my_time']
        return render_template('yourway.html',my_time=my_time,time=time)
    return render_template('home.html')

@app.route('/ourway')
def ourway():
    return render_template('ourway.html',time=time)


@app.route('/yourway')
def yourway():
    return render_template('yourway.html')


@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = { 'value' :  mainn()}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200