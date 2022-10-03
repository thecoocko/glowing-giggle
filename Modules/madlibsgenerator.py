
class Reader:
    def __init__(self,file):
        self.file = file
    
    def file_reader_txt(self):
        text = ''
        with open(self.file, 'r',encoding='utf-8') as buffer:
            for line in buffer:
                text += line
        return text
    
class MadLibsGenerator(Reader):
    def __init__(self, file,user_text):
        super().__init__(file)


