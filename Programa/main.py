ref_qbdata = open("qbdata.txt", "r")

for valor in ref_qbdata:
    valores = valor.split()
    print(valores[0])

ref_qbdata.close()
