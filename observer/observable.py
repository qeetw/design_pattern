from abc import ABCMeta, abstractmethod
from observer import Observer

class Observable(metaclass=ABCMeta):
    observers = []
    changed = False
    
    def add_observer(self, observer):
        if isinstance(observer, Observer):
            print('Add', observer, ' to observer list')
            self.observers.append(observer)

    def delete_observer(self, observer):
        print('Remove', observer, ' from observer list')
        self.observers.remove(observer)

    def notify_observers(self):
        if (self.changed):
            for observer in self.observers:
                print('To nofity observer:', observer)
                observer.update(self)
            self.changed = False

    def set_changed(self):
        self.changed = True