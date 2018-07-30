from django.contrib import admin

from tests.app1.models import App1Model1, App1Model2


@admin.register(App1Model1)
class App1Model1Admin(admin.ModelAdmin):
    pass


@admin.register(App1Model2)
class App1Model2Admin(admin.ModelAdmin):
    pass
