import mset
from base.container_widget import ContainerWidget


class SectionLayout(ContainerWidget):
    def __init__(self, spacing: int = 1, **kwargs):
        super().__init__(**kwargs)
        self.spacing = spacing

    def _create_mset_elements(self, parent_window):
        for i, widget in enumerate(self.child_widgets):
            widget.add_to_window(parent_window)
            
            if i < len(self.child_widgets) - 1:
                for _ in range(self.spacing):
                    parent_window.addReturn()

    def add_section(self, widget):
        self.add_child(widget)