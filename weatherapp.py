from flask import Flask, render_template, request #this creates website objects


app = Flask("Website")

@app.route("/home")
def home(): 
    some_variable = "malcolm"
    letters = list(some_variable)
    mylist=[1,2,3,4,5]
    userlogedin = True
    return render_template("tutorial.html",my_variable=some_variable, letters=letters,mylist=mylist,userlogedin=userlogedin)


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/signup/")
def signup():
    return render_template("signup.html")

@app.errorhandler(404)
def page_not_found(e):
    return  render_template('404.html'), 404

@app.route("/thankyou/")
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template("thankyou.html", first=first,last=last)

@app.route("/api/v1/<station>/<date>")
def api(station,date):
    temperature = 23
    return { "station": station,
            "date": date,
            "temperature": temperature}

app.run(debug=True)
