from django.contrib import admin

from bookings.models import Service, Review, Appointment


# class ProductAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Product._meta.fields if field.name != "id"]
#     list_editable = ['price', ]
#     list_filter = ['price', 'category']
#     actions = ['discount']
#     search_fields = [
#         'name',
#     ]
#
#     @admin.action(description='Set 10%% off discount')
#     def discount(self, request, queryset):
#         updated = queryset.update(price=F('price') * 0.9)
#         self.message_user(request, ngettext(
#             '%d product was successfully discounted by 10%%',
#             '%d products were successfully discounted by 10%%',
#             updated,
#         ) % updated, messages.SUCCESS)
#
#
# admin.site.register(Product, ProductAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Service._meta.fields if field.name != "id"]
    search_fields = [
        'name',
    ]


admin.site.register(Service, ServiceAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Appointment._meta.fields if field.name != "id"]


admin.site.register(Appointment, AppointmentAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Review._meta.fields if field.name != "id"]
    search_fields = [
        'name',
    ]


admin.site.register(Review, ReviewAdmin)
