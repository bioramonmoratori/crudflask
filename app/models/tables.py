from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    # Construtor
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
    
    # A forma como o objeto sera exibido ao ser pesquisado no banco de dados
    def __rep__(self, username):
        return "<User %r>" % (self.username) # Vai mostrar apenas o username de todos os dados encontrados

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id")) # Precisa referenciar um id da tabela usuarios

    user = db.relationship("User", foreign_keys=user_id) # Relacionamento entre as tabelas

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __rep__(self, content):
        return "<Post %r>" % (self.id)

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", foreign_keys=user_id)
    follower = db.relationship("User", foreign_keys=follower_id)