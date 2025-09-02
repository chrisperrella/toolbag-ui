from typing import Callable, Optional
from ..base.base_widget import BaseWidget

import mset


class ActionButton(BaseWidget):
    def __init__(self, text: str, on_click: Optional[Callable[[], None]] = None, 
                 frameless: bool = False, lit: bool = True, small: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.__frameless = frameless
        self.__lit = lit
        self.__on_click = on_click
        self.__small = small
        self.__text = text
        self.mset_button: Optional[object] = None

    def __create_mset_elements(self, parent_window):
        self.mset_button = mset.UIButton()
        self.mset_button.text = self.__text
        self.mset_button.frameless = self.__frameless
        self.mset_button.lit = self.__lit
        self.mset_button.small = self.__small
        
        if self.__on_click:
            self.mset_button.onClick = self.__on_click

        parent_window.addElement(self.mset_button)

        self.mset_elements.append(self.mset_button)

    @property
    def on_click(self) -> Optional[Callable[[], None]]:
        return self.__on_click
        
    @on_click.setter
    def on_click(self, callback: Callable[[], None]):
        self.__on_click = callback
        if self.mset_button and hasattr(self.mset_button, 'onClick'):
            self.mset_button.onClick = callback

    @property
    def text(self) -> str:
        return self.__text
        
    @text.setter
    def text(self, value: str):
        self.__text = value
        if self.mset_button and hasattr(self.mset_button, 'text'):
            self.mset_button.text = value