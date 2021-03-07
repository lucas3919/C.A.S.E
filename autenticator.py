import qrcode
lista = str(input('Equipamentos autorizados para o acesso: ')).strip()
n = qrcode.make(lista)
print(type(n))
print(n.size)
n.save('/Users/marques/Documents/CASE/imagens/autenticação.png')
'''
if used:
    delete it
else:
    keep it for 10 minutes
''' 