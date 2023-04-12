
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
agent_profile = {
    'username': 'Lemon',
    'firstname': 'Rex',
    'lastname': 'Lapis',
    'gender': 'FeMale',
    'date-of-birth': '01-01-0001',
    'mobile': '012345678910',
    'email': 'im.rex.lapis@yahoo.com',
    'category': ['Tech', 'Cooking', 'Gardenng'],
    'call_received': 10,
    'call_duration': 1200
}

class Agent_Dashboard_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        offset = -100
        
        with self.canvas:
            Color(20/255, 25/255, 35/255, 0.9)
            Rectangle(pos=(20, 20), size=(290, 560))
        with self.canvas:
            Color(0.8, 0.83, 1, 0.6)
            Rectangle(pos=(320, 265+offset), size=(460, 405))
        with self.canvas:
            Color(20/255, 25/255, 35/255, 0.9)
            Rectangle(pos=(80, 345), size=(170, 170), source="img/avater.png")
        with self.canvas:
            Color(0.95, 0.96, 1, 0.95)
            Rectangle(pos=(85, 350), size=(160, 160), source="img/avater.png")
        
        self.username_string = agent_profile['username'] + " "*(11-len(agent_profile['username']))
        self.fullname_string = agent_profile['firstname']+" "+agent_profile['lastname']
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
        
        self.receive_call_button = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="RECEIVE CALL", 
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
        self.gender = Label(text=agent_profile['gender']+" "*(32-len(agent_profile['gender'])), 
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
        self.date_of_birth = Label(text=agent_profile['date-of-birth']+" "*(32-len(agent_profile['date-of-birth'])), 
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
        self.mobile = Label(text=agent_profile['mobile']+" "*(32-len(agent_profile['mobile'])), 
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
        self.email = Label(text=agent_profile['email']+" "*(32-len(agent_profile['email'])), 
            pos=(510,390+offset), 
            size=(240, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.call_received_label = Label(text="Call Received    :", 
            pos=(340,360+offset), 
            size=(140, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.call_reveived = Label(text=str(agent_profile['call_received'])+" "*(32-len(str(agent_profile['call_received']))), 
            pos=(510,360+offset), 
            size=(240, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.call_duration_label = Label(text="Call Duration    :", 
            pos=(340,330+offset), 
            size=(140, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.call_duration = Label(text=str(agent_profile['call_duration'])+" Minute" +" "*(25-len(str(agent_profile['call_duration']))), 
            pos=(510,330+offset), 
            size=(240, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        self.category_label = Label(text="Category         :", 
            pos=(340,300+offset), 
            size=(140, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        temp_str = ", ".join(agent_profile['category'])
        self.category = Label(text=temp_str+" "*(32-len(temp_str)), 
            pos=(510,300+offset), 
            size=(240, 40), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/Inconsolata-Bold")
        


        self.status_selection_label = Label(text="Set Status:", 
            pos=(420,200+offset), 
            size=(80, 40), 
            size_hint=(None, None), 
            font_size='22sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")
        self.status = "Inactive"
        self.status_selection = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="Inactive", 
            background_color=(160/255, 198/255, 255/255, 0.9), 
            pos=(530, 200+offset), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        self.status_selection.bind(on_release=self.status_selection_callback)
        

        
        
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
        self.add_widget(self.call_received_label)
        self.add_widget(self.call_reveived)
        self.add_widget(self.call_duration_label)
        self.add_widget(self.call_duration)
        self.add_widget(self.category_label)
        self.add_widget(self.category)
        self.add_widget(self.receive_call_button)
        self.add_widget(self.log_out_button)
        self.add_widget(self.status_selection_label)
        self.add_widget(self.status_selection)

    
    def status_selection_callback(self, i):
        if self.status == "Inactive":
            self.status = "Active"
        else:
            self.status = "Inactive"
        i.text = self.status
        
        

        




