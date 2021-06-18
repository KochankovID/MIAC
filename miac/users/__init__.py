from enum import Enum


class AUTH_ROLE(Enum):
    ADMIN = 'admin'
    DOCTOR = 'doctor'
    PATIENTS = 'patients'

    def __str__(self):
        return self.value
