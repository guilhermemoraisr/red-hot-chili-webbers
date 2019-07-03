from flask import Flask, render_template, request, session, redirect, url_for
from data.dados import *

app = Flask(__name__)
app.secret_key = 'pipoca'

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/presentation_data')
def present():
    percEdu = Escolaridade(int(session['graduation']))
    percGen = Genero()
    percEtn = Etnia()
    return render_template('fim.html', percGen=percGen, percEtn=percEtn, percEdu=percEdu, renda=float(session['income']), familia=float(session['family']),genero=int(session['gender']), race=int(session['ethnicity']), escolaridade=int(session['graduation']), estado=int(session['state']))
#-------------------------------------fazer este comando caso queira fazer um 'if/else' no arquivo fim.html

@app.route('/form', methods=['POST'])
def create_information():
    session['income'] = request.form['income']
    session['ethnicity'] = request.form.get('ethnicity')
    session['gender'] = request.form.get('gender')
    session['family'] = request.form['family']
    session['state'] = request.form.get('state')
    session['graduation'] = request.form.get('graduation')
    return redirect(url_for('present'))
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
