from flask_login import UserMixin

class User(UserMixin):
    """Classe représentant un utilisateur connecté via le LDAP.

        :param UserMixin: Informations sur l'utilisateur.
        :type UserMixin: flask_login

    """
    def __init__(self, dn, username, data, active):
        self.dn = dn
        self.username = username
        self.data = data
        self.enabled = active

    def __repr__(self):
        return self.dn

    def get_id(self):
        #This method must return a str that uniquely identifies this user, and can be used to load the user from
        # the user_loader callback. Note that this must be a str - if the ID is natively an int or some other type,
        # you will need to convert it to str.
        return self.username
    
    def get_username(self):
        return self.username
    
    def get_data(self):
        return self.data
    
    def is_authenticated(self):
        # This property should return True if the user is authenticated, i.e. they have provided valid credentials. 
        # (Only authenticated users will fulfill the criteria of login_required.)
        return True
    
    def is_active(self):
        #This property should return True if this is an active user - in addition to being authenticated, they also have activated 
        # their account, not been suspended, or any condition your application has for rejecting an account. 
        # Inactive accounts may not log in (without being forced of course).
        return self.enabled
    
    def is_anonymous(self):
        #This property should return True if this is an anonymous user. (Actual users should return False instead.)
        return False