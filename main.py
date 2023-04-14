"""
Call center management system
"""

import sqlite3

database = sqlite3.connect("ccms_database.db")
database.execute("""CREATE TABLE IF NOT EXISTS Client(
                 user_name TEXT PRIMARY KEY,
                 first_name TEXT,
                 last_name TEXT,
                 password TEXT,
                 gender TEXT,
                 date_of_birth TEXT,
                 mobile TEXT,
                 email TEXT,
                 minute_remaining REAL)""")

database.execute("""CREATE TABLE IF NOT EXISTS Agent(
                 user_name TEXT PRIMARY KEY,
                 first_name TEXT,
                 last_name TEXT,
                 password TEXT,
                 gender TEXT,
                 date_of_birth TEXT,
                 mobile TEXT,
                 email TEXT,
                 call_reveived INTEGER,
                 call_duration REAL,
                 status TEXT)""")

database.execute("""CREATE TABLE IF NOT EXISTS Category(
                 user_name TEXT,
                 category TEXT,
                 PRIMARY KEY (user_name, category),
                 FOREIGN KEY(user_name) REFERENCES Agent(user_name) ON UPDATE CASCADE ON DELETE CASCADE)""")

database.execute("""CREATE TABLE IF NOT EXISTS Offer(
                 offer_id TEXT PRIMARY KEY,
                 minute INTEGER,
                 price REAL,
                 last_date TEXT)""")

database.execute("""CREATE TABLE IF NOT EXISTS Payment(
                 payment_id TEXT PRIMARY KEY,
                 date TEXT,
                 user_name TEXT,
                 offer_id,
                 FOREIGN KEY(user_name) REFERENCES Client(user_name) ON UPDATE CASCADE ON DELETE CASCADE,
                 FOREIGN KEY(offer_id) REFERENCES Offer(offer_id) ON UPDATE CASCADE ON DELETE CASCADE)""")

database.execute("""CREATE TABLE IF NOT EXISTS Make_Call(
                 dial_token TEXT PRIMARY KEY,
                 status TEXT,
                 selected_category TEXT,
                 start_time TEXT,\
                 connection_start_time TEXT,
                 user_name TEXT,
                 end_time TEXT,
                 agent_id TEXT,
                 FOREIGN KEY(user_name) REFERENCES Client(user_name) ON UPDATE CASCADE ON DELETE CASCADE,
                 FOREIGN KEY(agent_id) REFERENCES Agent(user_name) ON UPDATE CASCADE ON DELETE CASCADE)""")

database.commit()


import os
os.environ['KIVY_IMAGE'] = 'pil'
# os.environ["KIVY_NO_CONSOLELOG"] = "1"
from datetime import datetime

import kivy
kivy.require('2.1.0')
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.set('graphics','resizable', False)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.app import App 
from kivy.core.window import Window
# Window.minimum_width, Window.minimum_height = (800, 600)
Window.clearcolor = (0.05, 0.1, 0.15, 1)
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
from kivy.uix.screenmanager import Screen, ScreenManager
from hovekivy import HoverBehavior
from UI.login import Login_Widget
from UI.signup import Signup_Widget
from UI.profile import Profile_Widget
from UI.offer import Offer_Widget
from UI.edit_profile import Edit_Profile_Widget
from UI.purchase_history import Purchase_History_Widget
from UI.agent_dashboard import Agent_Dashboard_Widget
from UI.category_selection import Category_Selection_Widget
from UI.agent_category_selection import Agent_Category_Selection_Widget
from UI.purchase import Purchase_Widget
from modified_widget import *

with Window.canvas.before:
    Color(0.95, 0.96, 1, 1)
    # Image(source='bg_img.jpg', size=(800, 600))
    Rectangle(size=Window.size, source="img/bg_img.jpg", pos=(0,0))



