from django import template

from core.models import UserAccount

register = template.Library()


@register.filter
def can_manage_users(user):
    if not getattr(user, 'is_authenticated', False):
        return False
    if user.is_superuser:
        return True
    role = getattr(getattr(user, 'account', None), 'role', None)
    return role == UserAccount.ROLE_ADMINISTRATOR
