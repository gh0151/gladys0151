
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label 
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from pathlib import Path
import shutil #to move files into different directories
import os #used for moving file into archive directory
import time
import datetime


"""archive directory path"""
destination = "/home/pi/kivy/examples/archive"

source  = "/home/pi/kivy/examples/workfile.txt"

name =  "workfile"
extension = "txt"

"""set of users for login screen"""
usersSet = {"g", "jack", "taylor", "jorge"}

""" archives file if file is full"""
def archive_file(src, dest):
    shutil.move(src,dest) #moves into archive directory
    rename_file(destination, name, extension) #renames file

def create_new_file():
    new_file = open("workfile.txt","w")
    new_file.close()

""" renames file to 'workfile[current date].txt'
    for example goes from workfile.txt --> workfile2018-01-24.txt"""
def rename_file(dest, name, ext):
    os.rename(destination + '/' + name + '.' + ext,dest + '/' + name + str(datetime.date.today()) + '.' + ext)

""" Server sends alert to gui. This function is used to confirm if workfile.txt is "full", then archives file """
def check_if_Full():
    num_lines = sum(1 for line in open('workfile.txt')) 
    print(num_lines)
    # if file contains max num of lines or if the time is midnight
    midnight = datetime.time(1,0,0)
    if (num_lines >= 200 or datetime.time() == midnight):
        print("reached over 200 lines or has reached midnight")
        archive_file(source, destination) #archive file, then creates new file
    else:
        print("under 200 lines")

""" Checks if work file exists, if not, creates flat file that will interact with the server """
myfile = Path("/home/pi/kivy/examples/workfile.txt") #directory will change once Jack and I collab
if myfile.is_file():
    print("file exists in current path")
    check_if_Full()
else:
    print("file does not exist, creating file")
    f = open("workfile.txt", "w")
    f.close()

class ScreenManagement(ScreenManager):
    pass

class LoginScreen(Screen):

    def login(self, username, password):
        if username in usersSet and password == "test":
           self.parent.current = 'homepage'
	else:
	    box = BoxLayout(orientation = 'vertical', padding = (5))

	    box.add_widget(Label(text='Invalid username or password'))
	    popup = Popup(title='Login Error', title_size =(30),title_align='center',content=box,size=(25,25),auto_dismiss=True)
	    box.add_widget(Button(text='Dismiss', on_press=popup.dismiss))
	    popup.open()

class HomePage(Screen):
    pass

class ViewHealth(Screen):
    pass

class Modify(Screen):
    pass

class Setting(Screen):
    pass

Builder.load_file("testingapp1.kv")

class TestApp(App):
    title = "Login Screen"
    def build(self):
        return ScreenManagement()

if __name__ == "__main__":
    TestApp().run()
