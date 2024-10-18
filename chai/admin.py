from django.contrib import admin
from .models import ChaiVariety, ChaiCertificate, ChaiReview, Store

# Register your models here.
# and see them in admin

# Customizing the Admin View

# for, review it needs to have whose review, 
# so we have inline here
class ChaiReviewInLine(admin.TabularInline):
  model = ChaiReview
  extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'date_added')
  inlines = [ChaiReviewInLine]


class StoreAdmin(admin.ModelAdmin):
  list_display = ('name', 'location')
  filter_horizontal = ('chai_varieties', )


class ChaiCertificateAdmin(admin.ModelAdmin):
  list_display = ('chai', 'certificate_number')

# we till here, wrote customized classes
# now, we have to specify, which model we brought,
# and which customized class we applied


admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
