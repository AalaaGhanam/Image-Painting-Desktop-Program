import Tkinter
from Tkinter import *
from tkColorChooser import askcolor
from Dialog import *
class PaintApp:
    def __init__(self, root):
        self.color = 'black'
        self.size = 0
        self.drawing_area = Canvas(root,width=900,height=400,bg='white')
        self.drawing_area.pack()
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress>", self.press_mouse)
        self.drawing_area.bind("<ButtonRelease>", self.Release_up)
    drawing_tool = ""
    drawing_area=None
    puting = "up"
    # *********************X and Y POSITIONS for DRAWING with BRUSH ************************
    x_pos, y_pos = None, None
    def change_color_red(self):
        self.color = 'red'
    def change_color_green(self):
        self.color = 'green'
    def change_color_blue(self):
        self.color = 'blue'
    def change_color_orange(self):
        self.color = 'orange'
    def change_color_black(self):
        self.color = 'black'
    def create_earser(self):
        self.drawing_tool = "pencil"
        paint_app.size =70
        self.color='white'
    #*********************************************************************************************
#---------------------------------fuctions-----------------------------------------------
    def do_rectangle(self):
        self.drawing_tool='rect'
        self.drawing_area.create_rectangle(200, 200, 300, 300, width=5, fill=self.color)
        self.drawing_area.create_window(100, 100)
    def random_circle(self):
        self.drawing_tool = 'circle'
        self.drawing_area.create_oval(30, 40, 200, 200, width=2, fill=self.color)
        self.drawing_area.create_window(100, 100)
    def random_line(self):
        self.drawing_tool = 'line'
        self.drawing_area.create_line(300, 50, 450, 300, width=5, fill=self.color)
        self.drawing_area.create_window(100, 100)
   #*******************************************************************************
    def paint(self,event):
        if self. puting == "down":
            #CHECK VALUES OF X AND Y.
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos,self.y_pos, event.x, event.y, width=self.size, fill=self.color)
            self.x_pos = event.x
            self.y_pos = event.y
    def press_mouse(self, event=None):
       self. puting = "down"
    def Release_up(self, event=None):
        self. puting = "up"
        # Reset the line
        self.x_pos = None
        self.y_pos = None
    def motion(self,event=None):
        if self.drawing_tool == "pencil":
            self.paint(event)
window=Tk()
window.geometry('900x500+300+130')
window.title('paint')
paint_app = PaintApp(window)
def pencil():
    try:
        my_size = int(Entry_size.get())
        paint_app.drawing_tool = "pencil"
        paint_app.size = my_size
    except ValueError:
        pass
put_paint=Button(text='brush',width=10,command=pencil,bg='gray').place(x=0,y=0)
label_color1=Button(text='',width=5,bg='red',command=paint_app.change_color_red).place(x=80,y=0)
label_color2=Button(text='',width=5,bg='green',command=paint_app.change_color_green).place(x=125,y=0)
label_color3=Button(text='',width=5,bg='blue',command=paint_app.change_color_blue).place(x=170,y=0)
label_color4=Button(text='',width=5,bg='orange',command=paint_app.change_color_orange).place(x=210,y=0)
label_color5=Button(text='',width=5,bg='black',command=paint_app.change_color_black).place(x=255,y=0)
Label_size = Label(text="size",width=10,bg='gray')
Label_size.place(x=300,y=0)
Entry_size = Entry(bd=5,width=10)
Entry_size.place(x=370,y=0)
#***************************BUTTONS FOR DRAWING FUNCTIONS***************************
Rect= Button(text="Rectangle",width=10,command=paint_app.do_rectangle)
Rect.place(x=440,y=0)
circle = Button(text="circle",width=10,command=paint_app.random_circle)
circle.place(x=510,y=0)
Line = Button(text="Line",width=10, command=paint_app.random_line)
Line.place(x=580,y=0)
#**************************ERASER***************************************
earser=Button(text="Eraser",width=10,bg='black',fg='white', command=paint_app.create_earser)
earser.place(x=650,y=0)
#**********************************TEXT********************************************
#*************************TEXT***************************************
def getColor():
    (triple, color) = askcolor()#(triple,color) Tuple Contein 1-RGB Values OF Color. 2-Color Name.
    if color:
        TextLabel.config(foreground=color)
def onLabel(event):
    TextLabel.configure(text =entry.get())#Configure To Control Apperance.
entry = Entry(window,width=50)
entry.pack(side=BOTTOM)#Pack Show The Entry And Orrganize The Side.
Button(text='Text',bg = "white",width=10).place(x=730,y=0)#Execute WriteText Function.
SelectColor=Button(text='Select Color', command=getColor,bg = "white")
SelectColor.pack(side=BOTTOM,padx=5, pady=5)
entry.bind("<Return>", onLabel)#Execute Function OnLabel When Occure Event.
#*****************************************LABEL CONFLICT***************************************
TextLabel = Label(paint_app.drawing_area,bg = "WHITE",width=50,height=10)
TextLabel.pack(side=TOP,padx=10,pady=5)
paint_app.drawing_area.create_window(700, 300, window=TextLabel)

#******************************END TEXT ************************************************
#*******************************SAVE*******************************************************

screen_width = window.winfo_width()
screen_height = window.winfo_screenheight()

box=(window.winfo_x()+1,window.winfo_y()+1,1000,500)
def _save():
    ImageGrab.grab().crop(box).save("photo.png", "png")

toolbar = Frame(window)
button = Button(toolbar, text='save', width=10,bg='green',fg='black', command=_save).pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)
#****************END SAVE********************************************************************
window.mainloop()#called for windows to be drawn and events to be processed.

