import tkinter as tk
from tkinter import messagebox as MS
import datetime




class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.master = master
        self.f = open('dat.txt', 'r')
        self.b=[]
        self.base()
        self.vence()
       
        
        
        self.droga = tk.Entry(width='12',font=('arial black',16))
        self.droga.pack(side='left')
        
        self.laboratorio = tk.Entry(width='12',font=('arial black',16))
        self.laboratorio.pack(side='left')
        self.cantidad = tk.Entry(width='8',font=('arial black',16))
        self.cantidad.pack(side='left')
        self.dosis = tk.Entry(width='5',font=('arial black',16))
        self.dosis.pack(side='left')
        self.mesvencimiento = tk.Entry(width='15',font=('arial black',16))
        self.mesvencimiento.pack(side='left')
        self.anovencimiento = tk.Entry(width='15',font=('arial black',16))
        self.anovencimiento.pack(side='left')
        # Create the application variable.
        self.contents1 = tk.StringVar()
        self.contents2 = tk.StringVar()
        self.contents3 = tk.StringVar()
        self.contents4 = tk.StringVar()
        self.contents5 = tk.StringVar()
        self.contents6 = tk.StringVar()
        # Set it to some value.
        self.contents1.set("droga")
        self.contents2.set("laboratorio")
        self.contents3.set("dosis")
        self.contents4.set("cantidad")
        self.contents5.set("mesvencimiento")
        self.contents6.set("anovencimiento")
        # Tell the entry widget to watch this variable.
        self.droga["textvariable"] = self.contents1
        self.contents1.set("droga")
        self.laboratorio["textvariable"] = self.contents2
        self.contents2.set("laboratorio")
        self.dosis["textvariable"] = self.contents3
        self.contents3.set("dosis")
        self.cantidad["textvariable"] = self.contents4
        self.contents4.set("cantidad")
        self.mesvencimiento["textvariable"] = self.contents5
        self.contents5.set("mes vencimiento")
        self.anovencimiento["textvariable"] = self.contents6
        self.contents6.set("año vencimiento")
        # Tell the entry widget to watch this variable.
        self.create_widgets()
      #  self.droga["textvariable"] = self.contents1

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        
        

    

    def create_widgets(self):
        self.hi_there = tk.Button(self,font=('arial black',18),relief='groove',bd='10')
        self.hi_there["text"] = "ALMACENAR MEDICAMENTO"
        self.hi_there["command"] = self.datos
        self.hi_there.pack(side="left")
        self.stock = tk.Button(self, text="BUSCAR STOCK",font=('arial black',18),bd='10',relief='groove', bg="green",
                              command=self.stock)
        self.stock.pack(side="left")
        self.quit = tk.Button(self, text="CERRAR Y GUARDAR", bg="red",font=('arial black',18),bd='10',relief='groove',
                              command=self.goku)
        self.quit.pack(side="right")
        
    def goku(self):
        self.reload()
        self.master.destroy()


    def reload(self):
        self.f=open('dat.txt', 'r')
        self.base()
        mem1=[]
        mem2=[]
        for i in range(len(self.b)):
            mem2.append(self.b[i])
            mem1.append(self.b[i])
        o=0
        self.f=open('dat.txt', 'w')
        for i in range(len(mem1)-1):
            i=i-o
            
            if mem1[i][0]==mem1[i+1][0]:
                mem1.pop(i)
                o=o+1
        for i in range(len(mem1)):
            cant=0
            for j in range(len(mem2)):
                if mem2[j][0]==mem1[i][0]:
                   
                    cant=cant+int(mem2[j][4])
            mem3=[mem2[i][0],mem2[i][1],mem2[i][2],mem2[i][3],str(cant),mem2[i][5],mem2[i][6]]    


            for l in range(len(mem3)):
                d=str(mem3[l])+'\t'
                self.f.write(d)
            self.f.write('\n')        
        self.f=open('dat.txt', 'r')
        self.base()
    def say_hi(self):
        try:
            a=[self.contents1.get(),self.contents2.get(),self.contents3.get(),
            int(self.contents4.get()),int(self.contents5.get()),int(self.contents6.get())]
            return(a)
        except ValueError:
            print(MS.showinfo(message='HAY UN ERROR EN LOS DATOS INGRESADOS \n RESPETAR EL ORDEN Y TIPO DE DATO!!!', title='ERROR EN LOS DATOS INGRESADOS'))
    def stock(self):
        a=self.contents1.get()
        c=0
      
        r=[]
        t=str()
        
        for i in range(len(self.b)) :
            r.append([self.b[i][1],self.b[i][2],self.b[i][3]])
           
            if a==r[-1][0] :
                e=True
                t=t+'\n'+str(self.b[i][4])+' CAJAS DE LA DROGA :'+self.b[i][1]+' DEL LABORATORIO '+self.b[i][2]+ ' DE LA FORMA '+str(self.b[i][3])+'\n'
                
        
            if i==len(self.b)-1 and e==False:
                print(MS.showinfo(message='NO HAY STOCK DE: '+a, title=a))
            
            elif i==len(self.b)-1 and e==True:
           
                print(MS.showinfo(message=t, title=a))     
                
    
    def datos(self):

        a=self.say_hi()
      
        r=0
    
        for j in range(len(self.b)):

            
            if a[0+r]==self.b[j][1] and a[1+r]==self.b[j][2] and a[2+r]==self.b[j][3] and a[4+r]==int(self.b[j][5]) and a[5+r]==int(self.b[j][6]) and r==0:
                a.insert(0,self.b[j][0])
                r=1
             
            elif j==len(self.b)-1 and r!=1:
                a.insert(0,str(int(self.b[-1][0])+1))
                r=1       
        if len(self.b)==0:
                a.insert(0,0)
                
        for i in range(len(a)):
            
            d=str(a[i])+'\t'
            self.f.write(d)
        self.f.write('\n')
        self.b.append(a)
        
        self.reload()
        h=0
        for i in range(len(self.b)):
            if a[0]==self.b[i][0]:
                u=self.b[i]  
                h=1  
            elif h==0 :
                u=a
        print(MS.showinfo(message='AGREGASTE UN MEDICAMENTO! \n \n AHORA HAY '+str(u[4])+' CAJAS DE LA DROGA ' +str(u[1])+
                ' DEL LABORATIRIO '+str(u[2]),title='AGREGASTE UN MEDICAMENTO!'))
        
    
    def vence(self): 
        ano = int(datetime.datetime.today().year)
        mes = int(datetime.datetime.today().month)
        t=str()
        for i in range(len(self.b)) :
            a=int(self.b[i][5])
            c=int(self.b[i][6])
        
            if 0<=a-mes<=3 and ano==c :
                t=str(t+'\n'+str(self.b[i][4])+' CAJAS DE LA DROGA ' +str(self.b[i][1])+
                ' DEL LABORATIRIO '+str(self.b[i][2])+' SE VENCEN EN : '+str(a-mes)+',MESES '+'\n')
            if a-mes<<0  and ano==c :
                t=str(t+'\n'+str(self.b[i][4])+' CAJAS DE LA DROGA ' +str(self.b[i][1])+
                ' DEL LABORATIRIO '+str(self.b[i][2])+' SE VENCIERON HACE : '+str(-a+mes)+',MESES '+'\n')          
            elif t==str() and i==len(self.b)-1 :
                t='NO HAY VENCIMIENTOS PROXIMOS'
        print(MS.showwarning(message=t, title="VENCIMIENTOS PROXIMOS"))       
    def base(self): 
        contenido=self.f.readlines() 
        self.b=[]     
    
        for i in range (0,len(contenido),1): 
            datos0=[]
            datos1=[]
            datos2=[]
            datos3=[]
            datos4=[]
            datos5=[]
            datos6=[]
    
            dato0=contenido[i].find('\t')
            dato1=contenido[i].find('\t',dato0+1)
            dato2=contenido[i].find('\t',dato1+1)
            dato3=contenido[i].find('\t',dato2+1)
            dato4=contenido[i].find('\t',dato3+1)
            dato5=contenido[i].find('\t',dato4+1)
            dato6=contenido[i].find('\t',dato5+1)

            valor0=contenido[i][0:dato0]
            valor1=contenido[i][dato0+1:dato1] 
            valor2=contenido[i][dato1+1:dato2]
            valor3=contenido[i][dato2+1:dato3]
            valor4=contenido[i][dato3+1:dato4]
            valor5=contenido[i][dato4+1:dato5]
            valor6=contenido[i][dato5+1:dato6]
           
            self.b.append([valor0,valor1,valor2,valor3,valor4,valor5,valor6])
        self.b=sorted(self.b)
        self.f=open('dat.txt','a+')
       
root = tk.Tk()

myapp = App(root)
myapp.mainloop()
