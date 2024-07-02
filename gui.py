#Importing Necessary Libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy
import numpy as np

#Loading the model
from keras.models import load_model
from tensorflow.python import image
model=load_model('C:\\Users\\gagan\\Desktop\\Feature Detection\\Age_Sex_Detection.h5')

#Initializing the GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Age & Gender Detector')
top.configure(background='#CDCDCD')

#initializing the Labels (1 for age and 1 for sex
label1=Label(top, background="#CDCDCD", font =('arial', 15, "bold"))
label2=Label(top, background="#CDCDCD", font=('arial', 15, 'bold'))
label3=Label(top, background="#CDCDCD", font=('arial', 15, 'bold'))
label4=Label(top, background="#CDCDCD", font=('arial', 15, 'bold'))
label5=Label(top, background="#CDCDCD", font=('arial', 15, 'bold'))
sign_image=Label(top)


#Defining Detect function which detects the age and gender of the person in image using the model
def Detect(file_path):
    global label_packed
    image=Image.open(file_path)
    image=image.resize((48, 48))
    image=numpy.expand_dims(image, axis=0)
    image=np.array(image)
    image=np.delete(image, 0, 1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    sex_f=["Male", "Female"]
    hair_f=['short Hair', 'long Hair']
    nationalities = ['Canada', 'America', 'Africa', 'India', 'Russia', 'Japanese']  # List of nationalities 
    image=np.array([image])/255
    pred=model.predict(image)
    
    age=int(np.round(pred[1][0]))
    sex=int(np.round(pred[0][0]))
    hair=int(np.round(pred[0][0]))           
    nation = nationalities[np.argmax(pred)]
    
    print("Predicted Age is "+ str(age))
    print("Predicted Gender is "+sex_f[sex])
    if age<30 and age>20:
        print("Predicted Hairlength is "+hair_f[hair])
    else:
        print("Predicted Correct Gender is "+sex_f[sex])    
    print("Predicted nationality is  " +nation) 
   
    
    
    label1.configure(foreground="#011638", text=age)
    label2.configure(foreground="#011638", text=sex_f[sex])
    if age<30 and age>20:
        label3.configure(foreground="#011638", text=hair_f[hair])
    else:
        label4.configure(foreground="#011638", text=sex_f[sex])
    label5.configure(foreground="#011638", text=nation)


#Defining show_Detect button function
def show_Detect_button(file_path):
    Detect_b=Button(top, text="Detect Image", command=lambda:Detect(file_path), padx=10, pady=5)
    Detect_b.configure(background="#364156", foreground='white', font=('arial', 10, 'bold'))
    Detect_b.place(relx=0.79, rely=0.46)
        
#Defining Upload Image function
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded) 
                
        sign_image.configure(image=im)
        sign_image.image=im
        
        label1.configure(text='')
        label2.configure(text='')
        label3.configure(text='')
        label4.configure(text='')
        label5.configure(text='')
        show_Detect_button(file_path)
    except:
        pass
        
upload=Button(top, text="Upload and Image", command=upload_image, padx=5, pady=5)
upload.configure(background="#364156", foreground='white', font=('arial', 10, 'bold'))
upload.pack(side='bottom', pady=50)
sign_image.pack(side='bottom', expand=True)
label1.pack(side="bottom", expand=True)
label2.pack(side="bottom", expand=True)
label3.pack(side="bottom", expand=True)
label4.pack(side="bottom", expand=True)
label5.pack(side="bottom", expand=True)
heading=Label(top, text="Age and Gender Detector", pady=20, font=('arial', 20, "bold"))
heading.configure(background="#CDCDCD", foreground="#364156")
heading.pack()
top.mainloop()


            
    