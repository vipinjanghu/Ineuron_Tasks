"""Here we are retricting user to _rollandbranch method into other .py files ,so we can say its an example of abstraction"""

import logging
logging.basicConfig(filename="abstraction1.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class student:
    logging.info("we are into parent class")
    def __init__(self,name,roll,branch):
        self._name=name
        self._roll=roll
        self._branch=branch
    def _rollandbranch(self):
        logging.info(f"roll no is : {self._roll} and branch is {self._branch}")





