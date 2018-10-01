#trie Data structure
class InstantNode:
      def __init__(self,MAXCHARSIZE):
            self.MAXCHARSIZE=MAXCHARSIZE
            self.child = [None]*MAXCHARSIZE
            self.value = ""
            self.isEndOfWord = False

class InstantTree:
      indexDist = {}
      letterDist = {}
      charCount = 0

      def __init__(self):
            self._generateDist()
            self.CHARSIZE = len(self.indexDist)+1
            # print(self.indexDist)
            # print(self.letterDist)
            self.root = self._getNode()

      #char index map
      def _generateDist(self):
            letter = 'a'
            for i in range(0,26):
                  self.indexDist[self.charCount] = chr(ord(letter)+i)
                  self.letterDist[chr(ord(letter)+i)] = self.charCount
                  self.charCount+=1
            letter = 'A'
            for i in range(0,26):
			self.indexDist[self.charCount] = chr(ord(letter)+i)
			self.letterDist[chr(ord(letter)+i)] = self.charCount
			self.charCount+=1
            
            # letter = '.' #including special characters
            # self.letterDist[chr(ord(letter)+i)] = self.charCount
            # self.charCount+=1
            letter = ' '
            self.indexDist[self.charCount] = letter
            self.letterDist[letter] = self.charCount
            self.charCount+=1

            letters = '0123456789'
            length = len(letters)
            for i in range(length):
                  letter = letters[i]
                  self.indexDist[self.charCount] = letter
                  self.letterDist[letter] = self.charCount
                  self.charCount+=1
            letters = "@/:.!#$%^&*()_+=-'"
            length = len(letters)
            for i in range(length):
                  letter = letters[i]
                  self.indexDist[self.charCount] = letter
                  self.letterDist[letter] = self.charCount
                  self.charCount+=1


      def _getNode(self):
            return InstantNode(self.CHARSIZE)

      def _charToIndex(self,ch):
            if ch in self.letterDist.keys():
                  # print(self.letterDist[ch])
                  return self.letterDist[ch]
            elif ch == ' ':
                  return 100
            else:
			self.indexDist[self.charCount] = ch
			self.letterDist[ch] = self.charCount
			self.charCount+=1
			return self.indexDist[ch]
      
      def _indexToChar(self,idx):
            if idx in self.indexDist.keys():
                  # print(self.indexDist[idx])
                  return self.indexDist[idx]
            elif idx == 100:
                  return ' '
      
      def insert(self,key): 
            node = self.root 
            length = len(key) 
            original = key
            key = key.lower()
            # print(key)
            for i in range(length):
                  # print(key[i])
                  charIndex = self._charToIndex(key[i])
                  if not node.child[charIndex]:
                        node.child[charIndex] = self._getNode()
                  node = node.child[charIndex]
                  node.value = original
            node.isEndOfWord = True


      def search(self, key, autocomplete):
        node = self.root 
        length = len(key) 
        original = key
        key = key.lower()
        for i in range(length): 
            charIndex = self._charToIndex(key[i]) 
            if not node.child[charIndex]: 
                return False
            if i == len(key)-1 and autocomplete==True:
                  node = node.child[charIndex]
                  node.value = original
                  nameList = []
                  nameList = self._autocompelete(node,key,nameList,autocomplete)
                  return nameList
            node = node.child[charIndex] 
            node.value = original
        return node != None and node.isEndOfWord 

      def _autocompelete(self,root,key,nameList,autoFlag):
            if autoFlag == True and len(nameList) >=15:
                  return nameList
            if root.isEndOfWord == True:
                  nameList.append(root.value)
            for i in range(0,self.charCount):
			nextIndex = root.child[i]
			if nextIndex is not None:
				self._autocompelete(nextIndex,key+ self._indexToChar(i),nameList,autoFlag)
            return nameList


#referance https://en.wikipedia.org/wiki/Trie