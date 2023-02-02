
from tkinter import *

def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    
    return storeObj
 

 
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Multiply')
        self.story=''
    

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
          justify='right'
          , bd=30, bg="powder blue").pack(side=TOP,
                                          expand=YES, fill=BOTH)
        def button(source, side, text, command=None, a=int()):
            storeObj = Button(source, text=text, command=command)
            storeObj.pack(side=side, expand = YES, fill=BOTH)                
            self.story= str(text) +'\n'+self.story  

            return storeObj, text,a

        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''),0)
        
        
        
        for numButton in ("789", "456", "123", "*0."):
         FunctionNum = iCalc(self, TOP)
         
         for iEquals in numButton:
            
            
            a= button(FunctionNum, LEFT, iEquals, lambda
                storeObj=display, q=iEquals: storeObj
                   .set(storeObj.get() + q), 1)
            
            
            if display is True:
                self.story=a[1]+self.story
               

            
 
        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':

                btniEquals = button(EqualButton, LEFT, iEquals,0)
                btniEquals[0].bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')
 
 
            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                    (storeObj.get() + s),0)
        
        storyButton = iCalc(self, TOP)
        ichar = "Story"

        button(storyButton, LEFT, ichar,lambda storeObj=display, s=' %s ' % self.story: storeObj.set
                                    (storeObj.get() + s))
    def calc(self, display):
            try:
                display.set(eval(display.get()))
                self.story=str(display.set(eval(display.get())))
            except:
                display.set("ERROR")
 
 
if __name__=='__main__':
 app().mainloop()