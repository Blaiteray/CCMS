
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



class Signup_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        offset = 60
        with self.canvas:
            Color(0.3, 0.4, 0.6, 0.5)
            Rectangle(pos=(400, 20), size=(380, 560))
        with self.canvas:
            Color(0.95, 0.96, 1, 0.95)
            Rectangle(pos=(20, 140), size=(380, 380), source="img/signup.png")
        self.login_label = Label(text="Sign Up", 
            pos=(450,offset+40*11+20), 
            size=(80, 40), 
            size_hint=(None, None), 
            font_size='28sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")

        self.user_name = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            hint_text = 'User Name',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, offset+40*10), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.first_name = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            hint_text = 'First Name',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, offset+40*9), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.last_name = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            hint_text = 'Last Name',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, offset+40*8), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.password = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            password = True,
            hint_text = 'Password',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, offset+40*7), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.password_confirm = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            password = True,
            hint_text = 'Confirm Password',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, offset+40*6), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.gender = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            hint_text = 'Gender',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, offset+40*5), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.date_of_birth = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            hint_text = 'Date of Birth eg.31-08-2022',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, offset+40*4), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.mobile = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            hint_text = 'Mobile Number',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, offset+40*3), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.email = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            hint_text = 'Email Address',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440, offset+40*2), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        
        self.register_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="REGISTER", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(440, offset+27), 
            size=(300, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))

        self.login_button = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="LOGIN", 
            background_color=(160/255, 198/255, 255/255, 0.9), 
            pos=(440, offset-15), 
            size=(300, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        



        self.agent_customer_label = Label(text="Sign Up as:", 
            pos=(60,offset-15), 
            size=(100, 40), 
            size_hint=(None, None), 
            font_size='22sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")
        self.signup_as = "Customer"
        self.agent_customer_selection = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="Customer", 
            background_color=(160/255, 198/255, 255/255, 0.9), 
            pos=(180, offset-15), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        self.agent_customer_selection.bind(on_release=self.agent_customer_selection_callback)

        self.add_widget(self.login_label)
        self.add_widget(self.user_name)
        self.add_widget(self.password)
        self.add_widget(self.password_confirm)
        self.add_widget(self.first_name)
        self.add_widget(self.last_name)
        self.add_widget(self.gender)
        self.add_widget(self.date_of_birth)
        self.add_widget(self.mobile)
        self.add_widget(self.email)
        self.add_widget(self.register_button)
        self.add_widget(self.login_button)
        self.add_widget(self.agent_customer_label)
        self.add_widget(self.agent_customer_selection)
    
    def agent_customer_selection_callback(self, i):
        if self.signup_as == "Customer":
            self.signup_as = "Agent"
        else:
            self.signup_as = "Customer"
        i.text = self.signup_as



