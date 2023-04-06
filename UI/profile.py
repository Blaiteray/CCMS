
import kivy
kivy.require('2.1.0')

from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
# from kivy.uix.screenmanager import Screen, ScreenManager
from modified_widget import *

#Dummy
user_profile = {
    'username': 'Boo124535',
    'firstname': 'Rex',
    'lastname': 'Lapis',
    'gender': 'Male',
    'date-of-birth': '01-01-0001',
    'mobile': '012345678910',
    'email': 'im.rex.lapis@yahoo.com'
}

class Profile_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        
        

        self.add_widget(self.username)
        self.add_widget(self.full_name)

        




