from typing import Optional
from ..base.base_widget import BaseWidget
from ..base.signal_system import Signal

import mset


class CheckBox(BaseWidget):
    def __init__(self, text: str = "", checked: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.__checked = checked
        self.__text = text
        self.mset_checkbox: Optional[object] = None

    def __create_mset_elements(self, parent_window):
        self.mset_checkbox = mset.UICheckBox()
        self.mset_checkbox.text = self.__text
        self.mset_checkbox.checked = self.__checked
        self.mset_checkbox.onChange = self.__on_state_changed

        parent_window.addElement(self.mset_checkbox)
        parent_window.addReturn()

        self.mset_elements.append(self.mset_checkbox)

    def __init_signals(self):
        super().__init_signals()
        self.stateChanged = Signal()

    def __on_state_changed(self):
        if self.mset_checkbox and hasattr(self.mset_checkbox, 'checked'):
            self.__checked = self.mset_checkbox.checked
            self.stateChanged.emit(self.__checked)

    @property
    def checked(self) -> bool:
        return self.__checked
        
    @checked.setter
    def checked(self, value: bool):
        self.__checked = value
        if self.mset_checkbox and hasattr(self.mset_checkbox, 'checked'):
            self.mset_checkbox.checked = value

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
        if self.mset_checkbox and hasattr(self.mset_checkbox, 'text'):
            self.mset_checkbox.text = value
