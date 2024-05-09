from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get() 
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5cb93e189f86b4e3418e7c3a43dbd40b").json()
    w_lable1.config(text=data["weather"][0]["main"])
    wb_lable1.config(text=data["weather"][0]["description"])
    temp1=str(int(data["main"]["temp"]-273.15))
    temp_lable1.config(text=temp1+"°")
    temp2=str(data["main"]["pressure"])
    per_lable1.config(text=temp2+" Pa")


win = Tk()
win.title("Weather App")
win.config(bg = "lightskyblue")
win.geometry("500x550")

name_lable = Label(win,text="Weather App",font=("Verdana", 25, "bold"))
name_lable.place(x=25, y=50, height=60, width=450)

list_name = ["Anand","Jamnagar ","Bharuch","Surat","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


city_name = StringVar()
comm = ttk.Combobox(win,text="Weather App", values=list_name, font=("Verdana",16 , "bold"),textvariable=city_name)
comm.place(x=25, y=120, height=50, width=450)

w_lable = Label(win,text="Weather Climate",font=("Verdana", 10,"bold"))
w_lable.place(x=25, y=260, height=50, width=210)

w_lable1 = Label(win,text="",font=("Verdana", 8))
w_lable1.place(x=250, y=260, height=50, width=210)

wb_lable = Label(win,text="Weather Description",font=("Verdana", 10,"bold"))
wb_lable.place(x=25, y=320, height=50, width=210)

wb_lable1 = Label(win,text="",font=("Verdana", 8))
wb_lable1.place(x=250, y=320, height=50, width=210)

temp_lable = Label(win,text="Temperature",font=("Verdana", 10,"bold"))
temp_lable.place(x=25, y=380, height=50, width=210)

temp_lable1 = Label(win,text="",font=("Verdana", 8))
temp_lable1.place(x=250, y=380, height=50, width=210)

per_lable = Label(win,text="Pressure",font=("Verdana", 10,"bold"))
per_lable.place(x=25, y=440, height=50, width=210)

per_lable1 = Label(win,text="",font=("Verdana", 8))
per_lable1.place(x=250, y=440, height=50, width=210)

done_button = Button(win,text="Done",font=("Verdana", 20 , "bold"),command=data_get)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()

