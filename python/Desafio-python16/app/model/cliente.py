from app.config.db import get_string_conexao
from app.config.db import error

class Cliente():
  def __init__(self):
    self.id = 1
    self.nome = ""
    self.email = ""

  def salvar(self):
    try:
      connection = get_string_conexao()
      if connection.is_connected():
        cursor = connection.cursor()
        sql = "INSERT INTO clientes (nome, email)" + "VALUES (%s, %s)" if self.id == 0 else f"UPDATE clientes SET nome = %s, email = %s WHERE id = {self.id}"
        valores = (f'{self.nome}', f'{self.email}')
        cursor.execute(sql, valores)
        connection.commit()
        return {"msg": f"cliente {'cadastrado' if id == 0 else 'atualizado'} com sucesso...", "error": False}

    except error as e:
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
        sql = f"SELECT * FROM clientes WHERE id = {self.id}"
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
        sql = f"DELETE FROM clientes WHERE id = {self.id}"
        cursor.execute(sql)
        connection.commit()
        return {"msg": "cliente deletado com sucesso...", "error": False}

    except error as e:
      return {"error": True, "msg": e}
    finally:
      if connection.is_connected():
        cursor.close()
        connection.close()
