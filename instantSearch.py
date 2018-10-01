from fastDataStructure import InstantTree
import json
class InstantSearch:
      _filename = ""
      def __init__(self):
            print("InstantSearch Object Created")
      
      def loadData(self,filename):
            self._filename = filename
            self.ITree = InstantTree()
            self.insert("Saikrishna Mundrathi")
            self.insert("Saikrishna")
            self.insert("Jack Sparrow")
            self.insert("Master Luke")
            self.insert("Jack Dogge")
            self.insert("Black Knight")
            self.insert("Black Flag")
            print("Dumping Data")
            self.autoCompelete("Black")
            self._insertData()
            # self._checkString()
           
      def _checkString(self):
            file = open(self._filename)
            log= open("checklog.log","w+")
            lineCount = 0
            for line in file:
                  if lineCount==0: #skipping the header
                        lineCount+=1
                        continue
                  #replacing string with , ,, and removing trimming
                  line = line.replace(",,"," ").replace(","," ").replace(";","").replace("-","").strip() 
    
                  line = line.rstrip(".").strip()
                  if line == "":
                        pass
                  else:
                        resultSet = self.ITree.search(line,True)
                        log.write(line+" : "+str(resultSet)+"\n")

            file.close()
            log.close()


      def _getLongString(self):
            file = open(self._filename)
            lineCount = 0
            lineMax = 0
            for line in file:
                  if lineCount==0: #skipping the header
                        lineCount+=1
                        continue
                  #replacing string with , ,, and removing trimming
                  line = line.replace(",,"," ").replace(","," ").strip() 
                  if line == "":
                        pass
                  else:
                        if lineMax <len(line):
                              lineMax = len(line)
            file.close()
            return lineMax 

      def _insertData(self):
            file = open(self._filename)
            log= open("log.log","w+")
            lineCount = 0
            for line in file:
                  if lineCount==0: #skipping the header
                        lineCount+=1
                        continue
                  #replacing string with , ,, and removing trimming
                  line = line.replace(","," ").replace(",,"," ").replace(";","").replace("-","").replace("`","").replace("~","").strip() 
                  line = line.rstrip(".").replace('  ', ' ').strip()
                  if line == "":
                        pass
                  else:
                        self.insert(line)
                        log.write(str(lineCount)+" : "+line)
                        lineCount+=1
            log.close() 
            file.close()

      def insert(self,name):
            self.ITree.insert(name)

      def search(self,name):
            result = self.ITree.search(name,False)
            if(result==True):
                  res = []
                  res.append(name)
                  return res
            else:
                  return result
      
      def autoCompelete(self,name):
            result = self.ITree.search(name,True)
            if(result==False):
                  return []
            else:
                  return result