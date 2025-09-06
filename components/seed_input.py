import random
from typing import Optional

import mset
from base.base_widget import BaseWidget
from base.signal_system import Signal


class SeedInput(BaseWidget):
    def __init__(self, label_text: str = "Random Seed:", help_text: str = "(0 for random)", **kwargs):
        super().__init__(**kwargs)
        self.help_text = help_text
        self.label_text = label_text
        self.mset_button: Optional[object] = None
        self.mset_field: Optional[object] = None
        self.mset_help_label: Optional[object] = None
        self.mset_label: Optional[object] = None
        self.valueChanged = Signal()

    def _create_mset_elements(self, parent_window):
        self.mset_label = mset.UILabel(self.label_text)
        parent_window.addElement(self.mset_label)
        parent_window.addReturn()

        if self.help_text:
            self.mset_help_label = mset.UILabel(self.help_text)
            parent_window.addElement(self.mset_help_label)
            parent_window.addReturn()

        self.mset_field = mset.UITextFieldInt()
        self.mset_field.value = 0
        parent_window.addElement(self.mset_field)

        self.mset_button = mset.UIButton("Random")
        self.mset_button.onClick = self.__on_random_click
        parent_window.addElement(self.mset_button)
        parent_window.addReturn()

        elements = [self.mset_label, self.mset_field, self.mset_button]
        if self.mset_help_label:
            elements.append(self.mset_help_label)
        self.mset_elements.extend(elements)

    def __on_random_click(self):
        self.set_random_seed()

    def get_value(self) -> Optional[int]:
        if self.mset_field and hasattr(self.mset_field, 'value'):
            value = self.mset_field.value
            return value if value != 0 else None
        return None

    def set_random_seed(self):
        random_value = random.randint(1, 999999)
        self.set_value(random_value)

    def set_value(self, value: int):
        if self.mset_field and hasattr(self.mset_field, 'value'):
            old_value = self.mset_field.value
            self.mset_field.value = value
            if old_value != value:
                self.valueChanged.emit(self.get_value())