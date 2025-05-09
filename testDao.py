from database.DAO import DAO

connessioni = DAO.getConnessioni(950)
print(len(connessioni))