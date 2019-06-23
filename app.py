from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'pipoca'

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/presentation_data')
def present():
    return render_template('fim.html', renda=float(session['income']), familia=int(session['family']), genero=int(session['gender']), race=int(session['ethnicity']), estado=int(session['state']))
#-------------------------------------fazer este comando caso queira fazer um 'if/else' no arquivo fim.html

@app.route('/form', methods=['POST'])
def create_information():
    session['income'] = request.form['income']
    session['ethnicity'] = request.form.get('ethnicity')
    session['gender'] = request.form.get('gender')
    session['family'] = request.form['family']
    session['state'] = request.form['state']
    session['graduation'] = request.form['graduation']
    return redirect(url_for('present'))
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)
