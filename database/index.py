import json
import os

currentDir = os.getcwd()

path = f'{currentDir}/database/dados.json'

class connect:
  def __init__(self):
    with open(path, 'r') as json_file:
      data = json.load(json_file)
      self.__data = data
  
  def select (self, attr):
    if attr == '*':
      return self.__data
    return self.__data[attr]

    if len(values) > 0:
      return values
    return False

  def update (self, key, data):
    self.__data[key] = data
    self.refreshJsonFile()

  def refreshJsonFile (self):
    with open(path, 'w') as json_file:
      json.dump(self.__data, json_file, indent=4)