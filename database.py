import mysql.connector

class DataBaseConnector(object):
  _instance = None
  def __new__(class_, *args, **kwargs):
    if not isinstance(class_._instance, class_):
        class_._instance = object.__new__(class_, *args, **kwargs)
    return class_._instance

  def __init__(self) -> None:
    self.mydb = mysql.connector.connect(
    host="balrp5rv3xzbtemelvde-mysql.services.clever-cloud.com",
    user="uyjxibr8rj8jzgau",
    password="1KgCpCdrO1mDUNz7xSxc",
    database="balrp5rv3xzbtemelvde")

  
  
  def insertInputData(self,email,input):
    mycursor = self.mydb.cursor()
    sql = "INSERT INTO keyboard_input (email,input) VALUES(%s,%s)"
    val = (email, input)
    mycursor.execute(sql,val)
    self.mydb.commit()

  '''
  def allreadyExisist(self,email):
    sql = "SELECT input FROM `keyboard_input` where email=%s"
    self.mycursor.execute(sql,email)
    result = self.mydb.fetchall()
    if len(result) > 0:
      return True
    return False'''








