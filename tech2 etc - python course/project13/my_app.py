import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

#creating structure
#child class
class child_app(GridLayout):
    def __init__(self,**kwargs):
        super(child_app,self).__init__()
        self.cols=2
        self.add_widget(Label(text='Student name'))
        self.s_name=TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Student marks'))
        self.s_marks=TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text='Student gender'))
        self.s_gender=TextInput()
        self.add_widget(self.s_gender)

        self.press=Button(text="Save")
        self.press.bind(on_press=self.save)
        self.add_widget(self.press)

    def save(self, instance):
        print(f"Name of the student: {self.s_name.text}")
        print(f"Gender of the student: {self.s_gender.text}")
        print(f"Marks of the student: {self.s_marks.text}")
        print("")


#parent class
class parent_app(App):
    def build(self):
        return child_app()

if __name__=="__main__":
    parent_app().run()