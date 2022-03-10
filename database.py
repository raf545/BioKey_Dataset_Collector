import mysql.connector

class DataBaseConnector(object):
  _instance = None
  def __new__(class_, *args, **kwargs):
    if not isinstance(class_._instance, class_):
        class_._instance = object.__new__(class_, *args, **kwargs)
    return class_._instance

  def __init__(self) -> None:
    self.mydb = mysql.connector.connect(
    host="biokedataset.cyv9hubfihqq.us-east-1.rds.amazonaws.com",
    user="admin",
    password="7C034CBD7CD4",
    database="biokeyDataset")

  
  
  def insertInputData(self,email,input):
    mycursor = self.mydb.cursor()
    sql = "INSERT INTO inputdata (email, input) VALUES (%s,%s);"
    val = (email, input)
    mycursor.execute(sql,val)
    self.mydb.commit()









