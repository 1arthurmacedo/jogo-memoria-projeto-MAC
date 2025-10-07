import random
import time

# Esse é o primeiro tabuleiro a ser mostrado, como se todos os simbolos ainda estivessem escondidos, que já é uma matriz
tabuleiro_original = [
  ["■", "■", "■", "■", "■", "■", "■", "■"],
  ["■", "■", "■", "■", "■", "■", "■", "■"],
  ["■", "■", "■", "■", "■", "■", "■", "■"],
  ["■", "■", "■", "■", "■", "■", "■", "■"],
  ["■", "■", "■", "■", "■", "■", "■", "■"],
  ["■", "■", "■", "■", "■", "■", "■", "■"]
]
tabuleiro_modificado = tabuleiro_original #Aqui é pra gente modificar a lista que tá como tabuleiro modificado, e salvar o original

# Simbolos escondidos
linha1 = ["✝", "●", "▲", "░", "✿", "✦", "✩", "✹"]
linha2 = ["♛", "☠︎", "☂︎", "☣︎", "☸︎", "☯︎", "☘︎", "♟︎"]
linha3 = ["⚜", "➽", "◉", "⬟", "⬣", "$", "❤", "❄︎"]
linha4 = ["✝", "●", "▲", "░", "✿", "✦", "✩", "✹"]
linha5 = ["♛", "☠︎", "☂︎", "☣︎", "☸︎", "☯︎", "☘︎", "♟︎"]
linha6 = ["⚜", "➽", "◉", "⬟", "⬣", "$", "❤", "❄︎"]
linhas =[linha1, linha2, linha3, linha4, linha5, linha6] 
#Se der uma print dessa lista "linhas" vai ser basicamente o resultado final do tabuleiro sem tá tudo embaralhado

def criar_tabuleiro (tabuleiro): 
  
  # Essa função serve para printar o tabuleiro, tanto modificado, quanto o original, essa função ocorre basicamente o tempo todo
  
  print ("  A   B   C   D   E   F   G   H")
  for i in range (6):
    print (i + 1, end=" ")
    for j in range(8):
      print (tabuleiro[i][j], end="   ")
    print()

def aleatoriar_simbolos (linha1, linha2, linha3, linha4, linha5, linha6, linhas):  
  
  # Essa função é aonde a gente usa a biblioteca random, e esse shuffle embaralha os objetos, então eu utilizo ele separadamente em cada linha, e no final utilizo para embaralhar a ordem das linhas, essa função só ocorre no começo do game
  
  random.shuffle (linha1)
  random.shuffle (linha2)
  random.shuffle (linha3)
  random.shuffle (linha4)
  random.shuffle (linha5)
  random.shuffle (linha6)
  random.shuffle(linhas)

def linhas_colunas_indices (coluna, linha):

  # Essa função transforma a coluna e linha para os índices das listas, e da matriz

  if coluna == "A":
    coluna = int(0)
  elif coluna == "B":
    coluna = int(1)
  elif coluna == "C":
    coluna = int(2)
  elif coluna == "D":
    coluna = int(3)
  elif coluna == "E":
    coluna = int(4)
  elif coluna == "F":
    coluna = int(5)
  elif coluna == "G":
    coluna = int(6)
  elif coluna == "H":
    coluna = int(7)

  linha = linha - 1
  return coluna, linha

def acerto_ou_erro (tabuleiro_modificado):

  # Essa função serve para verificar se errou ou acertou, e se acertou manter o tabuleiro modificado, e se errou a coluna e linha selecionada volta para o original

  if tabuleiro_modificado[primeira_escolha[1]][primeira_escolha[0]] == tabuleiro_modificado[segunda_escolha[1]][segunda_escolha[0]]:
    
    print ("Você acertou!")
  else:
    
    print ("Você errou!")
    tabuleiro_modificado[primeira_escolha[1]][primeira_escolha[0]] = "■"
    tabuleiro_modificado[segunda_escolha[1]][segunda_escolha[0]] = "■"




#começa o game

while True: #while para o jogador escolher se quer jogar ou não
  play = input("Você deseja jogar o jogo da memória (SIM/NÃO): ")

  play = play.upper() 

  if play == "SIM": 

    criar_tabuleiro(tabuleiro_original) # cria o tabuleiro com tudo escondido
    tabuleiro_modificado = tabuleiro_original
    aleatoriar_simbolos(linha1, linha2, linha3, linha4, linha5, linha6, linhas) # deixa aleatório os simbolos

    while True: # while para resolver respostas inválias
      while True:
        coluna = input("Digite a coluna que você deseja (letras): ") 
        linha = input("Digite a linha que você deseja(números): ")
        # escolhe a coluna e linha da primeira opção
        if linha not in ("1", "2", "3", "4", "5", "6") or coluna not in ("A", "B", "C", "D", "E" ,"F", "G", "H"): # if para verificar se está nos parametros das linhas e colunas
          print ("Você digitou uma resposta inválida.")
        else: 
          linha = int(linha)
          coluna, linha = linhas_colunas_indices(coluna, linha) # converte a coluna e linha para índices
          primeira_escolha = [coluna, linha] # salva a primeira escolha em uma lista, para comparar ela com a segunda

          if tabuleiro_modificado[primeira_escolha[1]][primeira_escolha[0]] == "■": # if para saber se o objeto já foi escolhido antes
            tabuleiro_modificado[primeira_escolha[1]][primeira_escolha[0]] = linhas [primeira_escolha[1]][primeira_escolha[0]] # modifica o tabuleiro de acordo com a coluna e linha escolhida
            criar_tabuleiro(tabuleiro_modificado) # printa o tabuleiro com a primeira opção aparecendo o simbolo correspondente
            break
          else:
            print ("Você digitou uma resposta inválida.")

      while True:
        coluna = input("Digite a coluna que você deseja (letras): ")
        linha = input("Digite a linha que você deseja(números): ")
        # escolhe a coluna e linha da segunda opção
        if linha not in ("1", "2", "3", "4", "5", "6") or coluna not in ("A", "B", "C", "D", "E" ,"F", "G", "H"):
          print ("Você digitou uma resposta inválida.")
          print ('bug')
        else:
          linha = int(linha)
          coluna, linha = linhas_colunas_indices(coluna, linha) # converte a coluna e linha para índices   
          segunda_escolha = [coluna, linha] # salva a segunda escolha em uma lista, para comparar ela com a primeira
          if tabuleiro_modificado[segunda_escolha[1]][segunda_escolha[0]] == "■" and primeira_escolha != segunda_escolha: # esse if verifica se o objeto já foi escolhido antes e se a segunda resposta está igual a primeira.
            tabuleiro_modificado[segunda_escolha[1]][segunda_escolha[0]] = linhas[segunda_escolha[1]][segunda_escolha[0]]# modifica o tabuleiro de acordo com a coluna e linha escolhida
            criar_tabuleiro(tabuleiro_modificado) # printa o tabuleiro com a primeira e segunda opção
            break
          else:
            print ("Você digitou uma resposta inválida.")
      
      acerto_ou_erro(tabuleiro_modificado) # verifica se as duas opções são iguais, se elas forem iguais o tabuleiro se mantém modificado, se não forem ele deixa o tabuleiro com o símbolo do tabuleiro original
 
      criar_tabuleiro (tabuleiro_modificado) # mostra o tabuleiro de acordo com o erro ou acerto

      if tabuleiro_modificado == linhas: # esse if é pra finalizar o while, caso as o tabuleiro seja todo encontrado
        print("Você venceu!")
        break
  
  elif play == "NÃO":
    break
  else:
    print("Reposta inválida")