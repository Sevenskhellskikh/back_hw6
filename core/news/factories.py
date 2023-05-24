import factory
from faker import Factory

from .models import News, Category, Origin

factory_ru = Factory.create('ru-Ru')


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Sequence(lambda n: "Категория #%s" % n)

    class Meta:
        model = Category


class OriginFactory(factory.django.DjangoModelFactory):
    title = factory_ru.word()

    class Meta:
        model = Origin


class NewsFactory(factory.django.DjangoModelFactory):
    title = factory_ru.first_name()
    content = factory_ru.text()
    origin = factory.SubFactory(OriginFactory)
    created_at = factory_ru.date()

    class Meta:
        model = News

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.categories.set(*extracted)
        print(self.categories)
