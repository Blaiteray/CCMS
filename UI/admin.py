
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



# information_list_client = [
#     ["UserName1", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
#     ["UserName2", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
#     ["UserName3", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
#     ["UserName4", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
#     ["UserName5", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
#     ["UserName6", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
#     ["UserName7", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
#     ["UserName8", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
#     ["UserName9", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
#     ["UserName0", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 120.2],
# ]
# information_list_agent = [
#     ["Admin2", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["Admin1", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["Admin3", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["Admin4", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["Admin5", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["Admin6", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["Admin7", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["Admin8", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["Admin9", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["Admin0", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["UserNam11", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
#     ["UserNam12", "FName1", "LName1", "Gender", "xx-yy-zzzz", "432432432434", "seysfe@fesff.fesf", 12, 123.4],
# ]


class Admin_Widget(FloatLayout):
    def __init__(self, information_list_client, information_list_agent, **kwargs):
        super().__init__(**kwargs)
        self.information_list_client = information_list_client
        self.information_list_agent = information_list_agent
        #write your code from here
        self.main_label = Label(text="Admin Panel", 
            pos=(83,500), 
            size=(150, 40), 
            size_hint=(None, None), 
            font_size='28sp', 
            color=(41/255, 50/255, 70/255, 1),
            font_name="assets/static/Nunito-Bold")
        
        self.current_delete_category = "Customer"
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


        self.log_out_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="Log Out", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(80, 102), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        
        self.add_offer_button = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
            text="Add Offer", 
            background_color=(41/255, 50/255, 70/255, 0.9), 
            pos=(570, 102), 
            size=(150, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        
        with self.canvas:
            Color(41/255, 50/255, 70/255, 0.9)
            Rectangle(pos=(60, 80), size=(680, 390))

        self.information_list = []
        for item in information_list_client:
            username = item[0]+ " "*(16-len(item[0]))
            first_name = " "*(16-len(item[1]))+ item[1]
            last_name = item[2] + " "*(16-len(item[2]))
            self.information_list.append(f"  {username}        {first_name}    {last_name}  ")

        self.dummy_button = HoverButton((41/255, 50/255, 70/255, 1), (41/255, 50/255, 70/255, 1), 
                    text=f"  Username                    First Name    Last Name       ", 
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
            pos=(80, 155), 
            size=(640, 240), 
            size_hint=(None, None),
            scroll_wheel_distance = 100)
        self.row_button_container = BoxLayout(orientation='vertical',size_hint_y=None, height=len(self.information_list)*40)
        

        for row in self.information_list:
            row_containing_buttion = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
                    text=row, 
                    background_color=(41/255, 50/255, 70/255, 0.9),
                    font_name="assets/Inconsolata-Bold",
                    font_size='16sp',
                    size_hint_y=None,
                    border=(-20, 16, 20, 16),
                    height=40)
            row_containing_buttion.bind(on_release=self.view_info_popup)
            self.row_button_container.add_widget(row_containing_buttion)
        self.information_list_container.add_widget(self.row_button_container)

        t_username = ""
        self.current_delete_button = HoverButton((82/255, 100/255, 140/255, 0.7), (82/255, 100/255, 140/255, 0.9),
            text=t_username, 
            background_color=(82/255, 100/255, 140/255, 0.9),
            # pos=(270,185), 
            pos=(900,900), 
            size=(260, 34),
            font_name="assets/static/Nunito-Bold",
            font_size='16sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))



        self.add_widget(self.main_label)
        self.add_widget(self.type_button)
        self.add_widget(self.dummy_button)
        self.add_widget(self.information_list_container)
        self.add_widget(self.log_out_button)
        self.add_widget(self.add_offer_button)
        self.add_widget(self.current_delete_button)
    

    def update_information(self, information_list):
        remove_widget_recursive(self.information_list_container)
        self.information_list = []
        for item in information_list:
            username = item[0]+ " "*(16-len(item[0]))
            first_name = " "*(16-len(item[1]))+ item[1]
            last_name = item[2] + " "*(16-len(item[2]))
            self.information_list.append(f"  {username}        {first_name}    {last_name}  ")
        
        self.information_list_container = ScrollView(
            pos=(80, 155), 
            size=(640, 240), 
            size_hint=(None, None),
            scroll_wheel_distance = 100)
        self.row_button_container = BoxLayout(orientation='vertical',size_hint_y=None, height=len(self.information_list)*40)
        

        for row in self.information_list:
            row_containing_buttion = HoverButton((41/255, 50/255, 70/255, 0.7), (41/255, 50/255, 70/255, 0.9), 
                    text=row, 
                    background_color=(41/255, 50/255, 70/255, 0.9),
                    font_name="assets/Inconsolata-Bold",
                    font_size='16sp',
                    size_hint_y=None,
                    border=(-20, 16, 20, 16),
                    height=40)
            
            row_containing_buttion.bind(on_release=self.view_info_popup)
            self.row_button_container.add_widget(row_containing_buttion)
        self.information_list_container.add_widget(self.row_button_container)

        self.add_widget(self.information_list_container)
    

    def change_type(self, i):
        if self.showed_type == "Customer":
            self.showed_type = "Agent"
            self.type_button.text = "Agent"
            self.update_information(self.information_list_agent)
        elif self.showed_type == "Agent":
            self.showed_type = "Customer"
            self.type_button.text = "Customer"
            self.update_information(self.information_list_client)

    
    def view_info_popup(self, i):
        username = i.text[:22].strip()
        info = f"{username}"
        if self.showed_type == "Customer":
            for i in self.information_list_client:
                if i[0] == username:
                    info = f"User Name: {i[0]}\nFirst Name: {i[1]}\nLast Name: {i[2]}\nGender: {i[3]}\nDate of Birth: {i[4]}\nMobie: {i[5]}\nEmail: {i[6]}\nMinute Remaining: {i[7]} Minutes"
                    break
        elif self.showed_type == "Agent":
            for i in self.information_list_agent:
                if i[0] == username:
                    info = f"User Name: {i[0]}\nFirst Name: {i[1]}\nLast Name: {i[2]}\nGender: {i[3]}\nDate of Birth: {i[4]}\nMobie: {i[5]}\nEmail: {i[6]}\nCall Received: {i[7]}\nCall Duration: {i[8]} Minutes"
                    break
        content = FloatLayout()

        information_text = Label(text=info, 
            pos=(250,155), 
            size=(300, 300), 
            size_hint=(None, None), 
            font_size='16sp', 
            color=(1, 1, 1, 1),
            font_name="assets/Inconsolata-Bold")
        
        t_username = "Delete "+username
        self.current_delete_button.text = t_username
        self.current_delete_button.pos = (270,102)
        self.current_delete_category = self.showed_type

        content.add_widget(information_text)
        self.current_popup = MemoryPopup(content=content, 
            auto_dismiss=True, 
            size_hint=(.5, .5),
            separator_height=1,
            separator_color=(0.9, 1, 1, 1),
            background_color=(41/255, 50/255, 70/255, 0.9),
            title_font="assets/Inconsolata-Bold",
            title_size='16sp',
            title='Details Information')
        self.current_popup.open()
        




