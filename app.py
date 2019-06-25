from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'pipoca'
df = ...

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/presentation_data')
def present():
    return render_template('fim.html', renda=float(session['income']), familia=float(session['family']), genero=int(session['gender']), race=int(session['ethnicity']), escolaridade=int(session['graduation']), estado=int(session['state']))
#-------------------------------------fazer este comando caso queira fazer um 'if/else' no arquivo fim.html

@app.route('/form', methods=['POST'])
def create_information():
    income = session['income'] = request.form['income']

    ethnicity = session['ethnicity'] = request.form.get('ethnicity')
    gender = session['gender'] = request.form.get('gender')
    family = session['family'] = request.form['family']
    state = session['state'] = request.form.get('state')
    graduation = session['graduation'] = request.form.get('graduation')

    # Filtra o dataframe
    #if gender != 0:
    #        df = df[df.gender == gender]

    return redirect(url_for('present'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
