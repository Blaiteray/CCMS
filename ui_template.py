"""
A note keeping tool
"""

import os
os.environ['KIVY_IMAGE'] = 'pil'
# os.environ["KIVY_NO_CONSOLELOG"] = "1"

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
# from kivy.uix.screenmanager import Screen, ScreenManager
from hovekivy import HoverBehavior

with Window.canvas.before:
    Color(0.9, 0.8, 0.7, 0.5) 
    # Image(source='bg_img.jpg', size=(800, 600))
    Rectangle(size=Window.size, source="bg_img.jpg", pos=(0,0))


class HoverButton(Button, HoverBehavior):
    def __init__(self, enter, leave, **kwargs):
        super(HoverButton, self).__init__(**kwargs)
        self.enter = enter
        self.leave = leave
        # self.background_color = (0, 0, 0, 1)
    def on_enter(self):
        self.background_color = self.enter
    def on_leave(self):
        self.background_color = self.leave


class HoverTextInput(TextInput, HoverBehavior):
    def __init__(self, enter, leave, **kwargs):
        super(HoverTextInput, self).__init__(**kwargs)
        self.enter = enter
        self.leave = leave
        # self.background_color = (0, 0, 0, 1)
    def on_enter(self):
        self.background_color = self.enter
    def on_leave(self):
        self.background_color = self.leave


class MemoryPopup(Popup):
    def __init__(self, **kwargs):
        super(MemoryPopup, self).__init__(**kwargs)

    def on_dismiss(self):
        self.clear_widgets()

    def clear_widgets(self):
        for child in self.content.children:
            if isinstance(child, Popup):
                child.clear_widgets()
            else:
                self.content.remove_widget(child)


def remove_widget_recursive(widget):
    for child in widget.children:
        remove_widget_recursive(child)
    if widget.parent:
        widget.parent.remove_widget(widget)


class MainLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #write your code from here





class Main_Window(App):
    def build(self):
        return MainLayout()

Main_Window().run()
