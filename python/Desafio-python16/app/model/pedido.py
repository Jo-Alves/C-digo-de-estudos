from app.config.db import get_string_conexao
from app.config.db import error
from app.model.itens_pedidos import ItensPedido
from app.model.produto import Produto

item_pedido = ItensPedido()

class Pedido():
  def __init__(self):
    self.id = 1
    self.cliente_id = 1
    self.valor_total = 5000.00
    self.itens = [{"produto_id": 1}]

  def salvar(self):
    try:
      connection = get_string_conexao()
      if connection.is_connected():
        cursor = connection.cursor()
        sql = "INSERT INTO pedidos (cliente_id, valor_total)" + "VALUES (%s, %s)"
        valores = (self.cliente_id, self.valor_total)
        cursor.execute(sql, valores)
        connection.commit()
        sql = f"SELECT LAST_INSERT_ID();"
        cursor.execute(sql)
        last_id = cursor.fetchall()
        for item in self.itens:
          item_pedido.produto_id = item["produto_id"]
          item_pedido.pedido_id = last_id[0][0]
          item_pedido.salvar()
          
        return {"msg": "pedido cadastrado com sucesso...", "error": False}
      
    except error as e:
        print(e)
        return {"error": True, "msg": e}
    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()
        
  def buscar_por_id(self):
    try:
      connection = get_string_conexao()
      if connection.is_connected():
        cursor = connection.cursor()
        sql = f"SELECT * FROM pedidos WHERE id = {self.id}"
        cursor.execute(sql)
        data = cursor.fetchall()
        return {"error": False, "data": data}

    except error as e:
      return {"error": True, "msg": e}
    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()
    
  def calcalcularValorTotal(self):
    