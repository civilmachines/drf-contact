from rest_framework.generics import ListAPIView, CreateAPIView


class ShowContacts(ListAPIView):
    """
    This view is to show the details of a contact.
    """
    from .serializers import ShowContactDetailSerializer
    from rest_framework.filters import SearchFilter
    from .models import ContactDetail
    from drfaddons.serializer import IsOwnerFilterBackend
    from django_filters.rest_framework import DjangoFilterBackend
    from rest_framework.pagination import PageNumberPagination
    from rest_framework.permissions import IsAuthenticated
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser

    queryset = ContactDetail.objects.all()
    serializer_class = ShowContactDetailSerializer
    filter_backends = (IsOwnerFilterBackend, DjangoFilterBackend, SearchFilter)
    search_fields = ('^name',)
    pagination_class = PageNumberPagination
    page_size = 10
    permission_classes = (IsAuthenticated, )
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser, )


class AddContacts(CreateAPIView):
    """
    This view is to add new contacts.
    """
    from .serializers import AddContactDetailSerializer
    from rest_framework.permissions import IsAuthenticated
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser

    serializer_class = AddContactDetailSerializer
    permission_classes = (IsAuthenticated, )
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser, )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
