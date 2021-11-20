from tkinter import *
from gtts import gTTS
from playsound import *
from googletrans import Translator




root = Tk()
root.geometry('300x400')
root.resizable(0,0)
root.config(bg = 'ghost white')
root.title('TTS')



Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()



Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)


Msg = StringVar()

printer = ""
entry_field = Entry(root,textvariable = Msg, width ='30')
entry_field.place(x = 20 , y = 100)
translator = Translator()

text_box = Text(
    root,
    height=5,
    width=30
)
text_box.pack(expand=True)
text_box.place(x=15,y=300)
text_box.insert('end', printer)



def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('lang.mp3')
    playsound('lang.mp3')

def FRENCH():
    clearTextInput()
    Message = entry_field.get()
    text_to_translate = translator.translate(Message,
                                                     src= 'en',
                                                     dest= 'fr')
    speech = gTTS(text = text_to_translate.text, lang='fr', tld='fr')
    printer = text_to_translate.text
    text_box.insert('end', printer)
    speech.save('lang.mp3')
    playsound('lang.mp3')

def SPANISH():
    clearTextInput()
    Message = entry_field.get()
    text_to_translate = translator.translate(Message,
                                                     src= 'en',
                                                     dest= 'es')
    speech = gTTS(text = text_to_translate.text , lang='es', tld='es')
    printer = text_to_translate.text
    text_box.insert('end', printer)
    speech.save('lang.mp3')
    playsound('lang.mp3')

def GERMAN():
    clearTextInput()
    Message = entry_field.get()
    text_to_translate = translator.translate(Message,
                                                     src= 'en',
                                                     dest= 'de')
    speech = gTTS(text = text_to_translate.text, lang='de', tld='de')
    printer = text_to_translate.text
    text_box.insert('end', printer)
    speech.save('lang.mp3')
    playsound('lang.mp3')

def HINDI():
    clearTextInput()
    Message = entry_field.get()
    text_to_translate = translator.translate(Message,
                                                     src= 'en',
                                                     dest= 'hi')
    speech = gTTS(text = text_to_translate.text, lang='hi', tld='com')
    printer = text_to_translate.text
    text_box.insert('end', printer)
    speech.save('lang.mp3')
    playsound('lang.mp3')

def JAPANESE():
    clearTextInput()
    Message = entry_field.get()
    text_to_translate = translator.translate(Message,
                                                     src= 'en',
                                                     dest= 'ja')
    speech = gTTS(text = text_to_translate.text, lang='ja', tld='jp')
    printer = text_to_translate.text
    text_box.insert('end', printer)
    speech.save('lang.mp3')
    playsound('lang.mp3')

def RUSSIAN():
    clearTextInput()
    Message = entry_field.get()
    text_to_translate = translator.translate(Message,
                                                     src= 'en',
                                                     dest= 'ru')
    speech = gTTS(text = text_to_translate.text, lang='ru', tld='ru')
    printer = text_to_translate.text
    text_box.insert('end', printer)
    speech.save('lang.mp3')
    playsound('lang.mp3')


    
def Exit():
    root.destroy()
    
def Reset():
    Msg.set("")
    clearTextInput()

    
def clearTextInput():
    text_box.delete("1.0","end")
    

    
Button(root, text = 'PLAY' , font = 'arial 15 bold', command = Text_to_speech, width = 4).place(x=25, y = 140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'OrangeRed1').place(x = 100, y = 140)
Button(root, text = 'RESET', font ='arial 15 bold', command = Reset).place(x = 175 , y = 140)
Button(root, text = 'FRENCH', font ='arial 10 bold', command = FRENCH,width = 6).place(x = 25 , y =200)
Button(root, text = 'SPANISH', font ='arial 10 bold', command = SPANISH,width = 6).place(x = 110 , y =200)
Button(root, text = 'GERMAN', font ='arial 10 bold', command = GERMAN,width = 6).place(x = 195 , y = 200)
Button(root, text = 'HINDI', font ='arial 10 bold', command = HINDI,width = 6).place(x = 25 , y = 240)
Button(root, text = 'JAPANESE', font ='arial 10 bold', command = JAPANESE,width = 7).place(x = 110 , y = 240)
Button(root, text = 'RUSSIAN', font ='arial 10 bold', command = RUSSIAN,width = 6).place(x = 195 , y = 240)



root.mainloop()