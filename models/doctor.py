#!usr/bin/pyhton3
""" A class Doctor that inherits from Staff """


from models.staff import Staff


class Doctor(Staff, Permission):
    """ Simple Doctor class model """
    job_title = "Doctor"

    def __init__(self, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
            # if it's a new instantiation, generate a staff_id
            super().set_staff_id()
