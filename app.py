from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/page_1')
def page_1():
    return render_template("page_1.html")

@app.route('/page_2')
def page_2():
    return render_template("page_2.html")

@app.route('/page_3')
def page_3():
    return render_template("page_3.html")

@app.route('/page_4')
def page_4():
    return render_template("page_4.html")

@app.route('/page_5')
def page_5():
    return render_template("page_5.html")

@app.route('/page_6')
def page_6():
    return render_template("page_6.html")

@app.route('/page_7')
def page_7():
    return render_template("page_7.html")

@app.route('/page_8')
def page_8():
    return render_template("page_8.html")

if(__name__) == ('__main__'):
    app.run(debug=True)
