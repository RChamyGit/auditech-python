import os

file = open("blocos a verificar - inserir - efd.txt" , "r")
tabelas = file.readlines()
tabelas = [str(x).rstrip() for x in tabelas]

f = open("clearTables.sql", "w+")

for x in tabelas:
    print(x)
    f.write("delete from T01_REG"+x+";\n")

