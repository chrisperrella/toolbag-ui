from typing import List
from ..base.container_widget import ContainerWidget

import mset


class HBoxLayout(ContainerWidget):
    def __init__(self, spacing: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.__spacing = spacing
        self.__widgets: List[object] = []

    def __create_mset_elements(self, parent_window):
        for i, widget in enumerate(self.__widgets):
            widget.add_to_window(parent_window)
            
            if i < len(self.__widgets) - 1 and self.__spacing > 0:
                for _ in range(self.__spacing):
                    parent_window.addElement(mset.UILabel(""))

        if self.__widgets:
            parent_window.addReturn()

    def add_stretch(self):
        pass

    def add_widget(self, widget):
        if widget and widget not in self.__widgets:
            self.__widgets.append(widget)
            self.add_child(widget)

    def clear(self):
        self.__widgets.clear()
        self.clear_children()

    @property
    def count(self) -> int:
        return len(self.__widgets)

    def insert_widget(self, index: int, widget):
        if widget and 0 <= index <= len(self.__widgets):
            self.__widgets.insert(index, widget)
            self.add_child(widget)

    def remove_widget(self, widget):
        if widget in self.__widgets:
            self.__widgets.remove(widget)
            self.remove_child(widget)

    @property
    def spacing(self) -> int:
        return self.__spacing
        
    @spacing.setter
    def spacing(self, value: int):
        self.__spacing = max(0, value)
