def my_string_index(text, harf):
    
    for i in range(len(text)):
        
        if text[i]==harf:
            return i
        else:
            if i==len(text)-1:
                return (-1)
            else:
                i+=1
                