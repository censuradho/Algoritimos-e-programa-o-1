class menu:

  @staticmethod
  def render (props):
    labels = list(map(lambda opcao: opcao, props['opcoes']))
    
    title = props['title']
    opcoes = props['opcoes']

    print(title)
    for index, render in enumerate(opcoes):
      label = render

      print(f'{index} - {label}')

    while True:
      try:
        escolha = int(input('\nEscolha: '))      
        if (opcoes[escolha]):
          return [escolha, labels[escolha]]
      except:
        print('\033[1;37;41m 🔴 tente novamente.\033[m')
        
