from flask import  ( Flask, g, render_template, session, jsonify, make_response )
import os, logging, constants, toolbox
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG, encoding = "UTF-8", filename=constants.LOG_FILE)
from Operation import Operation
from Compte import Compte

def start():

    compte: Compte = toolbox.lireFichierCSV()
    if compte is not None:
        compte.afficherCompte()

    app = Flask(__name__)
    # Gestion de la session
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    @app.route("/")
    def index():
        session.pop('kmsparsem', None)
        session.pop('kmsparjour', None)
        logging.debug(f"Accès à la page d'index")
        return render_template('index.html', initdata=compte)

    @app.route("/detail")
    def detail():
        logging.debug(f"Accès à la page de détail")
        return render_template('detail.html', initdata=compte)
    
    @app.route("/skoda")
    def skoda():
        if ('kmsparsem' in session):
            g.kmsparsem = session.get('kmsparsem')
        if ('kmsparjour' in session):
            g.kmsparjour =session.get('kmsparjour')
        data = {}
        logging.debug(f"Accès à la page Skoda")
        data = toolbox.joursRestants().copy()
        return render_template('skoda.html', data=data)
    
    @app.route('/calculerkms/<valeur>', methods=['POST'])
    def calculerkms(valeur):
        data = {}
        kmsrestants = constants.KM_MAX - int(valeur)
        data = toolbox.joursRestants().copy()
        semaines = float(int(data['daytolimit']) / 7)
        kmsparsem = round (float(kmsrestants / semaines), 2)
        kmsparjour = round (float(kmsrestants / int(data['daytolimit'])), 2)
        session['kmsparsem'] = kmsparsem
        session['kmsparjour'] = kmsparjour
        versFetch = make_response(jsonify({"message":"everythingisfine!"}), 200)
        return versFetch

    return app
