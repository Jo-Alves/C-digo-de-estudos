from app.config.db import get_string_conexao
from app.config.db import error

class ItensPedido():
  def __init__(self):
    self.id = 0
    self.produto_id = 0
    self.pedido_id = 0

  def salvar(self):
    try:
      connection = get_string_conexao()
      if connection.is_connected():
        cursor = connection.cursor()
        sql = "INSERT INTO itens_pedidos (produto_id, pedido_id)" + "VALUES (%s, %s)"
        valores = (self.produto_id, self.pedido_id)
        cursor.execute(sql, valores)
        connection.commit()
        return {"error": False}
    except error as e:
        print(e)
        return {"error": True, "msg": e}
    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()
