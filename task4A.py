import string

def character_word_count(text):
    
    f = open('Book1.txt', 'r')
        w = f.readlines()

        for line in w:
                res = line.lower().strip(string.punctuation + string.whitespace$
                reserve = reserve + res
         List = text.lower().split('.')
         counter = 0
         index = 0
         Dict = {}
         count = []
        for character in List:
           words = character.split()
        for word in words:
           index = words.index(word)
           countList.append(index)
        if word not in Dict:
            Dict[word] = list()
        else:
            Dict[word].append(index)
    
character_word_count()  
