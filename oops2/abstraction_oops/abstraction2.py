"""Here we are restricting user to use __search_job method outside the class"""


import logging
logging.basicConfig(filename="abstraction2.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s %(message)s')
class jobs:
    def __init__(self,name,qulification,age):
        self.__name=name
        self.__qulification=qulification
        self.__age=age


    def __search_job(self):
        try:
            if self.__qulification is 12 and  self.__age<21:
                logging.info(f"{self.__name} you are eligible for agniveer")
                return self.__name
            else:
                logging.info(f"{self.__name} you aree not eligible")

        except Exception as e:
            logging.info(e)

    def pankaj(self):
        logging.info(self.__search_job())


obj=jobs("vipin",12,18)
obj.pankaj()




