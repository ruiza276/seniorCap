from django.contrib import admin
from .models import Skill
from .models import Major
from .models import Class

from .models import user_skills
from .models import UserProfile
from .models import user_classes

from .models import Job
# Register your models here.


admin.site.register(Skill)

admin.site.register(Major)

admin.site.register(Class)

admin.site.register(user_skills)

admin.site.register(user_classes)

admin.site.register(UserProfile)

admin.site.register(Job)


