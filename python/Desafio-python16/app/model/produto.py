from app.config.db import get_string_conexao
from app.config.db import error

class Produto():
  def __init__(self):
    self.id = 0
    self.nome = "notebook samsung"
    self.descricao = "eletro"
    self.preco = 5000.00

  def salvar(self):
    try:
      connection = get_string_conexao()
      if connection.is_connected():
        cursor = connection.cursor()
        sql = "INSERT INTO produtos (nome, descricao, preco)" + "VALUES (%s, %s, %s)" if self.id == 0 else f"UPDATE produtos SET nome = %s, descricao = %s, preco = %s WHERE id = {self.id}"
        valores = (self.nome, self.descricao, self.preco)
        cursor.execute(sql, valores)
        connection.commit()
        return {"msg": f"produto {'cadastrado' if id == 0 else 'atualizado'} com sucesso...", "error": False}

    except error as e:
        print(e)
        return {"error": True, "msg": e}
    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()
        
  @staticmethod      
  def buscar_por_id(self):
    try:
      connection = get_string_conexao()
      if connection.is_connected():
        cursor = connection.cursor()
        sql = f"SELECT * FROM produtos WHERE id = {self.id}"
        cursor.execute(sql)
        data = cursor.fetchall()
        return {"error": False, "data": data}

    except error as e:
      return {"error": True, "msg": e}
    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()       

  def excluir(self):
    try:
      connection = get_string_conexao()
      if connection.is_connected():
        cursor = connection.cursor()
        sql = f"DELETE FROM produtos WHERE id = {self.id}"
        cursor.execute(sql)
        connection.commit()
        return {"msg": "produto deletado com sucesso...", "error": False}

    except error as e:
      return {"error": True, "msg": e}
    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()
