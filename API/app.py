from flask import Flask, jsonify,request 
# jsonify é uma biblioteca que se encarrega de retornar os dados em formato json

#Instanciando a classe FLASK
app = Flask(__name__) # O python armazena um nome único a esta variável __name__


#pedido de compra é um array (Lista) com um dicionário dentro dela.
pedidoCompra = [

    {
        'id':1,
        'descricao': 'pedido de compra 1',
        #os itens contem tbm uma array com um dicionário com 3 parâmetros. (ID, descrição e valor)
        'itens': [   
            {
                'id':1,
                'descricao': 'Item do pedido 1',
                'valor': 9.99
            }
        ]
    }
] #Terá um ID e uma descrição, e dentro de cada pedido de compra nós teremos os itens de cada pedido


#CRIANDO ALGUNS ENDPOINTS

#GET que retorna todos os pedidos de compra. (Uma Lista)
#GET que retorna os pedidos de compra filtrando por id
#POST onde será possível inserir um novo pedido de compra
#GET Pedido de compra itens. Ou seja, retornar um item de um pedido específico
#POST pedido de comrpa itens. Ou seja, inserir um item a um determinado pedido de compra



@app.route('/')  #Utilizando uma rota (Decorator)
def home():
    return "Hello, Wolrd! Alterado."


#Criando a rota para chamada do método get que retorna todos os pedidos de compra. (o primeiro GET da nossa lista de endpoints acima)
@app.route('/pedidoCompra')
def getPedidoCompra():
    return jsonify(pedidoCompra)



#Uma nova rota será criada para consumir dado pelo ID
#A estrutura da será o caminho da rota, barra, tipo e qual o parâmetro.
@app.route('/pedidoCompra/<int:id>')
def getPedidoCompraById(id): #função que consome dado pelo id, recebendo dentro do parêntese o parâmetro.
    for pc in pedidoCompra: #pc a variável criada que significa pedido de compra
        if pc['id'] == id:
            return jsonify(pc)
    return jsonify({'message':f'Pedido {id} nao encontrado!'})


#Uma nova rota criada para criar novo pedido de compra
@app.route('/pedidoCompra', methods=['POST']) #foi utilizado o methods para restringir o tipo de endpoint a ser utilizado. POST
def criarPedidoCompra():
    dadoRequisicao = request.get_json() #Esta função irá pegar tudo que está no Body e armazenar na variável
    pedido = {
        'id': dadoRequisicao['id'],
        'descricao': dadoRequisicao['descricao'],
        'itens': [

        ]
    }
    #Adcionar pedido a lista de pedidos de compra
    pedidoCompra.append(pedido)

    return jsonify(pedido)


#Criando uma rota que retorna os itens de um determinado pedido
@app.route('/pedidoCompra/<int:id>/itens')
def getPedidoCompraItens(id):
    for pc in pedidoCompra:
        if pc['id'] == id:
            return jsonify(pc['itens'])


#Criando uma rota que adiciona itens em um determinado pedido
@app.route('/pedidoCompra/<int:id>/itens', methods=['POST'])
def criarPedidoCompraItens(id):
    dadoRequisicao = request.get_json() #Esta função irá pegar tudo que está no Body e armazenar na variável
    for pc in pedidoCompra:
        if pc['id'] == id:
            pc['itens'].append({
                'id':dadoRequisicao['id'],
                'descricao': dadoRequisicao['descricao'],
                'preco':dadoRequisicao['preco']
            })

            return jsonify(pc)
        
    return jsonify({'message':f'Pedido {id} nao encontrado!'})



#Criando uma rota que exclui pedido de compra
@app.route('/pedidoCompra/<int:id>', methods=["DELETE"])
def deletePedidoCompra(id):
    for pc in pedidoCompra:
        if pc['id'] == id:
            pedidoCompra.remove(pc)
            return jsonify({'message': f'Pedido {id} foi removido com sucesso!'}), 200
    return jsonify({'message': f'Pedido {id} não encontrado!'}), 404
        

app.run(port=5000)
