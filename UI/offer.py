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



class Offer_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        self.main_label = Label(text="PURCHASE BUNDLES", 
            pos=(83,500), 
            size=(250, 40), 
            size_hint=(None, None), 
            font_size='28sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")
        
        self.cancel_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="CANCEL", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(430, 500), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        
        self.history_button = HoverButton((160/255, 198/255, 255/255, 0.7), (160/255, 198/255, 255/255, 0.9), 
            text="HISTORY", 
            background_color=(160/255, 198/255, 255/255, 0.9), 
            pos=(590, 500), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        
        with self.canvas:
            Color(41/255, 50/255, 70/255, 0.9)
            Rectangle(pos=(60, 80), size=(680, 390))

        self.note_list = ["bobbo", "mamama", "fes", "feasfes", "hello woerld", "mama", "banana", "meau", "esa"]
        self.note_list_container = ScrollView(
            pos=(80, 115), 
            size=(640, 320), 
            size_hint=(None, None),
            scroll_wheel_distance = 100)
        self.note_button_container = BoxLayout(orientation='vertical',size_hint_y=None, height=len(self.note_list)*40)
        

        for note in self.note_list:
            self.note_containing_buttion = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
                    text=note, 
                    background_color=(41/255, 50/255, 70/255, 0.9),
                    font_name="assets/static/Nunito-Regular",
                    font_size='16sp',
                    size_hint_y=None,
                    border=(-20, 16, 20, 16),
                    height=40)
            self.note_button_container.add_widget(self.note_containing_buttion)
        self.note_list_container.add_widget(self.note_button_container)

        self.add_widget(self.main_label)
        self.add_widget(self.cancel_button)
        self.add_widget(self.history_button)
        self.add_widget(self.note_list_container)