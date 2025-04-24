import random 
from collections import defaultdict

class MarkoveText:
    def__init__(self):

    self.model=defaultdict(list)

    def build_model(self,text,n=2):
        """
        Build a Markov chain model from the input text.
            `n` is the order of the model(2= bigram,3=trigram,etc.)"""
        words=text.spilt()
        for i in  range(len(words)-n):
            key=tuple(words[i:i+n])
            next_word=words[i+n]
            self.model[key].append(next_word)

    def generate_text(self,length=50)
        """
        Generate text of `length`"words using the build model."""
        if not self.model:
            return"Model is empty.Please build it with some text first."""
       
        start=random.choice(list(self.model.keys()))
        result=list(start)
        for_in range(length-len(start)):
       
        key=tuple(result[-len(start):])
        next_words=self.model.get(key)
        if not next_words:

            break 
        next_word =random.choice(next_words)
        result.append(next_word)
        return ''.join(result)
if __name__ == "__main__": 
    sample_text="""
 Once upon a time there was a brave knight who fought dragons. 
    The knight was strong and fearless. 
    Everyone in the kingdom admired the knight's courage and strength.
"""
composer=MarkoveText()
composer.build_model(sample_text,n=2) #Bigram model

generated =composer.generate_text(30)
print ("Generated Text:\n" ,generated)