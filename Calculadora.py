import time

print("Criado por Nicolas Luiz - © Nenhum direito reservado")
time.sleep(2)
print("Olá! Qual é o seu nome?")
var = input()
print("É um prazer em te conhecer,")
print(var)
time.sleep(5)
print("Vamos fazer um cálculo matemático?")
time.sleep(2)
print("O que você quer fazer? Subtrair, Somar, Dividir ou Multiplicar?")
entrada = input("")
if entrada == "Somar":
    print("Digite abaixo dois números para somar algo!")
    primeiraparcela = input()
    segundaparcela = input()
    total = int(primeiraparcela) + int(segundaparcela)
    print("O total é..", total)


elif entrada == "Subtrair":
    print("Digite dois números abaixo para fazer a subtração!")
    minuendo = input()
    subtraendo = input()
    resto = int(minuendo) - int(subtraendo)
    print("O resto ou diferença é...", resto)

elif entrada == "Dividir":
    print("Digite dois números para fazer a divisão!")
    dividendo = input()
    divisor = input()
    quociente = int(dividendo) / int(divisor)
    print("O quociente é...", quociente)

elif entrada == "Multiplicar":
    print("Digite dois números para fazer a multiplicação!")
    fatorum = input()
    fatordois = input()
    produto = int(fatorum) * int(fatordois)
    print("O produto é...", produto)

else:
    print("Informações enviadas inválidas")