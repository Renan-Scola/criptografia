def criptografar(frase):
  mensagem = ""

  for i in frase:
    mensagem = mensagem + chr(ord(i) + 5)
  return mensagem



def descriptografar(mensagem):
  frase = ""

  for i in mensagem:
    frase = frase + chr(ord(i) - 5)
  return frase



print(criptografar(input("Escreva uma frase para que seja criptografada: ")))

validação = input("digite a senha para descriptografar: ")
if (validação != "wknqwndqwoqwm qosmdlwlm"):
  print("senha incorreta, tente novamente mais tarde!")
else:

  print(descriptografar(input("descriptografe aqui: ")))