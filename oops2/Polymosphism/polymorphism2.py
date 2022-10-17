import logging


logging.basicConfig(filename="polymosrphism2.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

class string:
    def __init__(self,name):
        self.name=name
    try:
        def custum_len(self):
            """return the lenght of string"""
            logging.info(f"length of string is :{len(self.name)}")
    except Exception as e:
        logging.info(e)

class lis:
    def __init__(self,obj):
        self.obj=obj
    try:
        def custum_len(self):
            """return length of lists"""
            logging.info(f"lenght of list :{len(self.obj)}")
    except Exception as e:
        logging.info(e)

