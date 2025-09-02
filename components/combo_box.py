from typing import List, Optional
from ..base.base_widget import BaseWidget
from ..base.signal_system import Signal

import mset


class ComboBox(BaseWidget):
    def __init__(self, items: List[str] = None, current_index: int = 0, label_text: str = "", **kwargs):
        super().__init__(**kwargs)
        self.__current_index = current_index
        self.__items = items or []
        self.__label_text = label_text
        self.mset_combo: Optional[object] = None

    def __create_mset_elements(self, parent_window):
        self.mset_combo = mset.UIListBox(self.__label_text)
        
        for item in self.__items:
            self.mset_combo.addItem(item)
            
        if self.__items and 0 <= self.__current_index < len(self.__items):
            self.mset_combo.selectedIndex = self.__current_index
            
        self.mset_combo.onChange = self.__on_selection_changed

        parent_window.addElement(self.mset_combo)
        parent_window.addReturn()

        self.mset_elements.append(self.mset_combo)

    def __init_signals(self):
        super().__init_signals()
        self.currentIndexChanged = Signal()
        self.currentTextChanged = Signal()

    def __on_selection_changed(self):
        if self.mset_combo and hasattr(self.mset_combo, 'selectedIndex'):
            old_index = self.__current_index
            self.__current_index = self.mset_combo.selectedIndex
            if old_index != self.__current_index:
                self.currentIndexChanged.emit(self.__current_index)
                if 0 <= self.__current_index < len(self.__items):
                    self.currentTextChanged.emit(self.__items[self.__current_index])

    def add_item(self, text: str):
        self.__items.append(text)
        if self.mset_combo:
            self.mset_combo.addItem(text)

    def clear(self):
        self.__items.clear()
        self.__current_index = 0
        if self.mset_combo:
            while self.mset_combo.itemCount > 0:
                self.mset_combo.removeItem(0)

    @property
    def count(self) -> int:
        return len(self.__items)

    @property
    def current_index(self) -> int:
        return self.__current_index
        
    @current_index.setter
    def current_index(self, value: int):
        if 0 <= value < len(self.__items):
            self.__current_index = value
            if self.mset_combo and hasattr(self.mset_combo, 'selectedIndex'):
                self.mset_combo.selectedIndex = value

    @property
    def current_text(self) -> str:
        if 0 <= self.__current_index < len(self.__items):
            return self.__items[self.__current_index]
        return ""

    def get_value(self) -> str:
        return self.current_text

    @property
    def items(self) -> List[str]:
        return self.__items.copy()

    def set_value(self, text: str):
        try:
            index = self.__items.index(text)
            self.current_index = index
        except ValueError:
            pass
