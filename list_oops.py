#Questions

# l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
# 1 . Try to reverse a list
# 2. try to access 234 out of this list
# 3 . try to access 456
# 4 . Try to extract only a list collection form list l
# 5 . Try to extract "sudh"
# 6 . Try to list all the key in dict element avaible in list
# 7 . Try to extract all the value element form dict available in list


import logging

logging.basicConfig(filename="list_oops_logging", level=logging.DEBUG,
                    format='%(levelname)s %(asctime)s %(name)s  %(message)s')


class custom_list:
    def __init__(self, list_data):
        self.list_data = list_data

    def reverce_list(self):

        """it will return reverse order of a list and a tuple"""
        try:
            logging.info("Revercing the list :%s", self.list_data)
            x2 = self.list_data[::-1]
            logging.info(f"Reversed list :{x2}")
            return x2
        except Exception as e:
            logging.info(e)

    def extract_number(self,number):
        """ it will return a list of number which we want to extract"""
        try:
            logging.info("Extracting number")
            x2=[]
            for i in self.list_data:
                if type(i)==list or type(i)==tuple:
                    for j in i:
                        if j==number:
                            x2.append(j)
                elif type(i)==dict:
                    for j,k in i:
                        if j==number:
                            x2.append(j)
                        elif k==number:
                            x2.append(k)
                else:
                    if i==number:
                        x2.append(i)
            logging.info("Number Extracted:%s",x2)
            return x2
        except Exception as e:
            logging.info(e)

    def extract_list(self):
        """it will return a list of extracted list from a list"""

        try:
            logging.info("extracting list from a list")
            x2 = []
            for i in self.list_data:
                if type(i)==list:
                    x2.append(i)
                elif type(i)==tuple:
                    for j in i:
                        if type(j)==list:
                            x2.append(j)
                elif type(i)==dict:
                    for j in i.values():
                        if type(j)==list:
                            x2.append(j)
            logging.info("Extraction completeed %s", x2)
            return x2
        except Exception as e:
            logging.info(e)

    def extract_string(self, string):
        """it will return a list of a extracted word"""
        try:
            logging.info("Extracting string ")
            x2 = []
            for i in self.list_data:
                if type(i)==list or type(i)==tuple:
                    for j in i:
                        if j==string:
                            x2.append(j)
                elif type(i)==dict:
                    for j,k in i.items():
                        if j==string :
                            x2.append(j)
                        elif k==string:
                            x2.append(k)
                else:
                    if i==string:
                        x2.append(i)
            logging.info("Extraction completeed  :%s ", x2)
            return x2
        except Exception as e:
            logging.info(e)


    def extract_keys(self):
        """it will return list of all the keys of dictionary"""
        try:
            logging.info("key extraction of dictionary")
            x2=[]
            for i in self.list_data:
                if type(i)==dict:
                    for j in i.keys():
                        x2.append(j)
            logging.info("Key extracted:%s", x2)
            return x2

        except Exception as e :
            logging.info(e)

    def extract_value(self):
        """it will return list of all the values of dictionary"""
        try:
            logging.info("value extraction of dictionary")
            x2=[]
            for i in self.list_data:
                if type(i) == dict:
                    for j in i.values():
                        x2.append(j)
            logging.info("Value extracted:%s",x2)
            return x2
        except Exception as e :
            logging.info(e)

