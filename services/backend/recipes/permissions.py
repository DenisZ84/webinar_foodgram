
import logging
from rest_framework.permissions import SAFE_METHODS, BasePermission

TYPES_MISTAKES = {'Recipe': 'рецепт'}

logger = logging.getLogger(__name__)


class IsAuthorOrReadOnly(BasePermission):
    """Разрешитель для автора или только чтение"""
    message = 'Изменять {} может только автор!'

    def has_permission(self, request, view):
        logger.debug('has_permission')
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        logger.debug('has_object_permission')
        self.message = self.message.format(TYPES_MISTAKES[type(obj).__name__])
        return (request.method in SAFE_METHODS
                or obj.author == request.user)