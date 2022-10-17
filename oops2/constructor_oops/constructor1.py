import logging

logging.basicConfig(filename="constructor.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')
class ineuron:
    logging.info("ineuron class conrtructor")
    try:
        def __int__(self,sunny,sudhanshu):
            self.sunny=sunny
            self.sudhanshu=sudhanshu
    except Exception as e:
        logging.info(e)

class student:
    logging.info("student class conrtructor")
    try:
        def __int__(self,vipin,ankit):
            self.vipin=vipin
            self.ankit=ankit
    except Exception as e:
        logging.info(e)

class internship:
    logging.info("internship class conrtructor")
    try:
        def __int__(self,data_science,python,big_data):
            self.data_science=data_science
            self.python=python
            self.big_data=big_data
    except Exception as e:
        logging.info(e)

class job:
    logging.info("job class constructor")
    try:
        def __int__(self,data_scientist,ml_engineer,python_developer):
            self.data_scientist=data_scientist
            self.ml_engineer=ml_engineer
            self.python_developer=python_developer

    except Exception as e:
        logging.info(e)

class blog:
    logging.info("blog class constructor")
    try:
        def __int__(self,python,ml,dl):
            self.python=python
            self.ml=ml
            self.dl=dl
    except Exception as e:
        logging.info(e)




