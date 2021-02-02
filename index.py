from database.index import connect
from menu import menu
from Estado import Estado
from Cidade import Cidade

db = connect()

def setDadosIniciaisEstado ():
  estados = db.select('estados')
  
  return list(map(lambda props: Estado(props['nome'], props['uf']), estados))
  
def setDadosIniciaisCidade ():
  cidades = db.select('cidades')
  return list(map(lambda props: Cidade(props['nome'], props['estado']), cidades))

def getNomesCidades (list_estados):
  return list(map(lambda value: value.nome, list_estados))

def getNomesEstados (list_estados):
  return list(map(lambda value: value.nome, list_estados))

def getUfEstados (list_estados):
  return list(map(lambda value: value.uf, list_estados))


def saveDadosCidade (list_cidades):
  cidades = list(map(lambda value: value.getAttrs(), list_cidades))
  db.update('cidades', cidades)
  print('\033[1;37;42m 🟢Cidades salvas com sucesso!.\033[m\n')

def saveDadosEstado (list_estados):
  estados = list(map(lambda value: value.getAttrs(), list_estados))
  db.update('estados', estados)
  print('\033[1;37;42m 🟢Estados salvos com sucesso!.\033[m\n')


def main ():
  list_estados = setDadosIniciaisEstado()
  list_cidades = setDadosIniciaisCidade()
  def cadastrarEstados ():
    nomes_cidades = getNomesCidades(list_cidades)
    nomes_estados = getNomesEstados(list_estados)
    ufs_estados = getUfEstados(list_estados)

    print('\n📝 Cadastrar Estado\n')

    escolha_estado = input('Digite o nome da Estado: ').upper()
    while escolha_estado in nomes_estados:
      print('\n\033[1;37;41m 🔴, estado já cadastrado.\033[m\n')
      escolha_estado = input('Digite o nome da Estado: ').upper()

    
    escolha_uf = input('\nDigite a UF do Estado: \n').upper()
    while escolha_uf in ufs_estados:
      print('\n\033[1;37;41m 🔴, UF já cadastrada.\033[m\n')
      escolha_uf = input('Digite a UF do Estado: ').upper()

    
    novo_estado = Estado(escolha_estado, escolha_uf)

    list_estados.append(novo_estado)

    saveDadosEstado(list_estados)
    
    
  def cadastrarCidades():
    nomes_cidades = getNomesCidades(list_cidades)
    nomes_estados = getNomesEstados(list_estados)

    print('\n📝 Cadastrar Cidade\n')
    escolha_cidade = input('Digite o nome da Cidade: ').upper()

    while escolha_cidade in nomes_cidades:
      print('\n\033[1;37;41m 🔴, cidade já cadastrada.\033[m\n')
      escolha_cidade = input('Digite o nome da Cidade: ').upper()
    
    opcoes_menu_estado = {
      'title': '\n## Escolha um entre os estados cadastrados\n',
      'opcoes': nomes_estados
    }

    escolha_estado = menu.render(opcoes_menu_estado)[1]

    nova_cidade = Cidade(escolha_cidade, escolha_estado)
    list_cidades.append(nova_cidade)
    saveDadosCidade(list_cidades)
    
  def relatorioEstados ():
    print('\n📋 Relatório Estados\n')
    for estado in list_estados:
      print(f'# {estado.nome} ---- quantidade de casos: {estado.casos}\n')

  def relatorioCidades ():
    print('\n📋 Relatório Cidades\n')
    for cidade in list_cidades:
      print(f'# {cidade.nome} ---- quantidade de casos: {cidade.casos}\n')

  def atualizarCasos ():
    print('\n🤒 Atualizar casos\n')

    nomes_cidades = getNomesCidades(list_cidades)

    casos_menu = {
      'title': '# E scolha quanl cidade deseja atualizar',
      'opcoes': nomes_cidades 
    }

    escolha_cidade = menu.render(casos_menu)[1]

    quantidade_casos = int(input('\nDigite o número de casos: '))
    
    while quantidade_casos <= 0:
      print('\n\033[1;37;41m 🔴, Valor precisa ser maior que 0.\033[m\n')
      quantidade_casos = int(input('\nDigite o número de casos: '))


    for index_cidade, cidade in enumerate(list_cidades):
      if cidade.nome == escolha_cidade:
        list_cidades[index_cidade].casos += quantidade_casos

      for index_estado, estado in enumerate(list_estados):
        if estado.nome == cidade.estado:
          list_estados[index_estado].casos += quantidade_casos

    saveDadosCidade(list_cidades)
    saveDadosEstado(list_estados)

  main_menu = {
    'title': '🖇  Menu',
    'opcoes': [
      'Finalizar o Programa',
      'Cadastrar estados',
      'Cadastrar cidades',
      'Relatório estados',
      'Relatório cidades',
      'Atualizar números de casos',
    ]
  }

  while True:
    escolha = menu.render(main_menu)[0]

    if escolha == 0: break
    elif escolha == 1: cadastrarEstados()
    elif escolha == 2: cadastrarCidades()
    elif escolha == 3: relatorioEstados()
    elif escolha == 4: relatorioCidades()
    elif escolha == 5: atualizarCasos()
main()
