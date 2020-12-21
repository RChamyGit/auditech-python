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
f = open("idSeqs.cs", "w+")

table_array = []
for row in cursor:
    table_array.append(row.TABLE_NAME)
    print(row.TABLE_NAME)
    f.write("\t\t\tidSeqs.Add(\"REG_"+row.TABLE_NAME[-4:]+"\", 0);\n")

f.close()

# using (AuditechDBContext context = new AuditechDBContext())
#                 {
#                     if (context.Reg_0150s.FirstOrDefault() != null)
#                         _idSeq_REG0150 = context.Reg_0150s.FirstOrDefault(p => p.ID_0150 == context.Reg_0150s.Max(x => x.ID_0150)).ID_0150;
#                 }