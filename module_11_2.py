from pprint import pprint
import inspect


def introspection_info(inspected_object):
    #- Тип объекта.
    object_type = type(inspected_object).__name__
    #- Атрибуты объекта.
    object_attributes = [attr for attr in dir(inspected_object) if not callable(getattr(inspected_object, attr))]
    #- Методы объекта.
    object_methods = [method for method in dir(inspected_object) if callable(getattr(inspected_object, method))]
    #- Модуль, ккоторому объект принадлежит.
    object_module = inspected_object.__module__
    #- Другие интересные свойства объекта, учитывая его тип(по желанию).
    object_properties = id(inspected_object)
    some_inspected_object_info = {"Тип": object_type, "Атрибуты": object_attributes, "Методы": object_methods,
                                  "Модули": object_module, "Разное": object_properties}
    return some_inspected_object_info


class Bicycle:
    def __init__(self, color,frame_material, wheel_material,frame_size ,wheel_size ,brakes_type,field = "road"):
        self.field = field
        self.system = self.system_gears()
        self.brakes_type = brakes_type
        self.wheel_size = wheel_size
        self.frame_size = frame_size
        self.wheel_material = wheel_material
        self.frame_material = frame_material
        self.color = color
        self.price = None

    def system_gears(self):
        if self.field == "road":
            self.system = 42
        if self.field == "mountain":
            self.system = 30
        else:
            self.system = 36
        return self.system

test_bike = Bicycle("natural","alu","alu","M",29,"h-disc")
print(test_bike.wheel_size)

pprint(introspection_info(test_bike))
