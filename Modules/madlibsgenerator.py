import re


class Reader:
    def __init__(self,file):
        self.file = file
    
    def __str__(self):
        return self.file_reader_txt() 

    def file_reader_txt(self):
        text = ''
        with open(self.file, 'r',encoding='utf-8') as buffer:
            for line in buffer:
                text += line
        return text
    
class MadLibsGenerator(Reader):
    def __init__(self, file,user_text):
        super().__init__(file)
        self.user_text = user_text

    def func(self):
        file_text = str(Reader('text.txt'))
        underline = [_.start() for _ in re.finditer("_", file_text)] 
        file_text = list(file_text)

        for i in range(len(underline)):
            file_text[underline[i]] = self.user_text[i]
            
        return "".join(file_text)

            
        
        

        



