from django.contrib import admin
from django.apps import apps

# Registrar todos os modelos automaticamente
app_models = apps.get_app_config('contato').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
