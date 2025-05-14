from django.contrib import admin
from .models import Profile, About, Certification, Education, Skill, Project
from adminsortable2.admin import SortableAdminMixin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not Profile.objects.exists()
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not About.objects.exists()
@admin.register(Certification)
class CertificationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'issuer', 'year']
    search_fields = ['title', 'issuer']
@admin.register(Education)
class EducationAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['institution', 'title', 'year']
    search_fields = ['institution', 'title']
@admin.register(Project)
class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
@admin.register(Skill)
class SkillAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'icon', 'color']
    search_fields = ['name', 'icon']
