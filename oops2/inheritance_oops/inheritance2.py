import logging
from oops2.inheritance_oops.inheritance1 import ineuron

"""its gona store logging info of parent class logging file"""

class Teacher(ineuron):
    logging.info("we are only inheriting only the constructor of parent class which is already in a package")
    def __init__(self,course,internship,blog):
        super().__init__(course,internship,blog)
    def name_teacher(self):
        try:
            if self.course=="Data science":
                logging.info(f"Sudhanshu sir is the mentor of {self.course}")

        except Exception as e:
            logging.info(e)



obj=Teacher("Data science","ml","dl")
obj.name_teacher()