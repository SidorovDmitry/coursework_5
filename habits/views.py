from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habits
from habits.permission import ListHabits, Owner
from habits.serializers import HabitsSerializer


class HabitsViewSet(ModelViewSet):
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()

    def get_serializer_context(self):
        """Добавляем request в контекст сериализатора"""
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        """
        Метод создание привычки - владелец теперь назначается автоматически в сериализаторе
        """
        serializer.save()

    def get_permissions(self):
        """
        Метод предоставления прав доступа.
        """

        if self.action == "list":
            permission_classes = [ListHabits]
        elif self.action in (
            "create",
            "retrieve",
            "update",
            "partial_update",
            "destroy",
        ):
            permission_classes = [Owner]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """
        Метод возврата списка привычек по критериям.
        """

        if self.request.user.is_superuser:
            return Habits.objects.all()

        elif self.request.user.is_authenticated:
            return Habits.objects.filter(owner=self.request.user) | Habits.objects.filter(is_public=True)

        else:
            return Habits.objects.none()