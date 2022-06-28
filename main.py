#Conceito verdadeiro ou falso usando comando (true) e (false)
#Fazer um programa simples no qual a cliente precisa de uma aprovação para um financiamento.

reda_maior_5mil = False
nome_limpo = False

if reda_maior_5mil or nome_limpo:
    print('Financiamento provado')
else:
    print('Finaciamento negado!')

  #qui no comando (True) inicialmente eu estava colocando com letras minusculas, isso estava gerando um erro. Fica atento com esse comando na diferença

#Assim que eu mudo os dois objetos (reda_maior_5mil) e (nome_limpo) para False ele roda a msg FINANCIAMENTO NEGADO, no (True) ele da FINANCIAMENTO APOROVADO