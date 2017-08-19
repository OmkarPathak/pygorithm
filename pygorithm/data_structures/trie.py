class Node:
    def __init__(self, v, p=None, w=False):
        self.word = w #If the node represents the end of a word or not
        self.parent = p
        self.value = v
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node('') #The root of the trie is always empty

    def Insert(self, word):
        """
        Insert word in the trie. Starting from the root, move down the trie
        following the path of characters in the word. If the nodes for the word
        characters end, add them. When the last char is added, mark it as a
        word-ending node.
        """
        l = len(word)
        curr = self.root
        for i, c in enumerate(word):
            last = False
            if(i == l-1):
                #The last char of the word
                last = True

            if(c not in curr.children):
                curr.children[c] = Node(c, curr, last)
            elif(last):
                #c already exists, but as it is the last char of word,
                #it should now be flagged as a word in the trie.
                curr.children[c].word = True

            curr = curr.children[c]

    def Search(self, word):
        """
        Searches for given word in trie. We want to find the last node for the
        word. If we can't, then it means the word is not in the trie.
        """
        if self.FindFinalNode(word):
            return True
        else:
            return False

    def FindWords(self, prefix):
        """
        Find all words with the given prefix
        """
        v = self.FindFinalNode(prefix)
        wList = self.BuildWordList(v, prefix)
        if(v and v.word):
            #v exists and the prefix is itself a word; add it to the list.
            wList.append(prefix)

        return wList

    def FindFinalNode(self, word):
        """
        Returns the last node in given word. The process goes like this:
        Start from the root. For every char in word, go down one level.
        If we can't go down a level, then the word doesn't exist.
        If we do, and the current char is the last char of the word and
        the node we are currently at is a word, then we have found the given
        word.
        """
        curr = self.root
        l = len(word)

        for i, c in enumerate(word):
            if(c not in curr.children):
                #There is no prefix of cWord + c
                return None

            if(i == l-1):
                #Last char of word
                return curr.children[c]

            curr = curr.children[c]

        return None

    def BuildWordList(self, v, cWord):
        """
        Recursively builds the list of words.
            * v: Node to check
            * cWord : The word built up to v
        """
        if(not v):
            return None

        wList = []
        for i, k in v.children.items():
            tempWord = cWord + i

            if(k.word):
                #If the iterated prefix is a word, add it to the list
                wList.append(tempWord)

            #The list of words under tWord
            wList.extend(self.BuildWordList(k, tempWord))

        return wList
