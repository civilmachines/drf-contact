from rest_framework import serializers


class ShowContactDetailSerializer(serializers.ModelSerializer):
    """
    ShowContactDetailSerializer is a model serializer that includes the details of a contact.
    Returns
    -------
        returns a dictionary containing::
            'id' : int
            'name' : str
            'email' : str
            'mobile' : str
    """

    class Meta:
        from .models import ContactDetail

        model = ContactDetail
        fields = ('id', 'name', 'email', 'mobile')


class AddContactDetailSerializer(serializers.ModelSerializer):
    """
    AddContactDetailSerializer is a model serializer that includes the fields required for adding a new contact.
    Returns
    -------
        returns a dictionary containing::
            'name' : str
            'email' : str
            'mobile' : str
    """

    class Meta:
        from .models import ContactDetail

        model = ContactDetail
        fields = ('name', 'email', 'mobile')
