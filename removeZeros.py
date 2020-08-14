import random


dictTabelas = ["|0200|","|C170|","|H010|"]
#0200 = campo 2 
#H010 = campo 2

#C170 = campo 3 


# TODO
# pegar o array com todas os campos[2]
# pegar o ultimo campos[2] lido
# iterar o elemento lido atual no array e procurar por elemento ja existente
# se ja existir, gerar um novo, se nao existir, append
# apos gerar um novo random , verificar se já existe no array antes de um final append
# continue

def verificaID(frase,start,end):
    
    
    print(frase)
    print(frase[start:end])
    print(int(frase[start:end-1]))
    for caracter in frase:
        print(frase[start:end])
        print(frase)
        alteracao = str(random.randrange(1,2^32-1))
        print(alteracao)
    
    frase = frase[:start] + alteracao + frase[end:]
    print(frase)
    
    if (1 == 2):
        array.append(int(frase[startCampos2:fimCampos2-1]))
        return array
    else:
        pass

array=[]

with open("efd_201702 - AJUSTADO - 0200.txt",'r', encoding="iso-8859-1") as f:
    newline=[]
   
    for frase in f.readlines():
        
        contBarra = 0
        i = 0
        if any(x in frase for x in dictTabelas):
            for caracter in frase:
                i+=1
                if(caracter == "|"):
                    contBarra+=1
                    if("|0200|" in frase or "|H010|" in frase):
                        if(contBarra==2):
                            startCampos2 = i
                        elif(contBarra==3):
                            fimCampos2 = i
                            
                    else:
                        if(contBarra==3):
                            startCampos2 = i
                        elif(contBarra==4):
                            fimCampos2 = i
                zeroEsquerda = 0    
            print(frase[startCampos2:fimCampos2-1])
            verificaID(array,frase,startCampos2,fimCampos2)
            
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
                novaFrase = frase[:startCampos2] + frase[zeroEsquerda+startCampos2:]
                print(novaFrase)
                frase = novaFrase
        newline.append(frase)
        for elemento in array:
            print(array)
with open("testeRicardo.txt",'w', encoding="iso-8859-1") as f:
     for line in newline:
         f.writelines(line)





#14-08 first commit - ricardo