class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        self.main_screen_manager = ScreenManager()

        self.login = Login_Widget()
        self.login.signup_button.bind(on_release=self.signup_button_callback)
        self.login.login_button.bind(on_release=self.login_login_button_callback)

        self.signup = Signup_Widget()
        self.signup.register_button.bind(on_release=self.regester_button_callback)
        self.signup.login_button.bind(on_release=self.signup_login_callback)

        self.profile = Profile_Widget()
        self.profile.edit_button.bind(on_release=self.edit_button_callback)
        self.profile.log_out_button.bind(on_release=self.logout_button_callback)
        self.profile.menu_button.bind(on_release=self.customer_menu_button_callback_popup)


        offer_list = list(database.execute("SELECT * FROM Offer"))
        selected_offer_list = []
        for offer in offer_list:
            if self.compare_date(datetime.now().strftime("%d-%m-%Y"), offer[3]):
                selected_offer_list.append(offer)
        self.offer = Offer_Widget(selected_offer_list)
        self.offer.cancel_button.bind(on_release=self.offer_cancel_button_callback)
        self.offer.history_button.bind(on_release=self.offer_history_button_callback)
        for offer_button in self.offer.offer_button_list:
            offer_button.bind(on_release=self.offer_selected_callback)

        self.edit_profile = Edit_Profile_Widget()
        self.edit_profile.cancel_button.bind(on_release=self.edit_cancel_button_callback)
        self.edit_profile.done_button.bind(on_release=self.edit_done_button_callback)

        self.purchase = Purchase_Widget()
        self.purchase.cancel_button.bind(on_release=self.purchase_cancel_callback)
        self.purchase.purchase_button.bind(on_release=self.purchase_confirm_callback_popup)

        self.purchase_history = Purchase_History_Widget()
        self.purchase_history.close_button.bind(on_release=self.purchase_history_close_callback)

        self.agent_dashboard = Agent_Dashboard_Widget()
        self.agent_dashboard.edit_button.bind(on_release=self.edit_button_callback)
        self.agent_dashboard.log_out_button.bind(on_release=self.logout_button_callback)
        # self.agent_dashboard.receive_call_button.bind(on_release)

        self.category_selection = Category_Selection_Widget()
        self.agent_category_selection = Agent_Category_Selection_Widget()
        self.agent_category_selection.select_button.bind(on_release=self.agent_category_selection_callback)

        self.login_screen = Screen(name='login')
        self.login_screen.add_widget(self.login)

        self.signup_screen = Screen(name='signup')
        self.signup_screen.add_widget(self.signup)

        self.offer_screen = Screen(name='offer')
        self.offer_screen.add_widget(self.offer)

        self.profile_screen = Screen(name='profile')
        self.profile_screen.add_widget(self.profile)

        self.edit_profile_screen = Screen(name='edit_profile')
        self.edit_profile_screen.add_widget(self.edit_profile)

        self.purchase_screen = Screen(name='purchase')
        self.purchase_screen.add_widget(self.purchase)

        self.purchase_history_screen = Screen(name='purchase_history')
        self.purchase_history_screen.add_widget(self.purchase_history)

        self.agent_dashboard_screen = Screen(name='agent_dashboard')
        self.agent_dashboard_screen.add_widget(self.agent_dashboard)

        self.category_selection_screen = Screen(name='category_selection')
        self.category_selection_screen.add_widget(self.category_selection)

        self.agent_category_selection_screen = Screen(name='agent_category_selection')
        self.agent_category_selection_screen.add_widget(self.agent_category_selection)





        self.main_screen_manager.add_widget(self.login_screen)
        self.main_screen_manager.current = 'login'


        self.add_widget(self.main_screen_manager)



    def signup_regester_completion_popup(self):
        content = FloatLayout()

        successful_label = Label(text="Signup Successful!", 
            pos=(300,300), 
            size=(200, 40), 
            size_hint=(None, None), 
            font_size='24sp', 
            color=(1, 1, 1, 1),
            font_name="assets/static/Nunito-Bold")
        
        go_login_button = HoverButton((82/255, 100/255, 140/255, 0.7), (82/255, 100/255, 140/255, 0.9),
            text="LOGIN", 
            background_color=(82/255, 100/255, 140/255, 0.9),
            pos=(270,215), 
            size=(260, 34),
            font_name="assets/static/Nunito-Bold",
            font_size='16sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        content.add_widget(go_login_button)
        content.add_widget(successful_label)
        popup = MemoryPopup(content=content, 
            auto_dismiss=False, 
            size_hint=(.4, .4),
            separator_height=0,
            separator_color=(0.9, 1, 1, 1),
            background_color=(41/255, 50/255, 70/255, 0.9),
            title_font="assets/static/Nunito-Bold",
            title_size='16sp',
            title='')
        def go_login_button_callback(i):
            self.main_screen_manager.switch_to(self.login_screen, direction='right')
            popup.dismiss()
        go_login_button.bind(on_press=go_login_button_callback)
        popup.open()

    def error_popup(self, msg):
        content = FloatLayout()

        error_label = Label(text=msg, 
            pos=(250,300), 
            size=(300, 40), 
            size_hint=(None, None), 
            font_size='18sp', 
            color=(1, 1, 1, 1),
            font_name="assets/static/Nunito-Bold")
        
        go_login_button = HoverButton((82/255, 100/255, 140/255, 0.7), (82/255, 100/255, 140/255, 0.9),
            text="OK", 
            background_color=(82/255, 100/255, 140/255, 0.9),
            pos=(270,215), 
            size=(260, 34),
            font_name="assets/static/Nunito-Bold",
            font_size='16sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        content.add_widget(go_login_button)
        content.add_widget(error_label)
        popup = MemoryPopup(content=content, 
            auto_dismiss=False, 
            size_hint=(.4, .4),
            separator_height=0,
            separator_color=(0.9, 1, 1, 1),
            background_color=(41/255, 50/255, 70/255, 0.9),
            title_font="assets/static/Nunito-Bold",
            title_size='16sp',
            title='')
        def ok_button_callback(i):
            popup.dismiss()
        go_login_button.bind(on_press=ok_button_callback)
        popup.open()
    

    def customer_menu_button_callback_popup(self, i):
        content = FloatLayout()

        menu_label = Label(text="MENU", 
            pos=(250,350), 
            size=(300, 40), 
            size_hint=(None, None), 
            font_size='18sp', 
            color=(1, 1, 1, 1),
            font_name="assets/static/Nunito-Bold")
        
        call_button = HoverButton((82/255, 100/255, 140/255, 0.7), (82/255, 100/255, 140/255, 0.9),
            text="Make Call", 
            background_color=(82/255, 100/255, 140/255, 0.9),
            pos=(270,265), 
            size=(260, 34),
            font_name="assets/static/Nunito-Bold",
            font_size='16sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        purchase_button = HoverButton((82/255, 100/255, 140/255, 0.7), (82/255, 100/255, 140/255, 0.9),
            text="Purchase Minures", 
            background_color=(82/255, 100/255, 140/255, 0.9),
            pos=(270,215), 
            size=(260, 34),
            font_name="assets/static/Nunito-Bold",
            font_size='16sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        content.add_widget(call_button)
        content.add_widget(menu_label)
        content.add_widget(purchase_button)
        popup = MemoryPopup(content=content, 
            auto_dismiss=True, 
            size_hint=(.4, .4),
            separator_height=0,
            separator_color=(0.9, 1, 1, 1),
            background_color=(41/255, 50/255, 70/255, 0.7),
            title_font="assets/static/Nunito-Bold",
            title_size='16sp',
            title='')
        def call_button_popup(i):
            popup.dismiss()
        def purchase_button_callback(i):
            self.main_screen_manager.switch_to(self.offer_screen, direction='left')
            popup.dismiss()
        call_button.bind(on_press=call_button_popup)
        purchase_button.bind(on_press=purchase_button_callback)
        popup.open()
    

    def purchase_confirm_callback_popup(self, i):
        msg = "Purchase Successful!"
        if self.purchase.postal.text == '' or self.purchase.card_no.text == '':
            msg = "Fill up the informations!"
        else:
            purhcase_no = list(database.execute("SELECT payment_id FROM Payment"))
            if len(purhcase_no) == 0:
                purhcase_no = '0'
            else:
                purhcase_no = str(int(purhcase_no[-1][0])+1)
            purhcase_no = "0"*(6-len(purhcase_no))+purhcase_no
            date = datetime.now().strftime("%d-%m-%Y")
            database.execute("INSERT INTO Payment VALUES (?, ?, ?, ?)", (purhcase_no, date, self.logged_in_user_name, self.selected_offer_id))
            remaining_minures = self.logged_in_info[0][-1]
            self.logged_in_info[0] = list(self.logged_in_info[0][:-1])
            self.logged_in_info[0].append(remaining_minures + self.selected_offer_minutes)
            database.execute("UPDATE Client SET minute_remaining=? WHERE user_name=?", (self.logged_in_info[0][-1], self.logged_in_user_name))
            database.commit()

            self.profile.update_minute_remaining(self.logged_in_info[0][-1])
        content = FloatLayout()

        msg_label = Label(text=msg, 
            pos=(250,300), 
            size=(300, 40), 
            size_hint=(None, None), 
            font_size='18sp', 
            color=(1, 1, 1, 1),
            font_name="assets/static/Nunito-Bold")
        
        go_login_button = HoverButton((82/255, 100/255, 140/255, 0.7), (82/255, 100/255, 140/255, 0.9),
            text="OK", 
            background_color=(82/255, 100/255, 140/255, 0.9),
            pos=(270,215), 
            size=(260, 34),
            font_name="assets/static/Nunito-Bold",
            font_size='16sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))
        content.add_widget(go_login_button)
        content.add_widget(msg_label)
        popup = MemoryPopup(content=content, 
            auto_dismiss=False, 
            size_hint=(.4, .4),
            separator_height=0,
            separator_color=(0.9, 1, 1, 1),
            background_color=(41/255, 50/255, 70/255, 0.9),
            title_font="assets/static/Nunito-Bold",
            title_size='16sp',
            title='')
        def ok_button_callback(i):
            if msg == "Purchase Successful!":
                self.purchase.postal.text = ''
                self.purchase.card_no.text = ''
                self.main_screen_manager.switch_to(self.profile_screen, direction='right')
            popup.dismiss()
        go_login_button.bind(on_press=ok_button_callback)
        popup.open()


    def signup_button_callback(self, i):
        self.main_screen_manager.switch_to(self.signup_screen, direction='left')

    
    def login_login_button_callback(self, i):
        self.logged_in_user_name = self.login.user_name.text
        password = self.login.password.text
        self.logged_in_info = None
        if self.login.login_as == "Customer":
            self.logged_in_info = list(database.execute("SELECT * FROM Client WHERE user_name = ? AND password = ?", (self.logged_in_user_name, password)))
            if len(self.logged_in_info) == 0:
                self.error_popup("User Name or Password don't \nMatch!")
            else:
                self.profile.update_info(*self.logged_in_info[0][:3], *self.logged_in_info[0][4:])
                self.main_screen_manager.switch_to(self.profile_screen, direction='left')
        elif self.login.login_as == "Agent":
            self.logged_in_info = list(database.execute("SELECT * FROM Agent WHERE user_name = ? AND password = ?", (self.logged_in_user_name, password)))
            if len(self.logged_in_info) == 0:
                self.error_popup("User Name or Password don't \nMatch!")
            else:
                categories = list(database.execute("SELECT category FROM Category WHERE user_name=?", (self.logged_in_user_name,)))
                m_categories = []
                for category in categories:
                    m_categories.append(category[0])
                self.agent_dashboard.update_info(*self.logged_in_info[0][:3], *self.logged_in_info[0][4:-1], m_categories)
                self.main_screen_manager.switch_to(self.agent_dashboard_screen, direction='left')


    def regester_button_callback(self, i):
        user_name = self.signup.user_name.text
        password = self.signup.password.text
        first_name = self.signup.first_name.text
        last_name = self.signup.last_name.text
        gender = self.signup.gender.text
        date_of_birth = self.signup.date_of_birth.text
        mobile = self.signup.mobile.text
        email = self.signup.email.text

        dob = self.signup.date_of_birth.text.split('-')
        check_username = list(database.execute("SELECT * FROM Client WHERE user_name=?", (user_name,)))

        if len(check_username) > 0:
            self.error_popup("User Name Already Exists!")
        elif len(self.signup.password.text) < 4:
            self.error_popup("Password Too Short!")
        elif self.signup.password.text != self.signup.password_confirm.text:
            self.error_popup("Password Don't Match!")
        elif not self.signup.gender.text in ['Male', 'Female']:
            self.error_popup("Gender either Male or Female")
        elif len(dob) != 3 or not (len(dob[0])+2==len(dob[1])+2==len(dob[2])==4) or not (dob[0].isdigit() and dob[1].isdigit() and dob[2].isdigit()):
            self.error_popup("Date format should be \ndd-mm-yyyy")
        elif self.signup.first_name.text == '' or self.signup.last_name.text == '' or self.signup.mobile == '' or self.signup.email == '':
            self.error_popup("Missing required information!")
        elif self.signup.signup_as == "Customer":
            database.execute("INSERT INTO Client VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_name, first_name, last_name, password, gender, date_of_birth, mobile, email, 100))
            database.commit()
            self.signup_regester_completion_popup()
        elif self.signup.signup_as == "Agent":
            database.execute("INSERT INTO Agent VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_name, first_name, last_name, password, gender, date_of_birth, mobile, email, 0, 0, "Inactive"))
            database.commit()
            self.main_screen_manager.switch_to(self.agent_category_selection_screen, direction='left')
        

    def signup_login_callback(self, i):
        self.main_screen_manager.switch_to(self.login_screen, direction='right')
    

    def edit_button_callback(self, i):
        if self.login.login_as == "Customer":
            self.edit_profile.update_info(*self.logged_in_info[0][:-1])
        elif self.login.login_as == "Agent":
            self.edit_profile.update_info(*self.logged_in_info[0][:-3])
        self.main_screen_manager.switch_to(self.edit_profile_screen, direction='left')
    

    def logout_button_callback(self, i):
        self.main_screen_manager.switch_to(self.login_screen, direction='right')
    
    
    def edit_cancel_button_callback(self, i):
        if self.login.login_as == "Customer":
            self.main_screen_manager.switch_to(self.profile_screen, direction='right')
        elif  self.login.login_as == "Agent":
            self.main_screen_manager.switch_to(self.agent_dashboard_screen, direction='right')
    

    def edit_done_button_callback(self, i):
        user_name = self.edit_profile.user_name.text
        password = self.edit_profile.password.text
        first_name = self.edit_profile.first_name.text
        last_name = self.edit_profile.last_name.text
        gender = self.edit_profile.gender.text
        date_of_birth = self.edit_profile.date_of_birth.text
        mobile = self.edit_profile.mobile.text
        email = self.edit_profile.email.text

        dob = self.edit_profile.date_of_birth.text.split('-')

        if len(self.edit_profile.password.text) < 4:
            self.error_popup("Password Too Short!")
        elif self.edit_profile.password.text != self.edit_profile.password_confirm.text:
            self.error_popup("Password Don't Match!")
        elif not self.edit_profile.gender.text in ['Male', 'Female']:
            self.error_popup("Gender either Male or Female")
        elif len(dob) != 3 or not (len(dob[0])+2==len(dob[1])+2==len(dob[2])==4) or not (dob[0].isdigit() and dob[1].isdigit() and dob[2].isdigit()):
            self.error_popup("Date format should be \ndd-mm-yyyy")
        elif self.edit_profile.first_name.text == '' or self.edit_profile.last_name.text == '' or self.edit_profile.mobile == '' or self.edit_profile.email == '':
            self.error_popup("Missing required information!")
        elif self.login.login_as == "Customer":
            database.execute("UPDATE Client SET first_name=?, last_name=?, password=?, gender=?, date_of_birth=?, mobile=?, email=? WHERE user_name=?", (first_name, last_name, password, gender, date_of_birth, mobile, email, user_name))
            database.commit()
            self.logged_in_info[0] = [user_name, first_name, last_name, password, gender, date_of_birth, mobile, email, self.logged_in_info[0][-1]]
            self.profile.update_info(*self.logged_in_info[0][:3], *self.logged_in_info[0][4:])
            self.main_screen_manager.switch_to(self.profile_screen, direction='right')
        elif self.login.login_as == "Agent":
            database.execute("UPDATE Agent SET first_name=?, last_name=?, password=?, gender=?, date_of_birth=?, mobile=?, email=? WHERE user_name=?", (first_name, last_name, password, gender, date_of_birth, mobile, email, user_name))
            database.commit()
            self.logged_in_info[0] = [user_name, first_name, last_name, password, gender, date_of_birth, mobile, email, self.logged_in_info[0][-3], self.logged_in_info[0][-2], self.logged_in_info[0][-1]]
            categories = list(database.execute("SELECT category FROM Category WHERE user_name=?", (self.logged_in_user_name,)))
            m_categories = []
            for category in categories:
                m_categories.append(category[0])
            self.agent_dashboard.update_info(*self.logged_in_info[0][:3], *self.logged_in_info[0][4:-1], m_categories)
            self.main_screen_manager.switch_to(self.agent_dashboard_screen, direction='right')




    
    def offer_cancel_button_callback(self, i):
        if self.login.login_as == "Customer":
            self.main_screen_manager.switch_to(self.profile_screen, direction='right')
        elif  self.login.login_as == "Agent":
            self.main_screen_manager.switch_to(self.agent_dashboard_screen, direction='right')
    

    def offer_history_button_callback(self, i):
        history_list = list(database.execute("SELECT o.* FROM Payment p LEFT JOIN Offer o ON p.offer_id=o.offer_id WHERE p.user_name=?", (self.logged_in_user_name,)))
        self.purchase_history.update_history(history_list)
        self.main_screen_manager.switch_to(self.purchase_history_screen, direction='left')

    
    def offer_selected_callback(self, i):
        self.selected_offer_id = i.text[:16].strip()
        self.selected_offer_minutes = int(i.text[18:26].strip())
        price = float(i.text[44:54].strip())
        self.main_screen_manager.switch_to(self.purchase_screen, direction='left')

    
    def purchase_history_close_callback(self, i):
        self.main_screen_manager.switch_to(self.offer_screen, direction='right')


    def purchase_cancel_callback(self, i):
        self.main_screen_manager.switch_to(self.offer_screen, direction='right')
    

    def agent_category_selection_callback(self, i):
        if len(self.agent_category_selection.selected_category) > 0:
            user_name = self.signup.user_name.text
            for category in self.agent_category_selection.selected_category:
                database.execute("INSERT INTO Category VALUES(?, ?)", (user_name, category))
            database.commit()
            self.main_screen_manager.switch_to(self.agent_dashboard_screen, direction='left')
        else:
            self.error_popup("Select at least one option!")

    
    def compare_date(self, date1, date2):
        date1 = date1.split("-")
        date2 = date2.split("-")
        date1.reverse()
        date2.reverse()
        date1 = "".join(date1)
        date2 = "".join(date2)
        return date1 <= date2

       





class Main_Window(App):
    def build(self):
        return MainLayout()

Main_Window().run()


database.close()