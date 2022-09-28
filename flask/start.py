from curses import flash
from flask import  ( Flask, g, render_template, session, jsonify, make_response, send_from_directory, redirect, url_for )
from flask_login import LoginManager, login_required, login_user, UserMixin, logout_user
from flask_sqlalchemy import SQLAlchemy
import os, logging, constants, toolbox
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG, encoding = "UTF-8", filename=constants.LOG_FILE)
from Operation import Operation
from Compte import Compte
#from User import User
from LoginForm import LoginForm
from RegisterForm import RegisterForm
from flask_bcrypt import Bcrypt
from wtforms.validators import ValidationError

def start():
    loginManager = LoginManager()
    compte: Compte = toolbox.lireFichierCSV()
    if compte is not None:
        compte.afficherCompte()

    app = Flask(__name__, instance_path="/tobeanalyzed")
    
    # Gestion de la base de données
    bdd = SQLAlchemy(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bdd.db'
    
    # Gestion du chiffrement
    chiffre = Bcrypt(app)
    
    # Gestion de la session
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    # Gestion de l'authentification
    loginManager.init_app(app)
    loginManager.login_view = 'index'
    loginManager.login_message = "L'accès à cette ressource nécessite d'être authentifié"
    loginManager.login_message_category = "warning"
    
    # Classe Utilisateur
    class Utilisateur (bdd.Model, UserMixin):
        id = bdd.Column(bdd.Integer, primary_key=True)
        username = bdd.Column(bdd.String(20), nullable=False, unique=True)
        password = bdd.Column(bdd.String(80), nullable=False)
    
    @loginManager.user_loader
    def load_user(user_id):
        return Utilisateur.query.get(int(user_id))
    
    @app.route('/secret/<path:filename>')
    @login_required
    def secret(filename):
        return send_from_directory(
            app.instance_path,
            filename
        )
    
    @app.route("/")
    def index():
        # L'instruction ci-dessous ne doit être exécuté qu'une fois pour créer la BDD.
        # bdd.create_all()
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
        infos = []
        kmsrestants = constants.KM_MAX - int(valeur)
        data = toolbox.joursRestants().copy()
        semaines = float(int(data['daytolimit']) / 7)
        kmsparsem = round (float(kmsrestants / semaines), 2)
        kmsparjour = round (float(kmsrestants / int(data['daytolimit'])), 2)
        session['kmsparsem'] = kmsparsem
        session['kmsparjour'] = kmsparjour
        infos.append(data['daytolimit'])
        infos.append(kmsparjour)
        toolbox.persistKmsRestants(infos)
        versFetch = make_response(jsonify({"message":"everythingisfine!"}), 200)
        return versFetch
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = Utilisateur.query.filter_by(username=form.username.data).first()
            if user:
                if chiffre.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect(url_for('index'))
        return render_template('login.html', form=form)
    
    
    @ app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            # Controle de l'existence d'un utilisateur avec le même nom
            existing_user_username = Utilisateur.query.filter_by(
            username=form.username.data).first()
            if existing_user_username:
                # TODO A revoir ... Génère une erreur 500
                raise ValidationError('L\'utilisateur existe déjà, merci de choisir un autre nom.')

            hashed_password = chiffre.generate_password_hash(form.password.data)
            new_user = Utilisateur(username=form.username.data, password=hashed_password)
            bdd.session.add(new_user)
            bdd.session.commit()
            return redirect(url_for('login'))
        return render_template('register.html', form=form)
    
    @app.route('/logout', methods=['GET', 'POST'])
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    return app
