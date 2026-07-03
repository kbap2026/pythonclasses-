# this project is about sending wats app msg automaticali using a short code
# go to google type pywhatkit
import pywhatkit
# dintho chala cheyachu but ye project lo wats app msgs matrame cheyadam
print("test")
import flask
#pywhatkit.sendwhatmsg("+919985817259",'hellow my dear friend,how are you',15,8)
# dynamic coding
wno=input('whats app no:')
msg =input("message:")
hr = int(input("hour:(in 24 hrs format)"))
mnt = int(input("minutes:"))
pywhatkit.sendwhatmsg("+91"+wno, msg,hr,mnt )