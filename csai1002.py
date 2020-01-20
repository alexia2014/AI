
humanbeing = "human"
graders = "graders"

def human(sentence):
    res = True
    l = len(sentence)
    i = 0
    m = 0
    while(i+1 < l and m+1 < 5):
        if((sentence[i] == humanbeing[m] and sentence[i+1] == humanbeing[m+1]) or (sentence[i] == graders[m] and sentence[i+1] == graders[m+1])):
            res = False
            m+=1
        else:
            m = 0
        i+=1
    return res
    
sentence = input("Enter sentence:")
print(human(sentence)) 


