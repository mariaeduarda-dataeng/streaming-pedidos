import time
import random

produtos = ['Pizza', 'Hamburguer', 'Sushi', 'Lasanha']

def gerar_pedido():
    return{
        'Produto': random.choice(produtos),
        'Valor': random.randint(20, 100)
    }

while True:
    pedido = gerar_pedido()
    print(pedido)
    time.sleep(2)