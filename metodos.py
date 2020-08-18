import dicionario as dicionario

def initArray(arquivo):
    dados=[] 
    with open(arquivo,'r', encoding="iso-8859-1") as f:
        for frase in f.readlines():
            if any(x in frase for x in dicionario.dictTabelas):
                campos = frase.split("|")
                dados.append(campos)
    return dados

def removeZero(campo):
    zeroEsquerda = 0
    for x in campo:
        print(campo[x])
        if(campo[x] != "0"):
            print("STOP LOOP")
            break
        else:
            zeroEsquerda+=1
            print("zeros a esquerda: ", zeroEsquerda)
        if(zeroEsquerda>0):
            print(campo)
            # novaFrase = frase[:startCampos2] + frase[zeroEsquerda+startCampos2:]
            print(campo[zeroEsquerda:])
            campo = campo[zeroEsquerda:]
    return campo

def removeDuplicata(arquivoEFD,numCampo):
    array=[]
    duplicados=[]
    for i,dados in enumerate(arquivoEFD):
        # if("02008289VINAGRE MARATA VINHO TINTO 12X500" in dados):
        #     print(dados)
        if(dados[numCampo] not in array):
            array.append(dados[numCampo])
            # print(array)
        else:
            #vetor simples com duplicados
            duplicados.append(dados[numCampo])
            
            del arquivoEFD[i]
            # for i,elemento in enumerate(dados):
            #     print(dados)
            #     dados[i] = ""
        
    for i,dados in enumerate(arquivoEFD):
        for i,campo in enumerate(dados[1:]):
            if("VINAGRE MARATA VINHO TINTO" in campo):
                print(dados)
            if("8289" in campo):
                print(dados)
            if(campo!="\n"):
                dados[i] = "|"+campo
            else:
                dados[i] = "|"
            # TODO FALTA FECHAR UM CAMPO
            # if(campo==):
            #     dados[i]="|"+campo+"|"
        # print(dados)
    with open("duplicados.csv",'w', encoding="iso-8859-1") as f:
        for line in duplicados:
            f.writelines(line + ",")   
    return arquivoEFD 