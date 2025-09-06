import mset
from base.container_widget import ContainerWidget


class FormLayout(ContainerWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _create_mset_elements(self, parent_window):
        for widget in self.child_widgets:
            widget.add_to_window(parent_window)

    def add_form_row(self, label_widget, control_widget):
        self.add_child(label_widget)
        self.add_child(control_widget)