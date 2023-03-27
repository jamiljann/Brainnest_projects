# import required modules
import requests
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
import tkinter as tk

class my_menus():   
    def __init__(self):   
        self.root = Tk()
        self.PROGRAM_NAME = " Weather App "
        self.root.title(self.PROGRAM_NAME)
        self.root.geometry('650x250')
        self.Search_input_var=       StringVar()
        
        self.init_gui()
        
    def init_gui(self):
        self.file_frame = Frame(self.root)
        self.file_frame.grid(column=0, row=0, padx=8, pady=4)
        # input the city name which must be searched its weather conditions
        self.input_label = Label(self.file_frame, text="Enter city name:", fg="green", font="Times 10 bold")
        self.input_entry = Entry(self.file_frame, textvariable= self.Search_input_var, font="Times 15 bold")
        self.search_button_input = Button(self.file_frame, text="Find Weather", command= self.weather, bg="orange")
        
        self.input_label.grid(row=0, column=0, sticky= NSEW, padx=10 ) 
        self.input_entry.grid(row=0, column=1 , padx=10) 
        self.search_button_input.grid(row=0, column=2, sticky=(W), padx=10, pady=10 )
        # show  current time and date
        now = datetime.now().strftime("%Y-%m-%d   %H:%M")
        now_label = Label(self.file_frame, text="Date and Time:", font="Times 8 bold")
        now_label.grid(row=1, column=0,  padx=5)
        time_label = Label(self.file_frame, text=str(now), font="Times 8 ")
        time_label.grid(row=1, column=1,  padx=5)
        #focus on search button
        self.input_entry.focus_set()
            
    def weather(self): 
        # Enter your API key here
        api_key = "54252047b28955efb5f93f788f549030"  
        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"         
        # complete_url variable to store complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" +  self.input_entry.get() 
        # get method of requests module return response object
        response = requests.get(complete_url)
        # json method of response object convert json format data into python format data
        x = response.json()  
        # Now x contains list of nested dictionaries Check the value of "cod" key is equal to "404", means city is found otherwise, city is not found
        if x["cod"] != "404": 
            # store the value of "main" key in variable y
            y = x["main"]
            # store the value corresponding to the "temp" key of y and convert it to celsius
            current_temperature = int(y["temp"] - 273.15)
            # store the value corresponding to the "pressure" key of y
            current_pressure = y["pressure"]
            # store the value corresponding to the "humidity" key of y
            current_humidity = y["humidity"]
            # store the value of "weather" key in variable z
            z = x["weather"]
            # store the value corresponding to the "description" key at the 0th index of z
            weather_description = z[0]["description"]
            # stor weather's icon in my_icon variable
            my_icon =  z[0]["icon"]
            
            
            # delete previous temperature
            Temperature_number = Label(self.file_frame, text="                              ", font="Times 10 bold")  #clear last output
            Temperature_number.grid(row=2, column=1, sticky=(W), padx=10)
            # show temperature
            Temperature_label = Label(self.file_frame, text="Temperature (in celsius unit):", font="Times 10 bold")
            Temperature_label.grid(row=2, column=0,sticky=(W), padx=10) 
            Temperature_number = Label(self.file_frame, text=str(current_temperature), font="Times 10 bold")
            Temperature_number.grid(row=2, column=1,sticky=(tk.W+ tk.E), padx=10)  
            # show pressure
            pressure_label = Label(self.file_frame, text="Atmospheric pressure (in hPa unit):", font="Times 10 bold")
            pressure_label.grid(row=3, column=0, sticky=(W), padx=10) 
            pressure_number = Label(self.file_frame, text=str(current_pressure), font="Times 10 bold")
            pressure_number.grid(row=3, column=1, sticky=(tk.W+ tk.E), padx=10) 
            # show pressure
            humidity_label = Label(self.file_frame, text="Humidity (in percentage):", font="Times 10 bold")
            humidity_label.grid(row=4, column=0, sticky=(W), padx=10) 
            humidity_number = Label(self.file_frame, text=str(current_humidity), font="Times 10 bold")
            humidity_number.grid(row=4, column=1, sticky=(tk.W+ tk.E), padx=10) 
            # delete previous description
            description_number = Label(self.file_frame, text="                              ", font="Times 10 bold") #clear last output
            description_number.grid(row=5, column=1, sticky=(W), padx=10)
            # show description
            description_label = Label(self.file_frame, text="Description:", font="Times 10 bold")
            description_label.grid(row=5, column=0, sticky=(W), padx=10) 
            description_number = Label(self.file_frame, text=str(weather_description), font="Times 10 bold")
            description_number.grid(row=5, column=1, sticky=(tk.W+ tk.E), padx=10) 
            
            image_file = "C:/Python/class/Session1/Javab/icons/" + my_icon +".png"

            # Create a photoimage object of the image in the path
            image1 = Image.open(image_file)
            test = ImageTk.PhotoImage(image1)
            label1 = Label(image=test)
            label1.image = test
            # Position image
            label1.grid(row=6, column=0,  padx=5)   
        else:
            messagebox.showerror('Error', 'City Not Found' )
            

if __name__ == '__main__': 
    My_menu = my_menus()
    My_menu.root.mainloop()