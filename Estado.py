class Estado:
  def __init__ (self, nome, uf):
    self.__nome = nome
    self.__uf = uf
    self.__pais = 'BRASIL'
    self.__casos = 0
  
  @property
  def nome (self):
    return self.__nome

  @property
  def uf (self):
    return self.__uf

  @property
  def pais (self):
    return self.__pais
  
  @property
  def casos (self):
    return self.__casos

  @casos.setter
  def casos (self, numero):
    self.__casos = numero

  def getAttrs (self):
    return {
      'nome': self.__nome,
      'uf': self.__uf,
      'pais': self.__pais,
      'casos': self.__casos
    }







  
