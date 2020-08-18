import dicionario

def initArray(arquivo):
    dados=[] 
    with open(arquivo,'r', encoding="iso-8859-1") as f:
        for frase in f.readlines():
            if any(x in frase for x in dicionario.dictTabelas):
                campos = frase.split("|")
                dados.append(campos)
    return dados

def removeZero(campo):
    for x in range(startCampos2,fimCampos2-1):
        print(frase[x])
        if(frase[x] != "0"):
            print("STOP LOOP")
            break
        else:
            zeroEsquerda+=1
            print("zeros a esquerda: ", zeroEsquerda)
        if(zeroEsquerda>0):
            print(frase)
            # novaFrase = frase[:startCampos2] + frase[zeroEsquerda+startCampos2:]
            print(novaFrase)
            frase = novaFrase
    return frase



def checkDuplicata(campos):
    pass