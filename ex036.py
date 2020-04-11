valor = float(input('Digite o valor total da Casa: '))
salario = float(input('Digite o valor da sua renda mensal: '))
tempo = int(input('Em quantos anos quer pagar: '))
cal = valor/(tempo*12)
if valor/(tempo*12) > salario*30/100:
    print('Solicitação de emprestimo \033[0;31mREPROVADA\033[m!!')
else:
    print('Solicitação de emprestimo \033[0;32mAPROVADO\033[m!!')
print ('O valor das parcelas ficam em: {:.0f} X {:.2f}'.format(tempo*12,cal))
