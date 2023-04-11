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


history_list = [
    ["ix12b5", 60, 4.99, "12-01-2023"],
    ["ix12b5", 160, 4.99, "12-01-2023"],
    ["ix12b5", 1260, 4.99, "12-01-2023"],
    ["ix12b5", 60, 4.99, "12-01-2023"],
    ["ix12b5", 60, 40.99, "12-01-2023"],
    ["ix12b5", 60, 99.99, "12-01-2023"],
    ["ix12b5", 60, 4.99, "12-01-2023"],
    ["ix12b5", 60, 4.99, "12-01-2023"],
    ["ix12b5", 60, 4.99, "12-01-2023"],
    ["ix12b5", 60, 4.99, "12-01-2023"],
    ["ix12b4", 60, 4.99, "12-01-2023"],
]


class Purchase_History_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        self.main_label = Label(text="PURCHASE HISTORY", 
            pos=(83,500), 
            size=(250, 40), 
            size_hint=(None, None), 
            font_size='28sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")
        
        self.close_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="CLOSE", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(590, 500), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        
        with self.canvas:
            Color(41/255, 50/255, 70/255, 0.9)
            Rectangle(pos=(60, 80), size=(680, 390))

        self.history_list = []
        for item in history_list:
            minutes = " "*(5-len(str(item[1])))+str(item[1])
            price = str(item[2])+" "*(6-len(str(item[2])))
            self.history_list.append(f"  {item[0]}             {minutes} Minutes        $ {price}       {item[3]}  ")

        self.dummy_button = HoverButton((41/255, 50/255, 70/255, 1), (41/255, 50/255, 70/255, 1), 
                    text=f"  Offer ID                Minutes          Price        Purchase Date ", 
                    background_color=(41/255, 50/255, 70/255, 1),
                    pos=(70, 395),
                    size_hint_x=None,
                    width=660,
                    font_name="assets/Inconsolata-Bold",
                    font_size='16sp',
                    size_hint_y=None,
                    border=(-20, 16, 20, 16),
                    height=40)
        
        self.history_list_container = ScrollView(
            pos=(80, 115), 
            size=(640, 280), 
            size_hint=(None, None),
            scroll_wheel_distance = 100)
        self.offer_button_container = BoxLayout(orientation='vertical',size_hint_y=None, height=len(self.history_list)*40)
        

        for offer in self.history_list:
            self.offer_containing_buttion = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
                    text=offer, 
                    background_color=(41/255, 50/255, 70/255, 0.9),
                    font_name="assets/Inconsolata-Bold",
                    font_size='16sp',
                    size_hint_y=None,
                    border=(-20, 16, 20, 16),
                    height=40)
            self.offer_button_container.add_widget(self.offer_containing_buttion)
        self.history_list_container.add_widget(self.offer_button_container)



        self.add_widget(self.main_label)
        self.add_widget(self.close_button)
        self.add_widget(self.dummy_button)
        self.add_widget(self.history_list_container)