import logging


logging.basicConfig(filename="inhertance1.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')


class ineuron:
    logging.info("we are into ineuron")
    def __init__(self,course,internship,blog):
        self.course=course
        self.internship=internship
        self.blog=blog
    def COURSE(self):
        try:
            logging.info("we are into course tab")
            l = {"Data science": 17000, "Python": 5000, "java": 40000, "Big data": 10000}
            x=[]
            for i in l:
                if i== self.course:
                    x.append(i)
                    logging.info(f"your {self.course} cousre fee is {l[i]} ")

            return x
        except Exception as e:
            logging.info(e)

    def JOB(self):
        try:
            logging.info("We are into job portal")
            job = {"Data science": ["python developer", "data scientist", "ml engineer", "data analyst", "dl engineer"],
                   "Python": "python developer", "java": ["java developer", "java web developer"],
                   "Big data": "data analyst"}
            j=self.COURSE()
            x=[]
            for y in job.keys():
                if y==j[0]:
                    logging.info(f" You can enter all the jobs option{job[y]}")
                    x.append(job[y])
            return x
        except Exception as e:
            logging.info(e)


class Student(ineuron):
    logging.info("We are into student class")
    def __init__(self,course,internship,blog,name,marks):
        super().__init__(course,internship,blog)
        self.name=name
        self.marks=marks
    try:
        def student_type(self):
            if self.marks<70:
                logging.info(f"Student {self.name} is average student")
            else:
                logging.info(f"Student {self.name} is above average student")

    except Exception as e:
        logging.info(e)



obj1=Student("Data science","ml","dl","vipin",40)
obj1.JOB()