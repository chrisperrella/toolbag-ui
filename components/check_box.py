from typing import Optional

import mset
from base.base_widget import BaseWidget
from base.signal_system import Signal


class CheckBox(BaseWidget):
    def __init__(self, text: str = "", checked: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.__checked = checked
        self.__text = text
        self.mset_checkbox: Optional[object] = None
        self.mset_label: Optional[object] = None
        self.stateChanged = Signal()

    def _create_mset_elements(self, parent_window):
        self.mset_checkbox = mset.UICheckBox()
        
        if self.__text:
            self.mset_label = mset.UILabel(self.__text)
            parent_window.addElement(self.mset_checkbox)
            parent_window.addElement(self.mset_label)
        else:
            parent_window.addElement(self.mset_checkbox)
            
        parent_window.addReturn()

        elements = [self.mset_checkbox]
        if self.mset_label:
            elements.append(self.mset_label)
        self.mset_elements.extend(elements)

    @property
    def checked(self) -> bool:
        return self.__checked
        
    @checked.setter
    def checked(self, value: bool):
        self.__checked = value

    def get_value(self) -> bool:
        return self.checked

    def set_value(self, value: bool):
        self.checked = value

    @property
    def text(self) -> str:
        return self.__text
        
    @text.setter
    def text(self, value: str):
        self.__text = value
        if self.mset_label and hasattr(self.mset_label, 'text'):
            self.mset_label.text = value
