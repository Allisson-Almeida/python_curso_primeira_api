from flask import Flask, jsonify # jsonify é uma biblioteca que se encarrega de retornar os dados em formato json

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


app.run(port=5000)
