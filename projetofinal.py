import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))
  return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
  i = 1
  textos = []
  texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
  while texto:
    textos.append(texto)
    i += 1
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
  return textos

def separa_sentencas(texto):
    #A funcao recebe um texto e devolve uma lista das sentencas dentro do texto#
  sentencas = re.split(r'[.!?]+', texto)
  i = 0
  while i < len(sentencas):
    if sentencas[i] in [" "]:
      del sentencas[i]
    else:
      i += 1
  return sentencas

def separa_frases(sentenca):
    #A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca#
  return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    #A funcao recebe uma frase e devolve uma lista das palavras dentro da frase#
  return frase.split()
    
def separa_todas_palavras(texto):
  #A funcao recebe um texto e devolve uma lista de todas as palavras dentro dele#
  s = separa_sentencas(texto)
  lista_de_frases = []
  for i in s:
    g = separa_frases(i)
    lista_de_frases.extend(g)
  lista_de_palavras = []
  for i in lista_de_frases:
    g = separa_palavras(i)
    lista_de_palavras.extend(g)
  return lista_de_palavras

def n_palavras_unicas(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez#
  freq = dict()
  unicas = 0
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:
      if freq[p] == 1:
        unicas -= 1
        freq[p] += 1
    else:
      freq[p] = 1
      unicas += 1
  return unicas

def n_palavras_diferentes(lista_palavras):
    #Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas#
  freq = dict()
  for palavra in lista_palavras:
    p = palavra.lower()
    if p in freq:
      freq[p] += 1
    else:
      freq[p] = 1
  return len(freq)

def tamanho_medio_palavra(texto):
  #IMPLEMENTAR. Essa funcao recebe um texto e deve devolver o tamanho medio de suas palavras#
  p = separa_todas_palavras(texto)
  x = []
  for i in p:
    x.append(len(i))
  y = 0
  z = 0
  while y < len(x):
    z = z + x[y]
    y += 1
  return z/len(p)
    
def type_token(texto):
  lista_palavras = separa_todas_palavras(texto)
  return n_palavras_diferentes(lista_palavras)/len(lista_palavras)

def hapax_legomana(texto):
  lista_palavras = separa_todas_palavras(texto)
  return n_palavras_unicas(lista_palavras)/len(lista_palavras)

def tamanho_medio_sentenca(texto):
  qtde_sentencas = len(separa_sentencas(texto))
  comprimento_sentencas = 0
  for i in separa_sentencas(texto):
    comprimento_sentencas = comprimento_sentencas + len(i)
  return comprimento_sentencas/qtde_sentencas

def complexidade_sentenca(texto):
  lista_sentencas = separa_sentencas(texto)
  lista_de_frases = []
  for i in lista_sentencas:
    lista_de_frases.append(separa_frases(i))
  return len(lista_de_frases)/len(lista_sentencas)

def tamanho_medio_frase(texto):
  lista_sentencas = separa_sentencas(texto)
  lista_de_frases = []
  for i in lista_sentencas:
    lista_de_frases.extend(separa_frases(i))
  qtde_frases = len(lista_de_frases)
  comprimento_frases = 0
  for frase in lista_de_frases:
    comprimento_frases = comprimento_frases + len(frase)
  return comprimento_frases/qtde_frases

def calcula_assinatura(texto):
    #IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.#
  a = tamanho_medio_palavra(texto)
  b = type_token(texto)
  c = hapax_legomana(texto)
  d = tamanho_medio_sentenca(texto)
  e = complexidade_sentenca(texto)
  f = tamanho_medio_frase(texto)
  assinatura = [a, b, c, d, e, f]
  return assinatura
  
def compara_assinatura(as_a, as_b):
    #IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.#
  somatorio = 0
  for i in range(len(as_a)):
    valor = abs(as_a[i] - as_b[i])
    somatorio += valor
  similaridade = somatorio/6
  return similaridade

def avalia_textos(textos, ass_cp):
    #IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.#
    #supostamente - obviamente supostamente porque sempre tem mais um problema - é a única parte do exercício que falta#
  # textos = le_textos()
  valor_minimo = 900
  i_minimo = -1
  for i in range(len(textos)):
    valor = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
    if valor < valor_minimo:
      valor_minimo = valor
      i_minimo = i
  return i_minimo + 1
  
  assinaturas = [calcula_assinatura(texto) for texto in textos]
  valores = [compara_assinatura(assinatura, ass_cp) for assinatura in assinaturas]
  
  return valores.index(min(valores)) + 1

assinatura = le_assinatura()
textos = le_textos()