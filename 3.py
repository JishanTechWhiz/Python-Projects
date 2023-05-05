from tkinter import *
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

window = Tk()
window.title('Weather App Using API')
window.geometry('900x500+300+200')


#Function

def getWeather():
    city = e1.get()

    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    #print(result)
    t1.config(text='CURRENT WEATHER')
    t2.config(text=current_time)

    #Weather API

    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=c2172c4e0998db8d41c542ae397e2756"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']

    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    lc1.config(text=(temp,"°"))
    lc2.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

    lc3.config(text=wind)
    lc4.config(text=humidity)
    lc5.config(text=description)
    lc6.config(text=pressure)





#Search Image
search_img = PhotoImage(file='copy of search.png')

l1 = Label(window,image=search_img)
l1.pack()

#Input
e1 = Entry(window,width=20,justify=CENTER,bg="#404040",fg="white",font=('sans',17,'bold'))
e1.place(x=250,y=20)
e1.focus()

#Search Icon
search_icon = PhotoImage(file='Copy of search_icon.png')
btn1 = Button(window,image=search_icon,bg="#404040",height=40,width=40,cursor='hand2',command=getWeather)
btn1.place(x=590,y=15)

#Time
t1 = Label(window,font=('arial',15,'bold'))
t1.place(x=100,y=150)

t2 = Label(window,font=('Helvetica',15))
t2.place(x=100,y=200)


#Logo
logo = PhotoImage(file='Copy of logo.png')
l3 = Label(window,image=logo)
l3.pack()

#Bottom Image

bottom_img = PhotoImage(file='Copy of box.png')
l3 = Label(window,image=bottom_img)
l3.pack(padx=5,pady=5,side=BOTTOM)

#Labels

lb1 = Label(window,text='WIND',font=('Helvetica',15,'bold'),bg='#1ab5ef',fg='white')
lb1.place(x=150,y=410)

lb2 = Label(window,text='HUMIDITY',font=('Helvetica',15,'bold'),bg='#1ab5ef',fg='white')
lb2.place(x=300,y=410)

lb3 = Label(window,text='DESCRIPTION',font=('Helvetica',15,'bold'),bg='#1ab5ef',fg='white')
lb3.place(x=450,y=410)

lb4 = Label(window,text='PRESSURE',font=('Helvetica',15,'bold'),bg='#1ab5ef',fg='white')
lb4.place(x=650,y=410)

#Config Label
lc1 = Label(window,font=('arial',45,'bold'),fg='#ee666d')
lc1.place(x=580,y=150)

lc2 = Label(window,font=('arial',15,'bold'))
lc2.place(x=580,y=250)

#

lc3 = Label(window,text='....',font=('arial',15,'bold'),bg='#1ab5ef')
lc3.place(x=150,y=430)

lc4 = Label(window,text='....',font=('arial',15,'bold'),bg='#1ab5ef')
lc4.place(x=310,y=430)

lc5 = Label(window,text='....',font=('arial',15,'bold'),bg='#1ab5ef')
lc5.place(x=460,y=430)

lc6 = Label(window,text='....',font=('arial',15,'bold'),bg='#1ab5ef')
lc6.place(x=650,y=430)




window.mainloop()



