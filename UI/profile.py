
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
    'username': 'Lemon',
    'firstname': 'Rex',
    'lastname': 'Lapis',
    'gender': 'FeMale',
    'date-of-birth': '01-01-0001',
    'mobile': '012345678910',
    'email': 'im.rex.lapis@yahoo.com',
    'minute_remaining': 100
}

class Profile_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        offset = -100
        
        with self.canvas:
            Color(20/255, 25/255, 35/255, 0.9)
            Rectangle(pos=(20, 20), size=(290, 560))
        with self.canvas:
            Color(0.8, 0.83, 1, 0.6)
            Rectangle(pos=(320, 305+offset), size=(420, 265))
        with self.canvas:
            Color(20/255, 25/255, 35/255, 0.9)
            Rectangle(pos=(80, 345), size=(170, 170), source="img/avater.png")
        with self.canvas:
            Color(0.95, 0.96, 1, 0.95)
            Rectangle(pos=(85, 350), size=(160, 160), source="img/avater.png")
        
        self.username_string = user_profile['username'] + " "*(11-len(user_profile['username']))
        self.fullname_string = user_profile['firstname']+" "+user_profile['lastname']
        self.fullname_string = self.fullname_string + " "*(20-len(self.fullname_string))
        self.username = Label(text=self.username_string, 
            pos=(20, 290), 
            size=(290, 40), 
            size_hint=(None, None), 
            font_size='32sp', 
            color=(1, 1, 1, 1),
            bold=True,
            font_name="assets/MajorMonoDisplay-Regular")
        
        self.fullname = Label(text=self.fullname_string, 
            pos=(20, 250), 
            size=(290, 40), 
            size_hint=(None, None), 
            font_size='18sp', 
            color=(1, 1, 1, 1),
            bold=True,
            font_name="assets/MajorMonoDisplay-Regular")

        self.edit_button = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="EDIT PROFILE", 
            background_color=(160/255, 198/255, 255/255, 0.9), 
            pos=(30, 170), 
            size=(270, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        
        self.menu_button = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="MENU", 
            background_color=(160/255, 198/255, 255/255, 0.9), 
            pos=(30, 125), 
            size=(270, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        self.log_out_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="LOG OUT", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(30, 80), 
            size=(270, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))

        self.gender_label = Label(text="Gender           :", 
            pos=(340,480+offset), 
            size=(140, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.gender = Label(text=user_profile['gender']+" "*(32-len(user_profile['gender'])), 
            pos=(510,480+offset), 
            size=(240, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        
        self.date_of_birth_label = Label(text="Date of Birth    :", 
            pos=(340,450+offset), 
            size=(140, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.date_of_birth = Label(text=user_profile['date-of-birth']+" "*(32-len(user_profile['date-of-birth'])), 
            pos=(510,450+offset), 
            size=(240, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")

        self.mobile_label = Label(text="Mobile           :", 
            pos=(340,420+offset), 
            size=(140, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.mobile = Label(text=user_profile['mobile']+" "*(32-len(user_profile['mobile'])), 
            pos=(510,420+offset), 
            size=(240, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")

        self.email_label = Label(text="Email            :", 
            pos=(340,390+offset), 
            size=(140, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.email = Label(text=user_profile['email']+" "*(32-len(user_profile['email'])), 
            pos=(510,390+offset), 
            size=(240, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.minute_remaining_label = Label(text="Minute Remaining :", 
            pos=(340,360+offset), 
            size=(140, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.minute_remaining = Label(text=str(user_profile['minute_remaining'])+" Minute" +" "*(25-len(str(user_profile['minute_remaining']))), 
            pos=(510,360+offset), 
            size=(240, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        

        
        
        self.add_widget(self.username)
        self.add_widget(self.fullname)
        self.add_widget(self.edit_button)

        self.add_widget(self.gender_label)
        self.add_widget(self.gender)
        self.add_widget(self.date_of_birth_label)
        self.add_widget(self.date_of_birth)
        self.add_widget(self.mobile_label)
        self.add_widget(self.mobile)
        self.add_widget(self.email_label)
        self.add_widget(self.email)
        self.add_widget(self.minute_remaining_label)
        self.add_widget(self.minute_remaining)
        self.add_widget(self.menu_button)
        self.add_widget(self.log_out_button)
    

    def update_info(self, user_name, first_name, last_name, gender, date_of_birth, mobile, email, minute_remaining):
        self.username_string = user_name + " "*(11-len(user_name))
        self.fullname_string = first_name+" "+last_name
        self.fullname_string = self.fullname_string + " "*(20-len(self.fullname_string))

        self.username.text = self.username_string
        self.fullname.text = self.fullname_string
        self.gender.text = gender+" "*(32-len(gender))
        self.date_of_birth.text = date_of_birth+" "*(32-len(date_of_birth))
        self.mobile.text = mobile+" "*(32-len(mobile))
        self.email.text = email+" "*(32-len(email))
        self.minute_remaining.text=str(minute_remaining)+" Minute" +" "*(25-len(str(minute_remaining)))
    
    def update_minute_remaining(self, minute_remaining):
        self.minute_remaining.text=str(minute_remaining)+" Minute" +" "*(25-len(str(minute_remaining)))

        
        

        




