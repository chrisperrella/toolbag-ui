from typing import Any, List
import mset
from .signal_system import Signal, SignalMixin


class BaseWidget(SignalMixin):
    def __init__(self, enabled: bool = True, tooltip: str = "", visible: bool = True, **kwargs):
        super().__init__(**kwargs)
        self.__enabled = enabled
        self.__tooltip = tooltip
        self.__visible = visible
        self.mset_elements: List[Any] = []

    def __create_mset_elements(self, parent_window):
        pass

    def __destroy_mset_elements(self):
        for element in self.mset_elements:
            if hasattr(element, 'destroy'):
                element.destroy()
        self.mset_elements.clear()

    def __init_signals(self):
        self.destroyed = Signal()
        self.enabledChanged = Signal()
        self.visibilityChanged = Signal()

    def __update_enabled_state(self):
        for element in self.mset_elements:
            if hasattr(element, 'enabled'):
                element.enabled = self.enabled

    def __update_visible_state(self):
        for element in self.mset_elements:
            if hasattr(element, 'visible'):
                element.visible = self.visible

    def add_to_window(self, parent_window):
        if parent_window:
            self.__create_mset_elements(parent_window)

    def destroy(self):
        self.destroyed.emit()
        self.__destroy_mset_elements()

    @property
    def enabled(self) -> bool:
        return self.__enabled
        
    @enabled.setter  
    def enabled(self, value: bool):
        if self.__enabled != value:
            self.__enabled = value
            self.__update_enabled_state()
            self.enabledChanged.emit(value)

    def get_value(self) -> Any:
        return None

    def set_value(self, value: Any):
        pass

    @property
    def tooltip(self) -> str:
        return self.__tooltip
        
    @tooltip.setter
    def tooltip(self, value: str):
        self.__tooltip = value

    @property 
    def visible(self) -> bool:
        return self.__visible
        
    @visible.setter
    def visible(self, value: bool):
        if self.__visible != value:
            self.__visible = value
            self.__update_visible_state() 
            self.visibilityChanged.emit(value)