class InputError(Exception):
    def __init__(self, given_object, func_name, accepted_type):
        self.obj_type = type(given_object)
        self.func_name = func_name
        self.accepted_type = accepted_type

    def __str__(self):
        return f"{self.obj_type} was given. {self.func_name} accepts only {self.accepted_type} type."
