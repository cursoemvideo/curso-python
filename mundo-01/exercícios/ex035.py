def verifica_float(numero):
    """
    FUNÇÃO QUE VALIDA A ENTRADA COMO FLOAT.
    RECEBE UM PARÂMETRO, QUE É O VALOR A SER VALIDADO
    A FUNÇÃO RETIRA ESPAÇOS ANTES E DEPOIS DA VARIÁVEL
    """
    while True:#ENQUANTO NÃO CHEGAR NO BREAK
        numero=numero.strip()#RETIRAR ESPAÇOS ANTES E DEPOIS
        numero=numero.replace(",",".")#SUBSTITUI AS VÍRGULAS(,) POR PONTO(.)
        try:#TENTA CONVERTER PARA FLOAT
            numero=float(numero)
        except:#SE NÃO CONSEGUIR, RECEBE OUTRA ENTRADA
            numero=input("Número não é Real. Tente novamente.\n--> ")
        else:#CASO A CONVERSÃO SEJA POSSÍVEL
            return numero
            break#FIM DO LAÇO


print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = verifica_float(input('Primeiro segmento: '))
r2 = verifica_float(input('Segundo segmento: '))
r3 = verifica_float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
