import mysql.connector 
usuario = input('Usuário do MySQL:')
senha = input('Senha MySQL:')
con = mysql.connector.connect(host = 'localhost' , database = 'projeto' , user = usuario , password  = senha)
#isso serve para conectar com o mysql

cursor = con.cursor()

comando_sql = cursor.execute("create table pessoas (nome varchar(20) not null , email var(20) not null, primary key email)")

#isso serve para criar tabela 