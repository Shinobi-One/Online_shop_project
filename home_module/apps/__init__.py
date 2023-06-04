import pkgutil
from shop_project import settings

for _, name ,_ in pkgutil.iter_modules(['apps']):
    if  f"apps.{name}" not in settings.INSTALLED_APPS :
        settings.INSTALLED_APPS.append(f"apps.{name}")