import os

class internal:
    @staticmethod
    def find_file(filename, directory):
        try:
            return os.walk(filename, directory)
        except FileNotFoundError:
            return False
        else:
            return True

    @staticmethod
    def searchdir(filename, directory):
        for root, dirs, files in os.walk(directory):
            if filename in files:
                return os.path.join(root, filename)
        return None
    
    @staticmethod
    def createf(filename, directory):
        try:
            if directory == "-sl":
                path = filename  # aktuelles Verzeichnis
            else:
                path = os.path.join(directory, filename)

            with open(path, "x") as f:
                pass  # Datei wird erstellt

            return True
        except FileExistsError:
            return False
        except FileNotFoundError:
            return False
        
    @staticmethod
    def ifexist(filename, directory):
        if directory == "-sl":
            path = filename
        else:
            path = os.path.join(directory, filename)

        return os.path.exists(path)
    
    @staticmethod
    def timer(tie):
        import time
        seconds = 0
        while seconds < tie:
            time.sleep(1)
            seconds = seconds + 1

class lister:
    @staticmethod
    def add(listname, addable):
        listname.append(addable)
    
    @staticmethod
    def delete(listname, deletable):
        listname.remove(deletable)
    
    @staticmethod
    def inlist(listname, searched):
        if searched in listname:
            return True
        elif searched not in listname:
            return False
        else:
            return False
    
class gui:
    def all(self, drawpx, openbutton, changepara):
        self.drawpx
        self.openbutton
        self.changepara

class var:
    def show(var):
        print(var)
        return var

    def compare(var1, var2):
        if var1 < var2:
            return "Smaller"
        elif var1 > var2:
            return "Bigger"
        elif var1 == var2:
            return "Same"
        else:
            return "None"
        
    def call(var):
        return var
        
class mathing:
    def square(num):
        return num * num
    
    def tible(num, times):
        oldnum = num
        amt = 1
        times = int(times)
        amt = int(amt)
        oldnum = int(oldnum)
        num = int(num)

        while times > amt:
            num = num * oldnum
            amt = amt + 1
        sum = num
        return sum
    
    def randomize(lowest, highest, numamt, numway):
        import random as r

        amt = 0
        NUMBERS = []

        if highest < 1:
            while numamt > amt:
                if numway != "complete":
                    num = r.random()
                    num = int(num)

                    if num > highest:

                        while num > highest:
                            num = r.random()
                        NUMBERS.append(num)

                    else:
                        NUMBERS.append(num)

                elif numway == "complete":
                    num = r.random()
                    num = int(num)

                    if num > highest:
                        while num > highest:
                            num = r.random()
                        num = round(num)
                        NUMBERS.append(num)

                    else:
                        num = round(num)
                        NUMBERS.append(num)
            return NUMBERS
        
        if highest < 10:
            while numamt > amt:
                num = r.random()
                num = int(num)

                if num > highest:
                    while num > highest:
                        num = r.random()
                        num = num * 10
                        num = round(num)
                    NUMBERS.append(num)

                else:
                    num = num * 10
                    num = round(num)
                    NUMBERS.append(num)
            return NUMBERS
                
        if highest < 100:
            while numamt > amt:
                num = r.random()
                num = num * 100
                num = round(num)
                print(num)
                num = int(num)

                if num > highest:
                    while num > highest or num == 0:
                        num = r.random()
                        num = num * 100
                        num = round(num)
                        print(num)
                    NUMBERS.append(num)

                else:
                    NUMBERS.append(num)

                amt += 1
            return NUMBERS

        if highest < 1000:
            while numamt > amt:
                num = r.random()
                num = int(num)

                if num > highest:
                    while num > highest:
                        num = r.random()
                        num = num * 1000
                        num = round(num)
                    NUMBERS.append(num)

                else:
                    num = num * 1000
                    num = round(num)
                    NUMBERS.append(num)
            return NUMBERS

    def tries(snum, tries="infinite"):
        import random as r

        print("DEBUG snum in tries =", snum)

        trynum = 0

        while True:
            trynum += 1
            num = r.randint(0, snum)

            if num == snum:
                return trynum

            if tries != "infinite" and trynum >= tries:
                return None

class itpec:

    @staticmethod
    def getip():
        
