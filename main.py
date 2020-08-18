import random
import dicionario as dicionario
import metodos as auditech

print(dicionario.dictTabelas)
arquivo = "efd_201702originalbrenda.txt"

#TODO criar uma classe EFD com os metodos 

def main():
    
    dadosEFD = auditech.initArray(arquivo)

    idCampo = 2
    dadosEFD = auditech.removeDuplicata(dadosEFD,idCampo)

    with open("testeRicardo.txt",'w', encoding="iso-8859-1") as f:
        for line in dadosEFD:
            f.writelines(line)
    


if __name__ == "__main__":
    main()



#14-08 first commit - ricardo
