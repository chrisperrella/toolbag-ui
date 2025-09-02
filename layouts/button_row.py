from typing import List
from ..base.container_widget import ContainerWidget
from ..components.action_button import ActionButton

import mset


class ButtonRow(ContainerWidget):
    def __init__(self, label_text: str = "", **kwargs):
        super().__init__(**kwargs)
        self.buttons: List[ActionButton] = []
        self.label_text = label_text
        self.mset_label = None

    def __create_mset_elements(self, parent_window):
        if self.label_text:
            self.mset_label = mset.UILabel(self.label_text)
            parent_window.addElement(self.mset_label)
            parent_window.addReturn()

        for button in self.buttons:
            button.add_to_window(parent_window)

        parent_window.addReturn()

        if self.mset_label:
            self.mset_elements.append(self.mset_label)

    def add_button(self, button: ActionButton):
        if button:
            self.buttons.append(button)
            self.add_child(button)

    def create_button(self, text: str, on_click=None) -> ActionButton:
        button = ActionButton(text, on_click)
        self.add_button(button)
        return button