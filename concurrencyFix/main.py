import pyodbc
import os
import sys

def pegaBanco():
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=localhost\SQLEXPRESS;'
                            'Database=Auditechbd;'
                            'Trusted_Connection=yes;')
        
        return conn.cursor()
    except pyodbc.Error as ex:
        print("pyodbc error!!!")
        print(ex)
        conn.close()

cursor = pegaBanco()
cursor.execute("SELECT * FROM Auditechbd.information_schema.tables WHERE TABLE_TYPE= "+"'BASE TABLE' AND TABLE_NAME LIKE ('T01_REG%') ORDER BY TABLE_NAME")
f = open("dbContexts.cs", "w+")

table_array = []
for row in cursor:
    table_array.append(row.TABLE_NAME)
    print(row.TABLE_NAME)
    f.write("\tusing (AuditechDBContext context = new AuditechDBContext())\n")
    f.write("\t{\n")
    f.write("\t\tif (context.Reg_"+row.TABLE_NAME[-4:]+"s.Any() != null)\n")
    f.write("\t\t\t_idSeq_"+row.TABLE_NAME[-7:]+" = context.Reg_"+row.TABLE_NAME[-4:]+"s.FirstOrDefault(p => p.ID_"+row.TABLE_NAME[-4:]+" == context.Reg_"+row.TABLE_NAME[-4:]+"s.Max(x => x.ID_"+row.TABLE_NAME[-4:]+")).ID_"+row.TABLE_NAME[-4:]+";\n")
    f.write("\t}\r\n")

# using (AuditechDBContext context = new AuditechDBContext())
#                 {
#                     if (context.Reg_0150s.FirstOrDefault() != null)
#                         _idSeq_REG0150 = context.Reg_0150s.FirstOrDefault(p => p.ID_0150 == context.Reg_0150s.Max(x => x.ID_0150)).ID_0150;
#                 }