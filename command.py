class Screen(object):
    def __init__(self, text=''):
        self.text = text
        self.clip_board = ''
        
    def cut(self, start=0, end=0):
        self.clip_board = self.text[end:]
        self.text = self.text[:start] + self.text[end:]
        
    def paste(self, offset=0):
        self.text = self.text[:offset] + self.clip_board + self.text[offset:]
        
    def clear_clipboard(self):
        self.clip_board = ''
        
    def length(self):
        return len(self.text)
        
    def __str__(self):
        return self.text
        

# screen command interface
class ScreenCommand:
    def __init__(self, screen):
        self.screen = screen
        self.previous_state = screen.text
        
    def execute(self):
        pass
    
    def undo(self):
        pass
        
        
        
class CutCommand(ScreenCommand):
    def __init__(self, screen, start=0, end=0):
        super().__init__(screen)
        self.start = start
        self.end = end
        
    def execute(self):
        self.screen.cut(start=self.start, end=self.end)
        
    def undo(self):
        self.screen.clear_clipboard()
        self.screen.text = self.previous_state
        

class PasteCommand(ScreenCommand):
    def __init__(self, screen, offset=0):
        super().__init__(screen)
        self.offset = offset
        
    def execute(self):
        self.screen.paste(offset=self.offset)
        
    def undo(self):
        self.screen.clear_clipboard()
        self.screen.text = self.previous_state
        

class ScreenInvoker:
    def __init__(self):
        self.history = []
        
    def store_and_execute(self, command):
        command.execute()
        self.history.append(command)
        
    def undo_last(self):
        if self.history:
            self.history.pop().undo()
            
    
def testing():
    screen = Screen('hello world')
    print('inisiasi screen                 ->', screen.__str__())
    cut = CutCommand(screen, start=5, end=11)
    client = ScreenInvoker()
    client.store_and_execute(cut)
    print('perintah client untuk cut       ->', screen.__str__())
    paste = PasteCommand(screen, offset=0)
    client.store_and_execute(paste)
    print('perintah client untuk paste     ->', screen.__str__())
    client.undo_last()
    print('perintah client untuk undo      ->', screen.__str__())
    client.undo_last()
    print('perintah client untuk undo lagi ->', screen.__str__())
    
    
    
if __name__ == '__main__':
    testing()    
    
    
    
    
    
    
    
    
    
        
        
        
    
    
    
    
    
        