from app import *


@app.route('/autores', methods=['GET'])
def listar_autores():
    autores = Autor.query.all()

    # Crie uma lista de dicionários com os dados dos autores
    autores_json = []
    for autor in autores:
        autores_json.append({
            'id': autor.id,
            'nome': autor.nome
        })

    return jsonify(autores_json)


@app.route('/autores', methods=['POST'])
def criar_autor():
    dados = request.get_json()

    novo_autor = Autor(nome=dados['nome'])

    db.session.add(novo_autor)
    db.session.commit()

    autor_criado = {
        'nome': novo_autor.nome
    }

    # Crie um dicionário com os dados do autor recém-criado
    autor_criado = {
        'id': novo_autor.id,
        'nome': novo_autor.nome
    }

    return jsonify({'mensagem': 'Autor criado com sucesso', 'autor': autor_criado}), 201

@app.route('/autores/<int:id>', methods=['GET'])
def buscar_autor(id):
    autor = Autor.query.get(id)

    # Verifique se o autor existe
    if not autor:
        return jsonify({'mensagem': 'Autor não encontrado'}), 404

    # Crie um dicionário com os dados do autor
    autor_json = {
        'id': autor.id,
        'nome': autor.nome
    }

    return jsonify(autor_json)

@app.route('/autores/<int:id>', methods=['PUT'])
def atualizar_autor(id):
    autor = Autor.query.get(id)

    # Verifique se o autor existe
    if not autor:
        return jsonify({'mensagem': 'Autor não encontrado'}), 404

    dados = request.get_json()

    # Atualize o autor
    autor.nome = dados['nome']

    db.session.commit()

    # Crie um dicionário com os dados do autor atualizado
    autor_atualizado = {
        'id': autor.id,
        'nome': autor.nome
    }

    return jsonify({'mensagem': 'Autor atualizado com sucesso', 'autor': autor_atualizado})

@app.route('/autores/<int:id>', methods=['DELETE'])
def remover_autor(id):
    autor = Autor.query.get(id)

    # Verifique se o autor existe
    if not autor:
        return jsonify({'mensagem': 'Autor não encontrado'}), 404

    db.session.delete(autor)
    db.session.commit()

    return jsonify({'mensagem': 'Autor removido com sucesso'})
