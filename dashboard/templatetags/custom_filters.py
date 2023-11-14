from django import template
import calendar

register = template.Library()


@register.filter
def get_by_student(queryset, student):
    try:
        return queryset.get(student=student)
    except queryset.model.DoesNotExist:
        return None


@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def month_name(month_number):
    return calendar.month_name[int(month_number)]
