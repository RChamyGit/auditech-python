with open("lists.txt",'r',encoding="UTF-8") as f:
    novoArquivo = open("bulk.txt",'w+')
    for x in f.readlines():
        if("Reg_" in x):
            
            novoArquivo.write("            if(reg_"+x[18:22]+"s.Count > 0) {\n")
            novoArquivo.write("                        try\n")
            novoArquivo.write("                        {\n")
            
            novoArquivo.write("                            // report \n")
            novoArquivo.write("                            App.Current.Dispatcher.Invoke((Action)delegate\n")
            novoArquivo.write("                            {\n")
            novoArquivo.write("                                textblockBlocoAtual.Text = \"bulk "+x[18:22]+"\";\n")
            novoArquivo.write("                            });\n")
            novoArquivo.write("                            await context.BulkInsertAsync(reg_"+x[18:22]+"s);\n")
            
            novoArquivo.write("                        }\n")
            novoArquivo.write("                        catch (Exception ex)\n")
            novoArquivo.write("                        {\n")
            novoArquivo.write("                            throw;\n")
            novoArquivo.write("                        }\n")
            novoArquivo.write("                 }\n")

with open("lists.txt",'r',encoding="UTF-8") as f:    
    novoArquivo = open("dbset.txt",'w+')
    for x in f.readlines():
        if("Reg_" in x):
            novoArquivo.write("\t\tpublic DbSet<Reg_"+x[18:22]+"> Reg_"+x[18:22]+"s { get; set; }\r")
with open("lists.txt",'r',encoding="UTF-8") as f:    

    novoArquivo = open("clearTables.sql", "w+")
    for x in f.readlines():
        print(x)
        novoArquivo.write("delete from T01_REG"+x[18:22]+";\n")

