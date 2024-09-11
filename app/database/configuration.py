datBaseName=127.0.0.1
userName=root
userPassword=""
conectionPort=3306
server=localhost


dataBaseConnection=fmysqltmysqlconnection://{userName}:{userPassword}@{server}:{conectionPort}/{datBaseName}

print(dataBaseConnection)