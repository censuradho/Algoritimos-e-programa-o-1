    # { "nome": "Porto Alegre", "estado": 0, "casos": 0 }
class Cidade:
  def __init__ (self, nome, estado):
    self.__nome = nome
    self.__estado = estado
    self.__casos = 0
  
  @property
  def nome (self):
    return self.__nome

  @nome.setter 
  def nome (self, nome):
    self.__nome = nome

  @property
  def estado (self):
    return self.__estado

  @estado.setter 
  def estado (self, estado):
    self.__estado = estado

  @property
  def casos (self):
    return self.__casos

  @casos.setter 
  def casos (self, numero):
    self.__casos = numero

  def getAttrs (self):
    return {
      'nome': self.__nome,
      'estado': self.__estado,
      'casos': self.__casos
    }