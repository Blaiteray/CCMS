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


user_profile = {
    'username': 'Lemon',
    'firstname': 'Rex',
    'lastname': 'Lapis',
    'gender': 'FeMale',
    'date-of-birth': '01-01-0001',
    'mobile': '012345678910',
    'email': 'im.rex.lapis@yahoo.com',
    'minute_remaining': 100
}


class Edit_Profile_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        offset = 60
        xmove = -190
        with self.canvas:
            Color(0.3, 0.4, 0.6, 0.5)
            Rectangle(pos=(400+xmove, 20), size=(380, 560))

        self.edit_label = Label(text="Edit Profile", 
            pos=(450+xmove,offset+40*11+20), 
            size=(128, 40), 
            size_hint=(None, None), 
            font_size='28sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")

        self.user_name = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text=user_profile['username'],
            readonly=True,
            hint_text = 'User Name',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440+xmove, offset+40*10), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.first_name = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text=user_profile['firstname'],
            hint_text = 'First Name',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440+xmove, offset+40*9), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.last_name = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text=user_profile['lastname'],
            hint_text = 'Last Name',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440+xmove, offset+40*8), 
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
            pos=(440+xmove, offset+40*7), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.password_confirm = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text='',
            password=True,
            hint_text = 'Confirm Password',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440+xmove, offset+40*6), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.gender = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text=user_profile['gender'],
            hint_text = 'Gender',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440+xmove, offset+40*5), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.date_of_birth = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text=user_profile['date-of-birth'],
            hint_text = 'Date of Birth eg.31-08-2022',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440+xmove, offset+40*4), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.mobile = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text=user_profile['mobile'],
            hint_text = 'Mobile Number',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440+xmove, offset+40*3), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        self.email = HoverTextInput((1, 1, 1, 1), (239/255, 243/255, 255/255, 1),
            text=user_profile['email'],
            hint_text = 'Email Address',
            background_color=(239/255, 243/255, 255/255, 1),
            pos=(440+xmove, offset+40*2), 
            size=(300, 30), 
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))
        
        self.done_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="DONE", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(440+xmove, offset+27), 
            size=(300, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))

        self.cancel_button = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="CANCEL", 
            background_color=(160/255, 198/255, 255/255, 0.9), 
            pos=(440+xmove, offset-15), 
            size=(300, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))

        self.add_widget(self.edit_label)
        self.add_widget(self.user_name)
        self.add_widget(self.password)
        self.add_widget(self.password_confirm)
        self.add_widget(self.first_name)
        self.add_widget(self.last_name)
        self.add_widget(self.gender)
        self.add_widget(self.date_of_birth)
        self.add_widget(self.mobile)
        self.add_widget(self.email)
        self.add_widget(self.done_button)
        self.add_widget(self.cancel_button)
    

    def update_info(self, user_name, first_name, last_name, password, gender, date_of_birth, mobile, email):
        self.user_name.text = user_name
        self.password.text = password
        self.password_confirm.text = password
        self.first_name.text = first_name
        self.last_name.text = last_name
        self.gender.text = gender
        self.date_of_birth.text =date_of_birth
        self.mobile.text = mobile
        self.email.text = email