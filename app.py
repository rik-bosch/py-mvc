from tkinter import *
from tkinter import ttk
from mvc import (Model, View, Controller)


class MessageModel(Model):
    def __init__(self, message: str):
        super().__init__()
        self.message = message

    @staticmethod
    def open():
        model = MessageModel("Hallo wereld!")
        main_view = MainView(model, "Test app")
        model.attach(main_view)
        main_view.add_child(TextView(model, main_view))
        main_view.add_child(ButtonView(model, main_view, "Klik mij", model, model.say_goodbye.__func__))
        main_view.run()

    def say_goodbye(self):
        self.message = "Tot ziens!"
        self.notify()


class MainView(View):
    def __init__(self, model: Model, title: str):
        super().__init__(model)
        self.window = Tk()
        self.window.title(title)
        self.frame = ttk.Frame(self.window)
        self.frame.grid()

    def run(self):
        self.window.mainloop()


class TextView(View):
    def __init__(self, model: MessageModel, parent: MainView):
        super().__init__(model, parent)
        self.textVar = StringVar(value=model.message)
        self.label = ttk.Label(parent.frame, textvariable=self.textVar)
        self.label.grid()

    def update(self):
        self.textVar.set(self.model.message)


class ButtonView(View):
    def __init__(self, model: Model, parent: MainView, label: str, target: object, method: callable):
        super().__init__(model, parent)
        self.controller = ButtonController(model, self, target, method)
        self.button = ttk.Button(parent.frame, text=label, command=self.controller)
        self.button.grid()


class ButtonController(Controller):
    def __init__(self, model: Model, view: ButtonView, target: object, method: callable):
        super().__init__(model, view)
        self.target = target
        self.target_method = method

    def __call__(self):
        self.target_method(self.target)


if __name__ == '__main__':
    MessageModel.open()
