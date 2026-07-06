# inthis tutorial we are going to learn  advvanced tutorials
# gui tutorials
# in this we will learn tkinter
# pycharm is also gui software where we click and things get done
# till now we have developed console based applications
# example of console applications
"""print("vidyavaradhi")
name=input("enter your name:")
print("")
print("hello   "+ name)
input("")"""
# in console based cmd or black svcreen and text only will be displayed
# even windows popularity based on gui
# now we are gonna learn phyton using gui applications
# we can use tikinter built in app using phton
# some 3rd party apps are htere such as panda,cutypy ,pygm,
# in gui noting will be printed except gui now we will import mobules
from tkinter import *
# when we use * everything will be imported from tikinter
## all clasess and properties are imported from tikinter
# lets create a window without window how it can be gui
"""main_window = Tk()"""
# for an application to be continuesly on the screen we need to use loop
"""main_window.mainloop()""" # with this we can use all the properties of main window using mainloop method
# so withthis if you run int a wite colur empty winow will come
# so CONGRATUALTIONS YOU HAVE BUILT YOUR FIRST GUI window
#only window have been created by mininmise maximize and close buttone

# we have to writete code in between mainwindow and main loop
main_window = Tk()

mylable = Label(main_window, text="vidyavaradhi",font=("Arial",20), padx=30,pady=50)
mylable.pack(side=LEFT)# it will ad screen to its size



main_window.mainloop()

# out put has came so if we want paddind its give space use padding pad x gives left and right space and pad y gives top
# and bottom function  if you see the midle of the window the text vidya varadhi is there
# so in pack the side ane argument untadhi andulo side anedi tiskunte ganaka adhi left loki vachestadhi
# emi ivakapoyina top lone untadhi  these all are constants ogf tikinter we all hve to capiter leters
# pack is a geomatric manage of lable soit desides where the lable should be in this all so we can use pad but t as we have used in above we can leave it for now
