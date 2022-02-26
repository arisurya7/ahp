from django.contrib import admin
from .models import Responden, WeightLRFM, WeightRFM

# Register your models here.
@admin.register(Responden)
class RespondenAdmin(admin.ModelAdmin):
    list_display = ('id_responden', 'name', 'education', 'birth_date', 'gender', 'name_company', 'businness_field', 'position', 'experience')

@admin.register(WeightRFM)
class WeightRFMAdmin(admin.ModelAdmin):
    list_display = ('id','id_responden','w_recency', 'w_frequency', 'w_monetary', 'score_input')

@admin.register(WeightLRFM)
class WeightLRFMAdmin(admin.ModelAdmin):
    list_display = ('id','id_responden','w_length','w_recency', 'w_frequency', 'w_monetary', 'score_input')