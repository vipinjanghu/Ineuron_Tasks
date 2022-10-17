import logging
logging.basicConfig(filename="inheritance3.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class student:
    logging.info("we are into parent class")
    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch
    def _rollandbranch(self):
        logging.info(f"roll no is : {self._roll} and branch is {self._branch}")



class ineuron(student):
    def __init__(self,name,roll,branch,):
        super().__init__(name,roll,branch)

    def displaydetail(self):
        logging.info(self._name)
        logging.info(self._rollandbranch())


obj=ineuron("vipin",25,"data science")
obj.displaydetail()