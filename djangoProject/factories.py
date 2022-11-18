import factory.django
from djangoProject.models import Categories, Products


class CategoriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categories

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: "Group #%s" % n)


class ProductsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Products
    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: "Product #%s" % n)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for category in extracted:
                self.categories.add(category)
