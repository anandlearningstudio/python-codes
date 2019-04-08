# Functional Approach

s = "This is the sentence"

def split_a_sentence(sentence):
    
    word_list = []
    start = 0
    prev_space = False
    
    for i in range(len(s)):

        if s[i] == ' ':

            if prev_space == False and i > 0:

                word_list.append(s[start:i])

            start = i + 1

            prev_space = True

        else:

            prev_space = False

    if prev_space==False:
        
        word_list.append(s[start:])
        
    return word_list

def reverse_the_list(word_list):
    
    sentence = ''
    count_words = len(word_list)
    index = count_words - 1
    
    while index >= 0:
        
        sentence += word_list[index]
        sentence += ' '
        index -= 1
        
    return sentence
        
reverse_the_list(split_a_sentence(s))

# Object Oriented Approach

class Reverse_the_Sentence:

    def split_a_sentence(self, sentence):

        self.word_list = []
        start = 0
        prev_space = False

        for i in range(len(s)):

            if s[i] == ' ':

                if prev_space == False and i > 0:

                    self.word_list.append(s[start:i])

                start = i + 1

                prev_space = True

            else:

                prev_space = False

        if prev_space==False:

            self.word_list.append(s[start:])

        return self.word_list

    def reverse_the_list(self, word_list):

        self.sentence = ''
        self.word_list = word_list
        count_words = len(self.word_list)
        index = count_words - 1

        while index >= 0:

            self.sentence += self.word_list[index]
            self.sentence += ' '
            index -= 1

        return self.sentence
        
