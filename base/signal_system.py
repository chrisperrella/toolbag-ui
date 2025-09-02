from typing import Any, Callable, List


class Signal:
    def __init__(self):
        self.__callbacks: List[Callable] = []
    
    def connect(self, callback: Callable):
        if callback and callback not in self.__callbacks:
            self.__callbacks.append(callback)
    
    def disconnect(self, callback: Callable = None):
        if callback:
            if callback in self.__callbacks:
                self.__callbacks.remove(callback)
        else:
            self.__callbacks.clear()
    
    def emit(self, *args, **kwargs):
        for callback in self.__callbacks:
            try:
                callback(*args, **kwargs)
            except Exception:
                pass


class SignalMixin:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__init_signals()
    
    def __init_signals(self):
        pass
