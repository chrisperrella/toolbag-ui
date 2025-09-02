from typing import Dict, List, Union
from ..base.container_widget import ContainerWidget
from ..base.signal_system import Signal
from .labeled_slider import LabeledSlider

import mset


class Vector3Input(ContainerWidget):
    def __init__(self, label_text: str, min_value: Union[int, float], max_value: Union[int, float],
                 default_value: Union[Union[int, float], List[Union[int, float]]], 
                 slider_type: str = "float", **kwargs):
        super().__init__(**kwargs)
        if isinstance(default_value, (list, tuple)):
            self.default_value = list(default_value)[:3]
            if len(self.default_value) < 3:
                self.default_value.extend([0] * (3 - len(self.default_value)))
        else:
            self.default_value = [default_value] * 3
            
        self.label_text = label_text
        self.max_value = max_value
        self.min_value = min_value
        self.mset_label = None
        self.slider_type = slider_type
        self.slider_widgets: Dict[str, LabeledSlider] = {}

    def __create_mset_elements(self, parent_window):
        if self.label_text:
            self.mset_label = mset.UILabel(self.label_text)
            parent_window.addElement(self.mset_label)
            parent_window.addReturn()

        for i, axis in enumerate(["X", "Y", "Z"]):
            slider = LabeledSlider(
                f"  {axis}:",
                self.min_value,
                self.max_value,
                self.default_value[i],
                self.slider_type
            )
            slider.valueChanged.connect(lambda v, ax=i: self.__on_component_change(ax, v))
            self.slider_widgets[axis] = slider
            self.add_child(slider)
            slider.add_to_window(parent_window)

        if self.mset_label:
            self.mset_elements.append(self.mset_label)

    def __init_signals(self):
        super().__init_signals()
        self.valueChanged = Signal()

    def __on_component_change(self, axis_index: int, value: Union[int, float]):
        self.valueChanged.emit(self.get_value())

    def get_value(self) -> List[Union[int, float]]:
        return [self.slider_widgets[axis].value for axis in ["X", "Y", "Z"]]

    def set_value(self, values: List[Union[int, float]]):
        if not isinstance(values, (list, tuple)) or len(values) < 3:
            return
            
        for i, axis in enumerate(["X", "Y", "Z"]):
            if i < len(values):
                self.slider_widgets[axis].value = values[i]