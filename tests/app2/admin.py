from django.contrib import admin

from tests.app2.models import App2Model1, App2Model2


@admin.register(App2Model1)
class App2Model1Admin(admin.ModelAdmin):
    pass


@admin.register(App2Model2)
class App2Model2Admin(admin.ModelAdmin):
    pass
