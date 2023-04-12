
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



class Login_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        with self.canvas:
            Color(0.3, 0.4, 0.6, 0.5)
            Rectangle(pos=(400, 150), size=(380, 340))
        with self.canvas:
            Color(0.95, 0.96, 1, 0.95)
            Rectangle(pos=(50, 180), size=(300, 300), source="img/login.png")
        self.login_label = Label(text="Login", 
            pos=(440,400), 
            size=(80, 40), 
            size_hint=(None, None), 
            font_size='28sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")

        self.user_name = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            hint_text = 'User Name',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, 335), 
            size=(300, 30), 
            font_size=14,
            font_name="assets/static/Nunito-Regular",
            multiline=False,
            size_hint=(None, None))
        self.password = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            password = True,
            hint_text = 'Password',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, 290), 
            size=(300, 30), 
            font_size=14,
            font_name="assets/static/Nunito-Regular",
            multiline=False,
            size_hint=(None, None))
        
        self.login_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="LOGIN", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(440,225), 
            size=(300, 34),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        
        self.signup_button = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="SIGN UP", 
            background_color=(160/255, 198/255, 255/255, 0.9), 
            pos=(440,185), 
            size=(300, 34),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        
        self.agent_customer_label = Label(text="Log in as:", 
            pos=(60,145), 
            size=(100, 40), 
            size_hint=(None, None), 
            font_size='22sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")
        self.login_as = "Customer"
        self.agent_customer_selection = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="Customer", 
            background_color=(160/255, 198/255, 255/255, 0.9), 
            pos=(180, 145), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        self.agent_customer_selection.bind(on_release=self.agent_customer_selection_callback)
        

        self.add_widget(self.login_label)
        self.add_widget(self.user_name)
        self.add_widget(self.password)
        self.add_widget(self.login_button)
        self.add_widget(self.signup_button)
        self.add_widget(self.agent_customer_label)
        self.add_widget(self.agent_customer_selection)

    
    def agent_customer_selection_callback(self, i):
        if self.login_as == "Customer":
            self.login_as = "Agent"
        else:
            self.login_as = "Customer"
        i.text = self.login_as




