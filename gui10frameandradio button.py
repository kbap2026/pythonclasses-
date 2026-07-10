# in this tutorial we learn about frames , radio buttons , check buttons
#drop downs list
# sliders(scale widget)
# gometry function
from tkinter import *
mw= Tk()
mw.title("VIDYA VARADHI")
mw.geometry("900x720")# size of window
# creating frames
frame1 = LabelFrame(mw,text="THS IS FRAME1", padx=10,pady=10,font=("",14))
#frame1.pack()
# you can als take it as grid insted of pack
frame1.grid(row=0,column=0,padx=20,pady=10)

exit_btn= Button(frame1,text="Exit",padx=60,pady=20,font=("",14),command=mw.quit)#command badulu frame 1 ani kuda tiskovachu
exit_btn.pack()

# creating Radio button

def rv_res():# radio buttun nokinapudu edina activity jargali ante ye funtion rakuntunam
    rv_lbl.config(text=rv.get())
rv= IntVar() # its a tikenter variable
Radiobutton(frame1,text="option1",value=1,variable=rv,font=("",14),command=rv_res).pack(pady=(30,10))
Radiobutton(frame1,text="option2",value=2,variable=rv,font=("",14),command=rv_res).pack(pady=(0,20))
# raido buttons edo okate select avtadi 1 tiskunte 2 deselect cheskuntundhi
rv_lbl=LabelFrame(frame1,text="",font=("",14))
rv_lbl.pack()


mw.mainloop()