from app import *

@app.route('/livros', methods=['GET'])
def listar_livros():
    livros = Livro.query.all()

    # Crie uma lista de dicionários com os dados dos livros
    livros_json = []
    for livro in livros:
        livros_json.append({
            'id': livro.id,
            'titulo': livro.titulo,
            'isbn': livro.isbn,
            'autores': [autor.id for autor in livro.autores],  # Passe os IDs dos autores
            'dataDePublicacao': livro.dataDePublicacao.strftime('%Y-%m-%d'),
            'estoque': livro.estoque.value  # Use .value para obter o valor Enum
        })

    return jsonify(livros_json)


@app.route('/livros', methods=['POST'])
def criar_livro():
    dados = request.get_json()

    # Certifique-se de que a lista de autores esteja presente no JSON
    if 'autores' not in dados:
        dados['autores'] = []

    # Crie uma lista de objetos Autor com base nos IDs fornecidos
    autores = []
    for autor_id in dados['autores']:
        autor = Autor.query.get(autor_id)
        if autor:
            autores.append(autor)

    # Crie o livro e associe os objetos Autor a ele
    novo_livro = Livro(
        titulo=dados['titulo'],
        isbn=dados['isbn'],
        autores=autores,
        dataDePublicacao=dados['dataDePublicacao'],
        estoque=dados['estoque']
    )

    db.session.add(novo_livro)
    db.session.commit()

    # Crie um dicionário com os dados do livro recém-criado
    livro_criado = {
        'id': novo_livro.id,
        'titulo': novo_livro.titulo,
        'isbn': novo_livro.isbn,
        'autores': [autor.id for autor in novo_livro.autores],  # Passe os IDs dos autores
        'dataDePublicacao': novo_livro.dataDePublicacao.strftime('%Y-%m-%d'),
        'estoque': novo_livro.estoque.value  # Use .value para obter o valor Enum
    }

    # Retorne a mensagem de sucesso e os dados do livro em JSON
    return jsonify({'mensagem': 'Livro criado com sucesso', 'livro': livro_criado}), 201

@app.route('/livros/<int:id>', methods=['GET'])
def buscar_livro(id):
    livro = Livro.query.get(id)

    # Verifique se o livro existe
    if not livro:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404

    # Crie um dicionário com os dados do livro
    livro_json = {
        'id': livro.id,
        'titulo': livro.titulo,
        'isbn': livro.isbn,
        'autores': [autor.id for autor in livro.autores],  # Passe os IDs dos autores
        'dataDePublicacao': livro.dataDePublicacao.strftime('%Y-%m-%d'),
        'estoque': livro.estoque.value  # Use .value para obter o valor Enum
    }

    return jsonify(livro_json)


@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    livro = Livro.query.get(id)

    # Verifique se o livro existe
    if not livro:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404

    dados = request.get_json()

    # Certifique-se de que a lista de autores esteja presente no JSON
    if 'autores' not in dados:
        dados['autores'] = []

    # Crie uma lista de objetos Autor com base nos IDs fornecidos
    autores = []
    for autor_id in dados['autores']:
        autor = Autor.query.get(autor_id)
        if autor:
            autores.append(autor)

    # Atualize o livro e associe os objetos Autor a ele
    livro.titulo = dados['titulo']
    livro.isbn = dados['isbn']
    livro.autores = autores
    livro.dataDePublicacao = dados['dataDePublicacao']
    livro.estoque = dados['estoque']

    db.session.commit()

    # Crie um dicionário com os dados do livro atualizado
    livro_atualizado = {
        'id': livro.id,
        'titulo': livro.titulo,
        'isbn': livro.isbn,
        'autores': [autor.id for autor in livro.autores],  # Passe os IDs dos autores
        'dataDePublicacao': livro.dataDePublicacao.strftime('%Y-%m-%d'),
        'estoque': livro.estoque.value  # Use .value para obter o valor Enum
    }

    return jsonify({'mensagem': 'Livro atualizado com sucesso', 'livro': livro_atualizado})

@app.route('/livros/<int:id>', methods=['DELETE'])
def remover_livro(id):
    livro = Livro.query.get(id)

    # Verifique se o livro existe
    if not livro:
        return jsonify({'mensagem': 'Livro não encontrado'}), 404

    db.session.delete(livro)
    db.session.commit()

    return jsonify({'mensagem': 'Livro removido com sucesso'})
