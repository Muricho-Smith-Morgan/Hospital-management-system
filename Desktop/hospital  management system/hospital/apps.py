from django.apps import AppConfig


class HospitalConfig(AppConfig):
    name = 'hospital'

    def ready(self):
        import hospital.signals