import random
import dicionario
import metodos as auditech

print(dicionario.dictTabelas)
arquivo = "efd_201702originalbrenda.txt"

def main():
    array=[]
    duplicados=[]
    novoArquivo = auditech.initArray(arquivo)
    for i,dados in enumerate(novoArquivo):
        if("02008289VINAGRE MARATA VINHO TINTO 12X500" in dados):
            print(dados)
        if(dados[2] not in array):
            array.append(dados[2])
            # print(array)
        else:
            duplicados.append(dados[2])
            del novoArquivo[i]
            # for i,elemento in enumerate(dados):
            #     print(dados)
            #     dados[i] = ""
        
    for i,dados in enumerate(novoArquivo):
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
        
    with open("testeRicardo.txt",'w', encoding="iso-8859-1") as f:
        for line in novoArquivo:
            f.writelines(line)

    with open("duplicados.csv",'w', encoding="iso-8859-1") as f:
        for line in duplicados:
            f.writelines(line + ",")
if __name__ == "__main__":
    main()



#14-08 first commit - ricardo
