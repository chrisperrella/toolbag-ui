from typing import Dict, List, Optional, Tuple

import mset
from base.container_widget import ContainerWidget


class GridLayout(ContainerWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__grid_items: Dict[Tuple[int, int], object] = {}
        self.__max_column = -1
        self.__max_row = -1

    def _create_mset_elements(self, parent_window):
        sorted_positions = sorted(self.__grid_items.keys())
        
        current_row = -1
        for row, col in sorted_positions:
            widget = self.__grid_items[(row, col)]
            
            if row != current_row:
                if current_row >= 0:
                    parent_window.addReturn()
                current_row = row
                
            widget.add_to_window(parent_window)

        if sorted_positions:
            parent_window.addReturn()

    def add_widget(self, widget, row: int, column: int):
        if widget and row >= 0 and column >= 0:
            position = (row, column)
            if position in self.__grid_items:
                old_widget = self.__grid_items[position]
                self.remove_child(old_widget)
                
            self.__grid_items[position] = widget
            self.add_child(widget)
            self.__max_row = max(self.__max_row, row)
            self.__max_column = max(self.__max_column, column)

    def clear_grid(self):
        self.__grid_items.clear()
        self.__max_column = -1
        self.__max_row = -1
        self.clear_children()

    @property
    def column_count(self) -> int:
        return self.__max_column + 1 if self.__max_column >= 0 else 0

    def get_widget_at(self, row: int, column: int) -> Optional[object]:
        return self.__grid_items.get((row, column))

    def remove_widget(self, widget):
        position_to_remove = None
        for position, stored_widget in self.__grid_items.items():
            if stored_widget == widget:
                position_to_remove = position
                break
                
        if position_to_remove:
            del self.__grid_items[position_to_remove]
            self.remove_child(widget)
            self.__update_max_dimensions()

    @property
    def row_count(self) -> int:
        return self.__max_row + 1 if self.__max_row >= 0 else 0

    def __update_max_dimensions(self):
        if not self.__grid_items:
            self.__max_row = -1
            self.__max_column = -1
            return
            
        positions = list(self.__grid_items.keys())
        self.__max_row = max(pos[0] for pos in positions)
        self.__max_column = max(pos[1] for pos in positions)
