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


category_list = ["Fashion", "Tech", "Software", "Programming", "Cooking", "Celebrity", "Games", "Sports", "Drawing"]


class Agent_Category_Selection_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        self.main_label = Label(text="Expertise Area (At Most Three)", 
            pos=(160, 500), 
            size=(480, 30), 
            size_hint=(None, None), 
            font_size='28sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")
    
        
        with self.canvas:
            Color(41/255, 50/255, 70/255, 0.9)
            Rectangle(pos=(160, 80), size=(480, 400))

        self.select_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="SELECT", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(325, 100), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))

        
        self.category_list_container = ScrollView(
            pos=(180, 155), 
            size=(440, 280), 
            size_hint=(None, None),
            scroll_wheel_distance = 100)
        self.category_button_container = BoxLayout(orientation='vertical',size_hint_y=None, height=len(category_list)*40)
        
        self.selected_category = []

        for category in category_list:
            category_containing_buttion = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
                    text=category, 
                    background_color=(41/255, 50/255, 70/255, 0.9),
                    font_name="assets/Inconsolata-Bold",
                    font_size='16sp',
                    size_hint_y=None,
                    border=(-20, 16, 20, 16),
                    height=40)
            category_containing_buttion.bind(on_release=self.category_selected_callback)
            self.category_button_container.add_widget(category_containing_buttion)
        self.category_list_container.add_widget(self.category_button_container)


        self.add_widget(self.main_label)
        self.add_widget(self.select_button)
        self.add_widget(self.category_list_container)
    
    def category_selected_callback(self, i):
        if i.text[:-10] in self.selected_category:
            self.selected_category.remove(i.text[:-10])
            i.text = i.text[:-10]
        elif len(self.selected_category) < 3:
            self.selected_category.append(i.text)
            i.text = i.text + "[SELECTED]"