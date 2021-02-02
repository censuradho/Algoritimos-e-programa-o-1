from menu import menu

pesquisa = {
  'avaliadores': {},
  'notas': ['Péssimo', 'Ruim', 'Regular', 'Bom', 'Ótimo'],
  'lista_de_produtos': ['COCACOLA', 'GUARANÁ', 'PEPSI', 'FANTA', 'SPRITE'],
}

def getMenuOptions(title, keys):
  opcoes = []

  for opcao in keys:
    opcoes.append({ 'label': opcao })

  render_menu_avaliacao = {
    'title': title,
    'opcoes': opcoes
  }

  return render_menu_avaliacao

def getNota(props):
  for index, value in enumerate(pesquisa['notas']):
    if value == props['nota']:
      return index 

def cadastrarAvaliador():
  avaliador = input('\n👤  Digite o nome do avaliador: ')
  pesquisa['avaliadores'][avaliador] = { 'avaliacoes': [] }
  print('\033[32mAvaliador cadastrado com sucesso! ✅\033[m \n \n')
  
def realizarAvaliacao():

  def validaAvaliacao(bebida, avaliador):
    bebidas_list = []
    for interator in pesquisa['avaliadores'][avaliador]['avaliacoes']:
      bebidas_list.append(interator['bebida'])
    if bebida in bebidas_list:
      return False
    return True
      
  def setNota(props, avaliador):
    avaliacao = { 'nota': props['nota'], 'bebida': props['bebida'] }
    pesquisa['avaliadores'][avaliador]['avaliacoes'].append(avaliacao)
  
  avaliadores = pesquisa['avaliadores'].keys()

  menu_options_avaliador = getMenuOptions('📝  Avaliação: Escolha um avaliador para começar.', avaliadores)
  menu_options_bebida = getMenuOptions('📝  Avaliação: Escolha qual bebida deseja avaliar.', pesquisa['lista_de_produtos'])
  menu_options_nota = getMenuOptions('📝  Avaliação: Agora escolha a nota adequada.', pesquisa['notas'])

  escolha_avaliador = menu(menu_options_avaliador)[1]
  escolha_bebida = menu(menu_options_bebida)[1]

  is_valid = validaAvaliacao(escolha_bebida, escolha_avaliador)

  if is_valid == False:
    return print('\033[31m--Error Só é possivel avaliar 1 unica vez cada bebida.\033[m')

  
  escolha_nota = menu(menu_options_nota)[1]

  nota = { 'bebida': escolha_bebida, 'nota': escolha_nota }

  setNota(nota, escolha_avaliador)

  print('\033[32mAvaliação realizada com sucesso!  ✅\033[m')
  
def relatorioAvaliadores():
  print('\n📋  Relatório Avaliadores: Quantidade de avaliações por avaliador\n\n')
  for interator in pesquisa['avaliadores']:
    numero_de_avaliacoes = len(pesquisa['avaliadores'][interator]['avaliacoes'])

    print(f'{interator}: {numero_de_avaliacoes}\n')

def relatorioProdutos():
  score = {}

  for produto in pesquisa['lista_de_produtos']:
    score[produto] = 0

  for avaliador in pesquisa['avaliadores']:
    for avalicao in pesquisa['avaliadores'][avaliador]['avaliacoes']:
      produto = avalicao['bebida']

      nota = getNota(avalicao)
      score[produto] = score[produto] + nota
  print(score)
          
render_main_menu = {
  'title': '🖇  Menu',
  'opcoes': [
    { 'label': 'Finalizar o Programa' },
    { 'label': 'Cadastrar avaliador' },
    { 'label': 'Realizar avaliação' },
    { 'label': 'Relatório de avaliadores' },
    { 'label': 'Relatório de produtos' },
  ]
}

while True:
  escolha = menu(render_main_menu)[0]
  if (escolha == 0): break
  elif (escolha == 1): cadastrarAvaliador()
  elif (escolha == 2): realizarAvaliacao()
  elif (escolha == 3): relatorioAvaliadores()
  elif (escolha == 4): relatorioProdutos()