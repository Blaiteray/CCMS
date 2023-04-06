
import kivy
kivy.require('2.1.0')
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from hovekivy import HoverBehavior


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