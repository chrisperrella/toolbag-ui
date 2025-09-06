from typing import Callable, Dict, Optional

import mset
from base.base_widget import BaseWidget


class AxisButtonGroup(BaseWidget):
    def __init__(self, label_text: str, **kwargs):
        super().__init__(**kwargs)
        self.__label_text = label_text
        self.__on_axis_click: Optional[Callable[[int], None]] = None
        self.mset_buttons: Dict[str, object] = {}
        self.mset_label: Optional[object] = None

    def _create_mset_elements(self, parent_window):
        self.mset_label = mset.UILabel(self.__label_text)
        parent_window.addElement(self.mset_label)
        parent_window.addReturn()

        for axis, index in [("X", 0), ("Y", 1), ("Z", 2)]:
            button = mset.UIButton()
            button.text = axis
            button.onClick = lambda idx=index: self.__on_button_click(idx)
            self.mset_buttons[axis] = button
            parent_window.addElement(button)

        parent_window.addReturn()

        self.mset_elements.append(self.mset_label)
        self.mset_elements.extend(self.mset_buttons.values())

    def __on_button_click(self, axis_index: int):
        if self.__on_axis_click:
            self.__on_axis_click(axis_index)

    @property
    def on_axis_click(self) -> Optional[Callable[[int], None]]:
        return self.__on_axis_click
        
    @on_axis_click.setter
    def on_axis_click(self, callback: Callable[[int], None]):
        self.__on_axis_click = callback