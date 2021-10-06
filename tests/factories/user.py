import factory

from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('safe_email')
    password = factory.PostGenerationMethodCall('set_password', 'test1pass')

    class Meta:
        model = User
