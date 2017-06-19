import sys

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'
DICIONARIO_FILE = 'dicio.txt'

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'

  
# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  print(cor + texto + RESET)
  


def adicionar(novaAtividade):
  #Antes, era "desc, extras" nos argumentos
  #if desc  == '' :
   # return False
  #else:
   # novaAtividade = desc + " " + extras
  novaAtividade = organizar([novaAtividade])
  if novaAtividade == "sem desc":
    return False
  # Escreve no TODO_FILE. 
  try: 
    fp = open(TODO_FILE, 'a')
    fp.write(str(novaAtividade) + "\n")
    fp.close()
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False

  return True

    

  
def alfabeto(letra):
  alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  if letra.lower() in alfabeto:
    return True
  else:
    return False
def alfabetoIndex(letra):
  alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  if letra.lower() in alfabeto:
    letra = letra.lower()
    return alfabeto.index(letra)
  else:
    return None

def prioridadeValida(pri):
  if type(pri) == int:
    return False
  if pri[0] == "(" and pri[2] == ")" and alfabeto(pri[1]):
    return True
  
  return False

def separadorHora(hora):
  horas = str(hora[0]) + str(hora[1])
  minutos = str(hora[2]) + str(hora[3])
  return "{}h {}m".format(horas, minutos)

def hora(horaMin):
  i = 0
  campo = ""
  hem = []
  while i < len(horaMin):
      if i == 2:
          hem.append(campo)
          campo = ""
          campo += horaMin[i]
          i += 1
      elif i == 3:
          campo += horaMin[i]
          hem.append(campo)
          campo = ""
          i += 1
      else:
          campo += horaMin[i]
          i += 1

  if int(hem[0]) > 23 or int(hem[0]) < 0:
      return False
  else:
      if int(hem[1]) > 59 or int(hem[1]) < 0:
          return False
      else:
          return True

def horaValida(horaMin) :
  if len(horaMin) != 4 or not soDigitos(horaMin):
    return False
  else:
    if not hora(horaMin):
      return False
    
    return True
def separadorData(data):
  i = 0
  datas = []
  campo = ""
  while i < len(data):                                                                                                  
    if i == 2:
      datas.append(campo)
      campo = ""
      campo += data[i]
      i += 1
    elif i == 4:
      datas.append(campo)
      campo = ""
      campo += data[i]
      i += 1
    elif i == len(data) - 1:
      campo += data[i]  
      datas.append(campo)
      campo = ""
      i += 1
    else:
      campo += data[i]
      i += 1
  mensagem = (str(datas[0])+"/"+str(datas[1])+"/"+str(datas[2]))
  return mensagem

def formatoCorreto(data):
  i = 0
  datas = []
  campo = ""
  while i < len(data):                                                                                                  
    if alfabeto(data[i]):
      return False
    elif i == 2:
      datas.append(campo)
      campo = ""
      campo += data[i]
      i += 1
    elif i == 4:
      datas.append(campo)
      campo = ""
      campo += data[i]
      i += 1
    elif i == len(data) - 1:
      campo += data[i]  
      datas.append(campo)
      campo = ""
      i += 1
    else:
      campo += data[i]
      i += 1
  if int(datas[1]) > 12 or int(datas[1]) < 1:
    return False
  elif int(datas[2]) < 2017:
    return False
         
  else:
    if int(datas[1]) == 1 or int(datas[1]) == 3 or int(datas[1]) == 5 or int(datas[1]) == 7 or int(datas[1]) == 8 or int(datas[1]) == 10 or int(datas[1]) == 12:
      if int(datas[0]) > 31:
        return False
    else:
      if int(datas[1]) == 2:
        if int(datas[0]) > 29:
          return False
      else:
        if int(datas[0]) > 30:
          return False
  return True

      
    

 
def dataValida(data) :
  if len(data) > 8:
    return False
  elif formatoCorreto(data):
    return True
  

  return False

def projetoCorreto(proj):
  if proj[0] == "+":
    return True
  else:
    return False

def projetoValido(proj):
  if len(proj) < 2:
    return False
  elif projetoCorreto(proj):
    return True
  else:
    return False


def contextoValido(cont):
  if len(cont) < 2:
    return False
  else:
    if cont[0] == "@":
      return True

  return False


def soDigitos(numero) :
  if type(numero) != str :
    return False
  for x in numero :
    if x < "0" or x > "9":
      return False
  return True
    
