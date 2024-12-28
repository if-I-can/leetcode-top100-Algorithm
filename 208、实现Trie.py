"""
这个题还是很有意思的，前缀树是通过嵌套空字典形成的。 记住就好了，挺好记的。
"""
class Trie(object):     

    def __init__(self):
        self.tri = {}
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        Node = self.tri
        for char in word:
            if char not in Node:
                Node[char] = {}
            Node = Node[char]
        Node["#"] = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        Node = self.tri
        for char in word:
            if char not in Node:
                return False
            Node = Node[char]
        return '#' in Node
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        Node = self.tri
        for char in prefix:
            if char not in Node:
                return False
            Node = Node[char]

        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)