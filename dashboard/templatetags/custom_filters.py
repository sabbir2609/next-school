from django import template

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
