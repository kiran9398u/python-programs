from tkinter import * 
from tkinter import messagebox as mb
from PIL import Image
import requests
import webbrowser
from datetime import datetime
mw=Tk()
mw.title("weather application")
mw.config(bg="royal blue")      
mw.geometry("700x450")

def get_weather():
    global city
    city=city_input.get()
    api_key="7c00ea5e949cb91a732e1eb18799886c"
    url=f' http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    responce=requests.get(url)
    if responce.status_code==200:
        data=responce.json()
        temp=data['main']['temp']
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        wind=(data['wind']['speed'])
        epoch_time=data['dt']
        date_time=datetime.fromtimestamp(epoch_time)
        desc=data["weather"][0]["description"]
        cloudy=data["clouds"]["all"]
        
        timelable.config(text=str(date_time))
        temp_field.insert(0,'{:.2f}'.format(temp)+"celcius")
        pressure_field.insert(0,str(pressure)+"hPa")
        humidity_field.insert(0,str(humidity)+"%")
        wind_field.insert(0,'{:.2f}'.format(wind)+"km/h")
        cloudiness_field.insert(0,str(cloudy)+"%")
        description_field.insert(0,str(desc))
    else:
     mb.showerror("your input was Error","city not found,Enter a valid city name")  

def reset():
    city_input.delete(0,END)
    temp_field.delete(0,END)
    pressure_field.delete(0,END)
    humidity_field.delete(0,END)
    wind_field.delete(0,END)
    cloudiness_field.delete(0,END)
    description_field.delete(0,END)
    timelable.config(text="")
    

title=Label(mw,text="weather direction and forecastiong",fg="green",bg="green",font=("bold",15))
label1=Label(mw,text="enter the city name : ",font=("bold",13),bg="green")
city_input=Entry(mw,width=24,fg="red2",font=('bold',14),relief=GROOVE)
timelable=Label(mw,text="",bg="green",font=("bold",14),fg="lime green")
btn_submit=Button(mw,text="get weather",width=10,font=12,bg="lime green",command=get_weather)
btn_reset=Button(mw,text="rest",font=12,bg="lime green",command=reset)
label2=Label(mw,text="template :",font=('bold',12),bg='royal blue')
label3=Label(mw,text="pressure :",font=('bold',12),bg="royal blue")
label4=Label(mw,text="humidity :",font=('bold',12),bg="royal blue")
label5=Label(mw,text="wind:",font=('bold',12),bg="royal blue")
label6=Label(mw,text="cloudiness:",font=('bold',12),bg="royal blue")
label7=Label(mw,text="description:",font=('bold',12),bg="royal blue")


temp_field=Entry(mw,width=24,font=11)
pressure_field=Entry(mw,width=24,font=11)
humidity_field=Entry(mw,width=24,font=11)
wind_field=Entry(mw,width=24,font=11)
cloudiness_field=Entry(mw,width=24,font=11)
description_field=Entry(mw,width=24,font=11)

timelable.grid(row=1,column=2)
btn_submit.grid(row=2,column=1,pady=5)
 

label2.grid(row=3,column=0,padx=5,pady=5,sticky="W")
label3.grid(row=4,column=0,padx=5,pady=5,sticky="W")
label4.grid(row=5,column=0,padx=5,pady=5,sticky="W")
label5.grid(row=6,column=0,padx=5,pady=5,sticky="W")
label6.grid(row=7,column=0,padx=5,pady=5,sticky="W")
label7.grid(row=8,column=0,padx=5,pady=5,sticky="W")

city_input.grid(row=1,column=1,padx=5,pady=5)
temp_field.grid(row=3,column=1,padx=5,pady=5)
pressure_field.grid(row=4,column=1,padx=5,pady=5)
humidity_field.grid(row=5,column=1,padx=5,pady=5)
wind_field.grid(row=6,column=1,padx=5,pady=5)
cloudiness_field.grid(row=7,column=1,padx=5,pady=5)
description_field.grid(row=8,column=1,padx=5,pady=5)
btn_reset.grid(row=9,column=1,pady=5)
mw.mainloop()