def organizar(texto):
  itens = []
  for linha in texto:
    linha = linha.strip() 
    tokens = linha.split()
    data = '' 
    hora = ''
    pri = ''
    desc = ''
    contexto = ''
    projeto = ''

    while len(tokens) > 0:
      b = 0
      campo = ""
      palavra = tokens[0]
      while b <= len(palavra):
        if b == len(palavra):
          if len(campo) == 3 and prioridadeValida(campo):
            pri = campo
            campo = ""
            b += 1
            palavra = ""
          elif len(campo) > 1 and contextoValido(campo):
            contexto = campo
            b += 1
            campo = ""
            palavra = ""
          elif len(campo) > 1 and projetoValido(campo):
            projeto = campo
            b += 1
            campo = ""
            palavra = ""
          elif len(campo) == 4 and horaValida(campo):
            hora = campo
            b += 1
            campo = ""
            palavra = ""
          elif len(campo) == 8 and dataValida(campo):
            data = campo
            b += 1
            palavra = ""
            campo = ""
          else:
            b += 1
            if len(campo) < 1:
              desc += campo
          
        elif palavra[b].isalnum() or palavra[b] == "+" or palavra[b] == "@" or (palavra[b] == "(" and palavra[b+2] == ")") or (palavra[b] == ")" and palavra[b-2] == "("):
          campo += palavra[b]
          b += 1
        else:
          if len(campo) == 3 and prioridadeValida(campo):
            pri = campo
            campo = ""
            b += 1
            palavra = ""
          elif len(campo) > 1 and contextoValido(campo):
            contexto = campo
            b += 1
            campo = ""
            palavra = ""
          elif len(campo) > 1 and projetoValido(campo):
            projeto = campo
            b += 1
            campo = ""
            palavra = ""
          elif len(campo) == 4 and horaValida(campo):
            hora = campo
            b += 1
            campo = ""
            palavra = ""
          elif len(campo) == 8 and dataValida(campo):
            data = campo
            b += 1
            palavra = ""
            campo = ""
          else:
            b += 1
           
      desc += (campo+" ")
      if len(tokens) >= 1:
        tokens.pop(0)

    desc = desc.strip()
    if len(desc) < 1:
      print("Não há descrição, tente novamente")
      return "sem desc"
     
    #s = " "
    #desc = s.join(desc)
    itens.append((desc, pri, (data, hora, contexto, projeto)))
  return itens

def imprimir(lista):
  contador = 1
  for ind in range(len(lista)):
    string = lista[ind][0]+" "+lista[ind][1]
    data = lista[ind][2][0]
    hora = lista[ind][2][1]
    if len(data) == 8:
      data = separadorData(data)
    if len(hora) == 4:
      hora = separadorHora(hora)
    tupla = data+" "+hora+" "+lista[ind][2][2]+" "+lista[ind][2][3]
    frase = string +" "+ tupla
    if lista[ind][1].upper() == "(A)" :
      printCores("{}. {}".format(contador, frase), RED)
    elif lista[ind][1].upper() == "(B)" :
      printCores("{}. {}".format(contador, frase), BLUE)
    elif lista[ind][1].upper() == "(C)":
      printCores("{}. {}".format(contador, frase), CYAN)
    elif lista[ind][1].upper() == "(D)":
      printCores("{}. {}".format(contador, frase), YELLOW)
    else:  
      print("{}. {}".format(contador, frase))
    contador += 1      
  
def ano(data):
  if len(data) == 8:
    ano = int(data[4]+data[5]+data[6]+data[7])
    return ano
  else:
    return int(data)

def mes(data):
  if len(data) == 8:
    mes = int(data[2]+data[3])
    return mes
  else:
    return int(data)

def dia(data):
  if len(data) == 8:
    dia = int(data[0]+data[1])
    return dia
  else:
    return int(data)
def horario(hora):
  if len(hora) == 4:
    h = hora[0]+hora[1]
    return h
  else:
    return hora
def minuto(hora):
  if len(hora) == 4:
    m = hora[2]+hora[3]
    return m
  else:
    return hora

def ordenarPorDataHora():
  ordenada1 = ordenarPorPrioridade()
  j = 0
  while j < len(ordenada1):
    i = 0
    while i < len(ordenada1) - 1:
      if ordenada1[i][1] != ordenada1[i+1][1]:
        i += 1
      else:
        data1 = ordenada1[i][2][0]
        data2 = ordenada1[i+1][2][0]
        hora1 = ordenada1[i][2][1]
        hora2 = ordenada1[i+1][2][1]
        if data1 == "" or data2 == "":
          if data1 == "" and data2 != "":
            ordenada1[i], ordenada1[i+1] = ordenada1[i+1], ordenada1[i]
            i += 1
          elif data2 == "":
            if data1 == "":
              if hora1 == "" and hora2 != "":
                ordenada1[i], ordenada1[i+1] = ordenada1[i+1], ordenada1[i]
                i += 1
              else:
                i += 1
            else:
               i += 1            
          else:
            i += 1
        else:
          year1 = ano(data1)
          year2 = ano(data2)
          if year1 > year2:
            ordenada1[i], ordenada1[i+1] = ordenada1[i+1], ordenada1[i]
            i += 1
          elif year1 == year2:
            month1 = mes(data1)
            month2 = mes(data2)
            if month1 > month2:
              ordenada1[i], ordenada1[i+1] = ordenada1[i+1], ordenada1[i]
              i += 1
            elif month1 == month2:
              day1 = dia(data1)
              day2 = dia(data2)
              if day1 > day2:
                ordenada1[i], ordenada1[i+1] = ordenada1[i+1], ordenada1[i]
                i += 1
              elif day1 == day2:
                if hora1 == "" or hora2 == "":
                  if hora1 == "" and hora2 != "":
                    ordenada1[i], ordenada1[i+1] = ordenada1[i+1], ordenada1[i]
                    i += 1
                  else:
                    i += 1
                else:
                  hour1 = horario(hora1)
                  hour2 = horario(hora2)
                  if hora1 > hora2:
                    ordenada1[i], ordenada1[i+1] = ordenada1[i+1], ordenada1[i]
                    i += 1
                  elif hora1 == hora2:
                    minute1 = minuto(hora1)
                    minute2 = minuto(hora2)
                    if minute1 > minute2:
                      ordenada1[i], ordenada1[i+1] = ordenada1[i+1], ordenada1[i]
                      i += 1
                    else:
                      i += 1                  
                  else:
                    i += 1 
              else:
                i += 1
            else:
              i += 1
          else:
            i += 1

    j += 1
  lista_final = ordenada1
  return lista_final

  

