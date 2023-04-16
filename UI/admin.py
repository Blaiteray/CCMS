
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



information_list_client = [
    ["UserName1", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
    ["UserName2", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
    ["UserName3", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
    ["UserName4", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
]
information_list_agent = [
    ["UserName2", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
    ["UserName1", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
    ["UserName3", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
    ["UserName4", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
]


class Admin_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        self.main_label = Label(text="Admin Panel", 
            pos=(83,500), 
            size=(250, 40), 
            size_hint=(None, None), 
            font_size='28sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")
        
        self.showed_type = "Customer"
        self.type_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="Customer", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(590, 500), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        self.type_button.bind(on_release=self.change_type)
        
        with self.canvas:
            Color(41/255, 50/255, 70/255, 0.9)
            Rectangle(pos=(60, 80), size=(680, 390))

        self.information_list = []
        for item in information_list_client:
            minutes = " "*(5-len(str(item[1])))+str(item[1])
            price = str(item[2])+" "*(6-len(str(item[2])))
            self.information_list.append(f"  {item[0]}             {minutes} Minutes        $ {price}       {item[3]}  ")

        self.dummy_button = HoverButton((41/255, 50/255, 70/255, 1), (41/255, 50/255, 70/255, 1), 
                    text=f"  row ID                Minutes          Price        Purchase Date ", 
                    background_color=(41/255, 50/255, 70/255, 1),
                    pos=(70, 395),
                    size_hint_x=None,
                    width=660,
                    font_name="assets/Inconsolata-Bold",
                    font_size='16sp',
                    size_hint_y=None,
                    border=(-20, 16, 20, 16),
                    height=40)
        
        self.information_list_container = ScrollView(
            pos=(80, 115), 
            size=(640, 280), 
            size_hint=(None, None),
            scroll_wheel_distance = 100)
        self.row_button_container = BoxLayout(orientation='vertical',size_hint_y=None, height=len(self.information_list)*40)
        

        for row in self.information_list:
            self.row_containing_buttion = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
                    text=row, 
                    background_color=(41/255, 50/255, 70/255, 0.9),
                    font_name="assets/Inconsolata-Bold",
                    font_size='16sp',
                    size_hint_y=None,
                    border=(-20, 16, 20, 16),
                    height=40)
            self.row_button_container.add_widget(self.row_containing_buttion)
        self.information_list_container.add_widget(self.row_button_container)



        self.add_widget(self.main_label)
        self.add_widget(self.type_button)
        self.add_widget(self.dummy_button)
        self.add_widget(self.information_list_container)
    

    def update_information(self, information_list):
        remove_widget_recursive(self.information_list_container)
        self.information_list = []
        for item in information_list:
            minutes = " "*(5-len(str(item[1])))+str(item[1])
            price = str(item[2])+" "*(6-len(str(item[2])))
            self.information_list.append(f"  {item[0]}             {minutes} Minutes        $ {price}       {item[3]}  ")
        
        self.information_list_container = ScrollView(
            pos=(80, 115), 
            size=(640, 280), 
            size_hint=(None, None),
            scroll_wheel_distance = 100)
        self.row_button_container = BoxLayout(orientation='vertical',size_hint_y=None, height=len(self.information_list)*40)
        

        for row in self.information_list:
            self.row_containing_buttion = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
                    text=row, 
                    background_color=(41/255, 50/255, 70/255, 0.9),
                    font_name="assets/Inconsolata-Bold",
                    font_size='16sp',
                    size_hint_y=None,
                    border=(-20, 16, 20, 16),
                    height=40)
            self.row_button_container.add_widget(self.row_containing_buttion)
        self.information_list_container.add_widget(self.row_button_container)

        self.add_widget(self.information_list_container)
    

    def change_type(self, i):
        if self.showed_type == "Customer":
            self.showed_type = "Agent"
        elif self.showed_type == "Agent":
            self.showed_type = "Customer"




