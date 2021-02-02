def menu (props):
  labels = list(map(lambda opcao: opcao['label'], props['opcoes']))
  if len(labels) < 1:
    return False

  title = props['title']
  opcoes = props['opcoes']

  print(title)
  for index, render in enumerate(opcoes):
    label = render['label']

    print(f'{index} - {label}')

  while True:
    try:
      escolha = int(input('\nEscolha: '))      
      if (opcoes[escolha]):
        return [escolha, labels[escolha]]
        print('Escolha errada')
    except:
      print('\033[31m--Error tente novamente.\033[m')
      
