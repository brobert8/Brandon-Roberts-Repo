import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyDesign(GridLayout):
    def __init__(self, **kwargs):
        super(MyDesign, self).__init__(**kwargs)

        self.cols = 1
        self.rows = 3

        self.add_widget(Label(text="Welcome to safe rider", font_size = 70, font_color = blue))

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="email"))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text="password"))
        self.password = TextInput(multiline=False)
        self.inside.add_widget(self.password)

        self.add_widget(self.inside)

        self.submit = Button(text="Create Account")
        self.submit.bind(on_press=self.ButtonAction)
        self.add_widget(self.submit)

    def ButtonAction(self, instance):
        email = self.email.text
        password = self.password.text
        print("user email is " + email + " and user pass is " + password)
        #clear text for next update
        self.email.text = ""
        self.password.text = ""

class MyApp(App):
    def build(self):
        return MyDesign()

if __name__ == '__main__':
    MyApp().run()