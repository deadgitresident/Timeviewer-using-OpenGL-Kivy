import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.clock import Clock
import time

class TimeViewer(BoxLayout):
    def __init__(self, **kwargs):
        super(TimeViewer, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.time_label = Label(font_size=64, font_name='Roboto', color=(1, 1, 1, 1))
        self.date_label = Label(font_size=24, font_name='Roboto', color=(1, 1, 1, 1))
        self.add_widget(self.time_label)
        self.add_widget(self.date_label)
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y-%m-%d")
        self.time_label.text = current_time
        self.date_label.text = current_date

class TimeViewerApp(App):
    def build(self):
        self.root = TimeViewer()
        with self.root.canvas.before:
            Color(0, 0, 0, 1)  # Black background
        return self.root

if __name__ == '__main__':
    TimeViewerApp().run()