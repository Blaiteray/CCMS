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
store = {
    'offer_id' : 'sdf153',
    'minute' : 123,
    'price' : 124.23
}

class Purchase_Widget(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here
        offset = 28  # qu
        with self.canvas:
            Color(0.3, 0.4, 0.6, 0.5)
            Rectangle(pos=(400, 20), size=(380, 560))
        with self.canvas:
            Color(0.95, 0.96, 1, 0.95)
            Rectangle(pos=(20, 140), size=(380, 380), source="img/purchase.png")

        self.purchase_store = Label(text="Purchase Store",
            pos=(450, offset + 40 * 10 + 20),
            size=(180, 35),
            size_hint=(None, None),
            font_size='28sp',
            color=(41 / 255, 50 / 255, 70 / 255, 1),
            font_name="assets/static/Nunito-Bold")

        self.offer_id_label = Label(text="Offer ID  : ",
            pos=(457, offset + 40 * 9 + 20 - 20),
            size=(80, 40),
            size_hint=(None, None),
            font_size='18sp',
            color=(41 / 255, 50 / 255, 70 / 255, 1),
            font_name="assets/Inconsolata-Bold")

        self.offer_id = Label(text=store['offer_id'] + " " * (8 - len(store['offer_id'])),
            pos=(555, offset + 40 * 9 + 20 -20),
            size=(80, 40),
            size_hint=(None, None),
            font_size='18sp',
            color=(41 / 255, 50 / 255, 70 / 255, 1),
            font_name="assets/Inconsolata-Bold")

        self.minute_label = Label(text="Minute    : ",
            pos=(457, offset + 40 * 8 + 20 -10),
            size=(80, 40),
            size_hint=(None, None),
            font_size='18sp',
            color=(41 / 255, 50 / 255, 70 / 255, 1),
            font_name="assets/Inconsolata-Bold")

        self.minute = Label(text=str(store['minute'] )+ " " * (8 - len(str(store['minute']))),
            pos=(555, offset + 40 * 8 + 20 -10),
            size=(80, 40),
            size_hint=(None, None),
            font_size='18sp',
            color=(41 / 255, 50 / 255, 70 / 255, 1),
            font_name="assets/Inconsolata-Bold")

        self.price_label = Label(text="Price     : ",
            pos=(457, offset + 40 * 7 + 20),
            size=(80, 40),
            size_hint=(None, None),
            font_size='18sp',
            color=(41 / 255, 50 / 255, 70 / 255, 1),
            font_name="assets/Inconsolata-Bold")

        self.price = Label(text=str(store['price'] )+ " " * (8 - len(str(store['price']))),
            pos=(555, offset + 40 * 7 + 20),
            size=(80, 40),
            size_hint=(None, None),
            font_size='18sp',
            color=(41 / 255, 50 / 255, 70 / 255, 1),
            font_name="assets/Inconsolata-Bold")

        self.postal = HoverTextInput((1, 1, 1, 1), (239 / 255, 243 / 255, 255 / 255, 1),
            text='',
            hint_text='Postal/Zip code: ',
            background_color=(239 / 255, 243 / 255, 255 / 255, 1),
            pos=(440, offset + 40 * 6),
            size=(300, 30),
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))

        self.card_no = HoverTextInput((1, 1, 1, 1), (239 / 255, 243 / 255, 255 / 255, 1),
            text='',
            hint_text='Card No: ',
            background_color=(239 / 255, 243 / 255, 255 / 255, 1),
            pos=(440, offset + 40 * 5),
            size=(300, 30),
            font_name="assets/static/Nunito-Regular",
            font_size=14,
            multiline=False,
            size_hint=(None, None))

        self.purchase = HoverButton((41 / 255, 50 / 255, 70 / 255, 0.7), (41 / 255, 50 / 255, 70 / 255, 0.9),
            text="PURCHASE",
            background_color=(41 / 255, 50 / 255, 70 / 255, 0.9),
            pos=(440, offset + 120),
            size=(300, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))

        self.cancel = HoverButton((160 / 255, 198 / 255, 255 / 255, 0.7), (160 / 255, 198 / 255, 255 / 255, 0.9),
            text="CANCEL",
            background_color=(160 / 255, 198 / 255, 255 / 255, 0.9),
            pos=(440, offset + 80),
            size=(300, 35),
            font_name="assets/static/Nunito-Bold",
            font_size='15sp',
            color=(1, 1, 1, 1),
            size_hint=(None, None))

        self.add_widget(self.purchase_store)
        self.add_widget(self.offer_id)
        self.add_widget(self.minute)
        self.add_widget(self.price)
        self.add_widget(self.postal)
        self.add_widget(self.card_no)
        self.add_widget(self.purchase)
        self.add_widget(self.cancel)
        self.add_widget(self.offer_id_label)
        self.add_widget(self.minute_label)
        self.add_widget(self.price_label)