from typing import List
from base.base_widget import BaseWidget


class ContainerWidget(BaseWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.child_widgets: List[BaseWidget] = []

    def add_child(self, widget: BaseWidget):
        if widget and widget not in self.child_widgets:
            self.child_widgets.append(widget)

    def clear_children(self):
        for widget in self.child_widgets:
            widget.destroy()
        self.child_widgets.clear()

    def destroy(self):
        self.clear_children()
        super().destroy()

    def remove_child(self, widget: BaseWidget):
        if widget in self.child_widgets:
            widget.destroy()
            self.child_widgets.remove(widget)

    @BaseWidget.enabled.setter
    def enabled(self, value: bool):
        BaseWidget.enabled.fset(self, value)
        for widget in self.child_widgets:
            widget.enabled = value

    @BaseWidget.visible.setter
    def visible(self, value: bool):
        BaseWidget.visible.fset(self, value)
        for widget in self.child_widgets:
            widget.visible = value