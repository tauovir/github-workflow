
class CommonCase:

    def __init__(self) -> None:
        pass

    def factorial(self,num : int) -> int:
        if num == 1 or num == 0:
            return 1
        else:
            return num * self.factorial(num-1)
    
    def __remove_special_char(self,word : str) -> str:
        special_chars = ['#','@','-','$','!']
        resp = ''
        for ch in word:
            if ch in special_chars:
                continue
            resp = resp + ch
        return resp



    def clean_string(self, text:str) -> str:
        resp = ''
        for sub in text.split():
            clean_word = self.__remove_special_char(word = sub)
            resp = resp + ' '+ clean_word
        return resp


obj = CommonCase()
resp = obj.factorial(num=6)
resp2 = obj.clean_string(text = 'Taukir! kha#n')
print(resp)
print(resp2)
