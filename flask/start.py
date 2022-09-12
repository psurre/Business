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
        logging.debug(f"Accès à la page d'index")
        return render_template('index.html', initdata=compte)

    @app.route("/detail")
    def detail():
        logging.debug(f"Accès à la page d'index")
        return render_template('index.html', initdata=compte)

    return app
