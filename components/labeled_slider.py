from typing import Optional, Union
from ..base.base_widget import BaseWidget
from ..base.signal_system import Signal
from ..base.validation_helpers import ValidationHelpers

import mset


class LabeledSlider(BaseWidget):
    def __init__(self, label_text: str, min_value: Union[int, float], max_value: Union[int, float], 
                 default_value: Union[int, float], slider_type: str = "float", **kwargs):
        super().__init__(**kwargs)
        self.__default_value = default_value
        self.__label_text = label_text
        self.__max_value = max_value
        self.__min_value = min_value
        self.__slider_type = slider_type
        self.mset_label: Optional[object] = None
        self.mset_slider: Optional[object] = None

    def __create_mset_elements(self, parent_window):
        self.mset_label = mset.UILabel(self.label_text)
        parent_window.addElement(self.mset_label)
        parent_window.addReturn()

        if self.__slider_type == "int":
            self.mset_slider = mset.UISliderInt(min=int(self.__min_value), max=int(self.__max_value))
        else:
            self.mset_slider = mset.UISliderFloat(min=float(self.__min_value), max=float(self.__max_value))

        self.mset_slider.value = self.__default_value
        self.mset_slider.onChange = self.__on_slider_change
        parent_window.addElement(self.mset_slider)
        parent_window.addReturn()

        self.mset_elements.extend([self.mset_label, self.mset_slider])

    def __init_signals(self):
        super().__init_signals()
        self.valueChanged = Signal()

    def __on_slider_change(self):
        if self.mset_slider and hasattr(self.mset_slider, 'value'):
            self.valueChanged.emit(self.mset_slider.value)

    @property
    def label_text(self) -> str:
        return self.__label_text

    @property
    def maximum(self) -> Union[int, float]:
        return self.__max_value
        
    @property 
    def minimum(self) -> Union[int, float]:
        return self.__min_value

    @property
    def value(self) -> Union[int, float]:
        if self.mset_slider and hasattr(self.mset_slider, 'value'):
            return self.mset_slider.value
        return self.__default_value
        
    @value.setter
    def value(self, new_value: Union[int, float]):
        if self.__slider_type == "int":
            new_value = ValidationHelpers.clamp_int(int(new_value), int(self.__min_value), int(self.__max_value))
        else:
            new_value = ValidationHelpers.clamp_float(float(new_value), float(self.__min_value), float(self.__max_value))
            
        if self.mset_slider and hasattr(self.mset_slider, 'value'):
            old_value = self.mset_slider.value
            self.mset_slider.value = new_value
            if old_value != new_value:
                self.valueChanged.emit(new_value)