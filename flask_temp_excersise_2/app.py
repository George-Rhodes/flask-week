from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')


@app.route('/the_boys')
def the_boys():
	return render_template('the_boys.html', users = ["ben", "harry", "bob", "jay", "matt", "bill"])




if __name__ == "__main__":
    app.run(host= '0.0.0.0',debug=True)
