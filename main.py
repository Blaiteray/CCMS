"""
A note keeping tool
"""

import os
os.environ['KIVY_IMAGE'] = 'pil'
# os.environ["KIVY_NO_CONSOLELOG"] = "1"

import kivy
kivy.require('2.1.0')
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics','resizable', False)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App 
from kivy.core.window import Window
# Window.minimum_width, Window.minimum_height = (800, 600)
Window.clearcolor = (0.05, 0.1, 0.15, 1)
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
from hovekivy import HoverBehavior
from UI.login import Login_Widget
from UI.signup import Signup_Widget
from UI.profile import Profile_Widget
from modified_widget import *

with Window.canvas.before:
    Color(0.95, 0.96, 1, 1)
    # Image(source='bg_img.jpg', size=(800, 600))
    Rectangle(size=Window.size, source="img/bg_img.jpg", pos=(0,0))



class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        self.add_widget(Profile_Widget())
       





class Main_Window(App):
    def build(self):
        return MainLayout()

Main_Window().run()