def ordenarPorPrioridade():
  sem_prioridade = []
  listona = listar_s()
  j = 0
  while j < len(listona):
    i = 0
    while i < len(listona) - 1:
      if listona[i][1] == "":
        sem_prioridade.append(listona[i])
        del listona[i]
        i += 1
      elif listona[i][1] > listona[i+1][1]:
        listona[i], listona[i+1] = listona[i+1], listona[i]
        i += 1
      else:
        i += 1

    j += 1
  total = listona + sem_prioridade
  return total

def listar_s():
  fil = open(TODO_FILE, 'r')
  total_texto = fil.readlines()
  lista_listar = organizar(total_texto)
  fil.close()
  return lista_listar    

def listar():
  #fil = open(TODO_FILE, 'r')
  #total_texto = fil.readlines()
  #lista_listar = organizar(total_texto)
  #fil.close()
  lista_listar = ordenarPorDataHora()
  imprimir(lista_listar)
  
  return  

def fazer(num):
  indice = num - 1
  lista_ord = ordenarPorDataHora()
  linha_rmv = lista_ord[indice]
  arquivo = open(TODO_FILE, "r")
  linhas_totais = arquivo.readlines()
  total = organizar(linhas_totais)
  
  arquivo.close()
  fil = open(TODO_FILE, "w")
  for x in total:
    if x != linha_rmv:
      fil.write(str(x)+"\n")
  f = open(ARCHIVE_FILE, 'a')
  f.write(str(linha_rmv) + "\n")  
  return 


def remover(num):
  indice = num - 1
  lista_ord = ordenarPorDataHora()
  linha_rmv = lista_ord[indice]
  arquivo = open(TODO_FILE, "r")
  linhas_totais = arquivo.readlines()
  total = organizar(linhas_totais)  
  arquivo.close()
  fil = open(TODO_FILE, "w")
  for x in total:
    if x != linha_rmv:
      fil.write(str(x)+"\n")
    
def priorizar(num, prioridade):
  if not prioridadeValida(prioridade):
    return "Algo deu errado"
  indice = num - 1
  lista_ord = ordenarPorDataHora()
  linha_pri = lista_ord[indice]
  reescrever = linha_pri[0]+ " "+ prioridade
  tuplinha = " ".join(linha_pri[2])
  nova_pri = reescrever +" "+ tuplinha
  nova_pri = organizar([nova_pri])
  f = open(TODO_FILE, "r")
  linhas = f.readlines()
  total = organizar(linhas)
  f.close()
  fi = open(TODO_FILE, "w")
  for x in total:
    if x == linha_pri:
      fi.write(str(nova_pri) + "\n")
    else:
      fi.write(str(x) + "\n")      
  return 

def processarComandos(comandos) :
  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'adicionar'
    try:
      itemParaAdicionar = organizar([' '.join(comandos)])[0]
      adicionar(itemParaAdicionar[0], itemParaAdicionar[2]) # novos itens não têm prioridade
    except IndexError:
      print("Xiiii... Algo deu errado... tente novamente")
    return None
  elif comandos[1] == LISTAR:
    comandos.pop(0) #remove agenda.py
    comandos.pop(0) #remove o listar
    listar()
    return           
  elif comandos[1] == REMOVER:
    comandos.pop(0) #remove agenda.py
    comandos.pop(0) #remove o ... remover h3uhu
    numero = (int(comandos[0]))
    remover(numero)
    return 
  elif comandos[1] == FAZER:
    comandos.pop(0)
    comandos.pop(0)
    fazer(int(comandos[0]))
  elif comandos[1] == PRIORIZAR:
    comandos.pop(0) #remove agenda.py
    comandos.pop(0) #remove o priorizar
    priorizar(int(comandos[0]), comandos[1])
    return
  else :
    print("Comando inválido.")
    
  
# sys.argv é uma lista de strings onde o primeiro elemento é o nome do programa
# invocado a partir da linha de comando e os elementos restantes são tudo que
# foi fornecido em sequência. Por exemplo, se o programa foi invocado como
#
# python3 agenda.py a Mudar de nome.
#
# sys.argv terá como conteúdo
#
# ['agenda.py', 'a', 'Mudar', 'de', 'nome']
#processarComandos(sys.argv)


