import mset

from components.action_button import ActionButton
from components.axis_button_group import AxisButtonGroup
from components.check_box import CheckBox
from components.combo_box import ComboBox
from components.labeled_slider import LabeledSlider
from components.line_edit import LineEdit
from components.parameter_group import ParameterGroup
from components.seed_input import SeedInput
from components.status_display import StatusDisplay
from components.vector3_input import Vector3Input
from layouts.grid_layout import GridLayout
from layouts.hbox_layout import HBoxLayout
from layouts.vbox_layout import VBoxLayout


class WidgetShowcase:
    def __init__(self):
        self.main_window = mset.UIWindow("UI Widget Showcase")
        self.main_window.width = 350
        self.status_display = None
        self.widgets = []
        
        self.__create_showcase_ui()
        self.main_window.visible = True

    def __create_showcase_ui(self):
        basic_group = ParameterGroup("Basic Widgets", expanded=True)
        
        gravity_slider = LabeledSlider("Gravity", 0.0, 20.0, 9.81)
        gravity_slider.valueChanged.connect(self.__on_gravity_changed)
        basic_group.add_parameter(gravity_slider)
        
        count_slider = LabeledSlider("Count", 1, 100, 50, "int")
        count_slider.valueChanged.connect(self.__on_count_changed)
        basic_group.add_parameter(count_slider)
        
        seed_input = SeedInput()
        seed_input.valueChanged.connect(self.__on_seed_changed)
        basic_group.add_parameter(seed_input)
        
        basic_group.add_to_window(self.main_window)
        self.widgets.append(basic_group)
        
        input_group = ParameterGroup("Input Widgets")
        
        name_input = LineEdit("Enter name...", "Name placeholder")
        name_input.textChanged.connect(self.__on_name_changed)
        input_group.add_parameter(name_input)
        
        feature_toggle = CheckBox("Enable advanced features", False)
        feature_toggle.stateChanged.connect(self.__on_feature_toggled)
        input_group.add_parameter(feature_toggle)
        
        surface_combo = ComboBox(["Mesh Surface", "Procedural Plane", "Procedural Sphere", "Procedural Box"], 0, "Surface Type:")
        surface_combo.currentTextChanged.connect(self.__on_surface_changed)
        input_group.add_parameter(surface_combo)
        
        input_group.add_to_window(self.main_window)
        self.widgets.append(input_group)
        
        axis_group = ParameterGroup("Axis Operations")
        
        align_buttons = AxisButtonGroup("Align to Axis:")
        align_buttons.on_axis_click = self.__on_align_axis
        axis_group.add_parameter(align_buttons)
        
        position_input = Vector3Input("Position", -10.0, 10.0, [0.0, 0.0, 0.0])
        position_input.valueChanged.connect(self.__on_position_changed)
        axis_group.add_parameter(position_input)
        
        axis_group.add_to_window(self.main_window)
        self.widgets.append(axis_group)
        
        layout_group = ParameterGroup("Layout Demos")
        
        hbox_demo = self.__create_hbox_demo()
        layout_group.add_parameter(hbox_demo)
        
        vbox_demo = self.__create_vbox_demo()
        layout_group.add_parameter(vbox_demo)
        
        grid_demo = self.__create_grid_demo()
        layout_group.add_parameter(grid_demo)
        
        layout_group.add_to_window(self.main_window)
        self.widgets.append(layout_group)
        
        action_button = ActionButton("Test Action", self.__on_test_action)
        action_button.add_to_window(self.main_window)
        self.widgets.append(action_button)
        
        self.status_display = StatusDisplay("Status:", "Showcase ready")
        self.status_display.add_to_window(self.main_window)
        self.widgets.append(self.status_display)

    def __create_grid_demo(self):
        grid = GridLayout()
        
        grid.add_widget(ActionButton("A", lambda: self.__on_layout_click("Grid A")), 0, 0)
        grid.add_widget(ActionButton("B", lambda: self.__on_layout_click("Grid B")), 0, 1)
        grid.add_widget(ActionButton("C", lambda: self.__on_layout_click("Grid C")), 1, 0)
        grid.add_widget(ActionButton("D", lambda: self.__on_layout_click("Grid D")), 1, 1)
        
        return grid

    def __create_hbox_demo(self):
        hbox = HBoxLayout()
        
        hbox.add_widget(ActionButton("H1", lambda: self.__on_layout_click("HBox 1")))
        hbox.add_widget(ActionButton("H2", lambda: self.__on_layout_click("HBox 2")))
        hbox.add_widget(ActionButton("H3", lambda: self.__on_layout_click("HBox 3")))
        
        return hbox

    def __create_vbox_demo(self):
        vbox = VBoxLayout()
        
        vbox.add_widget(ActionButton("V1", lambda: self.__on_layout_click("VBox 1")))
        vbox.add_widget(ActionButton("V2", lambda: self.__on_layout_click("VBox 2")))
        vbox.add_widget(ActionButton("V3", lambda: self.__on_layout_click("VBox 3")))
        
        return vbox

    def __on_align_axis(self, axis_index):
        axis_names = ["X", "Y", "Z"]
        if self.status_display:
            self.status_display.set_status(f"Align to {axis_names[axis_index]} axis clicked")

    def __on_count_changed(self, value):
        if self.status_display:
            self.status_display.set_status(f"Count changed to: {value}")

    def __on_feature_toggled(self, checked):
        if self.status_display:
            state = "enabled" if checked else "disabled"
            self.status_display.set_status(f"Advanced features {state}")

    def __on_gravity_changed(self, value):
        if self.status_display:
            self.status_display.set_status(f"Gravity changed to: {value:.2f}")

    def __on_layout_click(self, button_name):
        if self.status_display:
            self.status_display.set_status(f"Layout demo clicked: {button_name}")

    def __on_name_changed(self, text):
        if self.status_display:
            self.status_display.set_status(f"Name changed to: '{text}'")

    def __on_position_changed(self, value):
        if self.status_display:
            self.status_display.set_status(f"Position: [{value[0]:.1f}, {value[1]:.1f}, {value[2]:.1f}]")

    def __on_seed_changed(self, value):
        if self.status_display:
            seed_text = str(value) if value is not None else "random"
            self.status_display.set_status(f"Seed changed to: {seed_text}")

    def __on_surface_changed(self, surface_type):
        if self.status_display:
            self.status_display.set_status(f"Surface type changed to: {surface_type}")

    def __on_test_action(self):
        if self.status_display:
            self.status_display.set_status("Test action executed!")


if __name__ == "__main__":
    WidgetShowcase()
