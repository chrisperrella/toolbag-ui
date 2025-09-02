from typing import Any, Optional, Tuple, Union


class ValidationHelpers:
    @staticmethod
    def clamp_float(value: float, min_value: float, max_value: float) -> float:
        return max(min_value, min(max_value, value))

    @staticmethod
    def clamp_int(value: int, min_value: int, max_value: int) -> int:
        return max(min_value, min(max_value, value))

    @staticmethod
    def is_valid_float(value: Any) -> bool:
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def is_valid_int(value: Any) -> bool:
        try:
            int(value)
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def normalize_float(value: Any, default: float = 0.0) -> float:
        if ValidationHelpers.is_valid_float(value):
            return float(value)
        return default

    @staticmethod
    def normalize_int(value: Any, default: int = 0) -> int:
        if ValidationHelpers.is_valid_int(value):
            return int(value)
        return default

    @staticmethod
    def validate_range(value: Union[int, float], min_value: Union[int, float], max_value: Union[int, float]) -> Tuple[bool, str]:
        if value < min_value:
            return False, f"Value {value} is below minimum {min_value}"
        if value > max_value:
            return False, f"Value {value} is above maximum {max_value}"
        return True, ""

    @staticmethod
    def validate_vector3(value: Any) -> Tuple[bool, str, Optional[list]]:
        if not isinstance(value, (list, tuple)):
            return False, "Vector3 must be a list or tuple", None
        
        if len(value) != 3:
            return False, "Vector3 must have exactly 3 components", None
            
        try:
            normalized = [float(v) for v in value]
            return True, "", normalized
        except (ValueError, TypeError):
            return False, "All Vector3 components must be numeric", None
