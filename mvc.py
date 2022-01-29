class Model:
    def __init__(self):
        self.views = []

    def attach(self, view):
        self.views.append(view)

    def detach(self, view):
        self.views.remove(view)

    def notify(self):
        for view in self.views:
            view.update()


class View:
    def __init__(self, model: Model, parent = None):
        self.model = model
        self.parent = parent
        self.children = []
        self.controller = Controller(model, self)

    def update(self):
        for child_view in self.children:
            child_view.update()

    def add_child(self, child_view):
        self.children.append(child_view)

    def remove_child(self, child_view):
        self.children.remove(child_view)


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
