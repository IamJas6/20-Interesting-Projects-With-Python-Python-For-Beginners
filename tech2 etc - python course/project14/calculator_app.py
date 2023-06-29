from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class mainapp(App):
    def op(self):
        self.icon="download2.png"
        self.operators=["/","*","+","-"]
        self.last_op_was=None
        self.last_button=None

        Main_layout=BoxLayout(orientation="vertical")
        self.solution=TextInput(background_color="black", foreground_color="white",multiline=False,halign="center",font_size=55,readonly=True)
        Main_layout.add_widget(self.solution)
        buttons=[
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","+"],
            [".","0","clear","-"],
        ]
        for row in buttons:
            h_layout=BoxLayout()
            for label in row:
                button=Button(text=label,font_size=30,backgrounf_color="red",pos_hint={"center_x":0.5,"center_y":0.5},)
                h_layout.add_widget(button)
                button.bind(on_press=self.on_button_press)
            Main_layout.add_widget(h_layout)

        equal_button=Button(text="=",font_size=30,backgrounf_color="red",pos_hint={"center_x":0.5,"center_y":0.5},)
        equal_button.bind(on_press=self.on_solution)
        Main_layout.add_widget(equal_button)
        return Main_layout
    def on_button_press(self, instance):
        current=self.solution.text
        button_text=instance.text
        if button_text=="clear":
            self.solution.text=""
        else:
            if current and (self.last_op_was and button_text in self.operators):
                return
            elif current=="" and button_text in self.operators:
                return
            else:
                 new_text=current+button_text
                 self.solution.text=new_text
        self.last_button=button_text
        self.last_op_was=self.last_button in self.operators

    def on_solution(self, instance):
        text=self.solution.text
        if text:
            solution=str(eval(self.solution.text))
            self.solution.text=solution




if __name__=="__main__":
    app=mainapp()
    app.run()
