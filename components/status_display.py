from typing import Optional

import mset
from base.base_widget import BaseWidget


class StatusDisplay(BaseWidget):
    def __init__(self, label_text: str = "Status:", initial_status: str = "Ready", **kwargs):
        super().__init__(**kwargs)
        self.initial_status = initial_status
        self.label_text = label_text
        self.mset_label: Optional[object] = None
        self.mset_status_label: Optional[object] = None

    def _create_mset_elements(self, parent_window):
        if self.label_text:
            self.mset_label = mset.UILabel(self.label_text)
            parent_window.addElement(self.mset_label)

        self.mset_status_label = mset.UILabel(self.initial_status)
        parent_window.addElement(self.mset_status_label)
        parent_window.addReturn()

        elements = [self.mset_status_label]
        if self.mset_label:
            elements.append(self.mset_label)
        self.mset_elements.extend(elements)

    def get_value(self) -> str:
        if self.mset_status_label and hasattr(self.mset_status_label, 'text'):
            return self.mset_status_label.text
        return self.initial_status

    def set_status(self, status: str):
        self.set_value(status)

    def set_value(self, status: str):
        if self.mset_status_label and hasattr(self.mset_status_label, 'text'):
            self.mset_status_label.text = status