from typing import Optional
from ..base.base_widget import BaseWidget
from ..base.signal_system import Signal

import mset


class LineEdit(BaseWidget):
    def __init__(self, text: str = "", placeholder_text: str = "", **kwargs):
        super().__init__(**kwargs)
        self.__placeholder_text = placeholder_text
        self.__text = text
        self.mset_field: Optional[object] = None

    def __create_mset_elements(self, parent_window):
        self.mset_field = mset.UITextField()
        self.mset_field.text = self.__text
        self.mset_field.onChange = self.__on_text_changed

        parent_window.addElement(self.mset_field)
        parent_window.addReturn()

        self.mset_elements.append(self.mset_field)

    def __init_signals(self):
        super().__init_signals()
        self.textChanged = Signal()

    def __on_text_changed(self):
        if self.mset_field and hasattr(self.mset_field, 'text'):
            old_text = self.__text
            self.__text = self.mset_field.text
            if old_text != self.__text:
                self.textChanged.emit(self.__text)

    def clear(self):
        self.text = ""

    def get_value(self) -> str:
        return self.text

    @property
    def placeholder_text(self) -> str:
        return self.__placeholder_text
        
    @placeholder_text.setter
    def placeholder_text(self, value: str):
        self.__placeholder_text = value

    def select_all(self):
        if self.mset_field and hasattr(self.mset_field, 'selectAll'):
            self.mset_field.selectAll()

    def set_value(self, value: str):
        self.text = str(value)

    @property
    def text(self) -> str:
        return self.__text
        
    @text.setter
    def text(self, value: str):
        self.__text = value
        if self.mset_field and hasattr(self.mset_field, 'text'):
            self.mset_field.text = value
