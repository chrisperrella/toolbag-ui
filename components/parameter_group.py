from typing import Optional
from ..base.container_widget import ContainerWidget

import mset


class ParameterGroup(ContainerWidget):
    def __init__(self, title: str, expanded: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.__expanded = expanded
        self.__title = title
        self.mset_drawer: Optional[object] = None
        self.mset_window: Optional[object] = None

    def __create_mset_elements(self, parent_window):
        self.mset_drawer = mset.UIDrawer(name=self.__title)
        self.mset_window = mset.UIWindow(name="")
        self.mset_drawer.containedControl = self.mset_window
        self.mset_drawer.open = self.__expanded

        for widget in self.child_widgets:
            widget.add_to_window(self.mset_window)

        parent_window.addElement(self.mset_drawer)
        parent_window.addReturn()

        self.mset_elements.extend([self.mset_drawer, self.mset_window])

    def add_parameter(self, widget):
        self.add_child(widget)
        if self.mset_window:
            widget.add_to_window(self.mset_window)

    @property
    def expanded(self) -> bool:
        return self.__expanded
        
    @expanded.setter
    def expanded(self, value: bool):
        self.__expanded = value
        if self.mset_drawer and hasattr(self.mset_drawer, 'open'):
            self.mset_drawer.open = value