from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


User = get_user_model()


class Sport(models.Model):
    """Sport model."""
    sport_name = models.CharField(max_length=150)
    sport_slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.sport_name

    class Meta:
        default_related_name = 'sports'


class Covering(models.Model):
    """Covering model."""
    covering_name = models.CharField(max_length=150)
    covering_slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.covering_name

    class Meta:
        default_related_name = 'coverings'


class Playground(models.Model):
    """Playground model."""
    TYPE_PLAYGROUND_CHOICES = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )

    playground_name = models.CharField(
        max_length=150,
    )
    playground_type = models.CharField(
        max_length=10,
        choices=TYPE_PLAYGROUND_CHOICES,
    )
    size = models.CharField(
        max_length=50,
    )
    playground_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0,
        blank=False,
    )
    address = models.CharField(
        max_length=150,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    description = models.TextField(blank=True)

    sports = models.ManyToManyField(
        Sport,
    )
    covering = models.ForeignKey(
        Covering,
        on_delete=models.SET_DEFAULT,
        default=1,
    )
    shower = models.BooleanField(default=False)
    changing_rooms = models.BooleanField(default=False)
    lighting = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    stands = models.PositiveIntegerField(default=0)

    playground_slug = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.playground_name

    def get_absolute_url(self):
        return reverse("playground_detail", kwargs={"slug": self.playground_slug})

    class Meta:
        default_related_name = 'playgrounds'


class ImagePlayground(models.Model):
    """Images playground model."""
    description_image = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='playground_image/')
    main_image = models.BooleanField(default=False)
    playground = models.ForeignKey(Playground, on_delete=models.CASCADE)

    def __str__(self):
        return self.description_image

    class Meta:
        default_related_name = 'playground_images'


class Inventory(models.Model):
    """Inventory model."""
    inventory_name = models.CharField(max_length=150)
    inventory_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    playground = models.ForeignKey(Playground, on_delete=models.CASCADE)

    def __str__(self):
        return self.inventory_name

    class Meta:
        default_related_name = 'inventories'
