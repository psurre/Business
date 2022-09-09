from flask import  ( Flask, g, render_template, session, jsonify, make_response )
import os, logging, constants
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG, encoding = "UTF-8", filename=constants.LOG_FILE)

def start():
    app = Flask(__name__)
    # Gestion de la session
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    @app.route("/")
    def index():
        logging.debug(f"Accès à la page d'index")
        return render_template('index.html')
    return app