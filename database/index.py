import json

path = './entregar2/database/dados.json'

class connect ():
  def __init__ (self):
    with open(path, 'r') as json_file:
      data = json.load(json_file)
      self.data = data

  def select (self, key):
    try:
      if key == '*':
        return self.data 
      return self.data[key]

    except:
      print('\033[31m--Error tente novamente.\033[m')
      return False

  def update (self, key, data):
    try:
      self.data[key] = data
      self.refreshJsonFile()
    except:
      print('\033[31m--Error tente novamente.\033[m')
      return False

  def refreshJsonFile (self):
    with open(path, 'w') as json_file:
      json.dump(self.__data, json_file, indent=4)
