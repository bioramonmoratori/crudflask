from app import db
from enum import Enum as EnumPy
from sqlalchemy import Enum
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


livro_autor = Table('livro_autor', db.Model.metadata,
    Column('livro_id', Integer, ForeignKey('livros.id')),
    Column('autor_id', Integer, ForeignKey('autores.id'))
)

class Estoque(EnumPy):
    DISPONIVEL = "DISPONIVEL"
    RESERVADO = "RESERVADO"
    VENDIDO = "VENDIDO"

class Livro(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), unique=False)
    isbn = db.Column(db.String(30), nullable=False)
    autores = relationship('Autor', secondary=livro_autor, back_populates='livros')
    dataDePublicacao = db.Column(db.Date, nullable=False)
    estoque = db.Column(Enum(Estoque), nullable=False, default=Estoque.DISPONIVEL)

    # Construtor
    def __init__(self, titulo, isbn, autores, dataDePublicacao, estoque):
        self.titulo = titulo
        self.isbn = isbn
        self.autores = autores
        self.dataDePublicacao = dataDePublicacao
        self.estoque = estoque
    
    # A forma como o objeto sera exibido ao ser pesquisado no banco de dados
    def __rep__(self, titulo):
        return "<Livro %r>" % self.titulo


class Autor(db.Model):
    __tablename__ = "autores"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)

    # Relação Many-to-Many com Livro
    livros = relationship('Livro', secondary=livro_autor, back_populates='autores')

    # Construtor
    def __init__(self, nome):
        self.nome = nome