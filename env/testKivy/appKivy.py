from kivy.app import App
from kivy.uix.label import Label

class testApp(App):
    def build(self):
        label = Label(text="Hello Word")
        return label
    
app = testApp()    
app.run()