from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICE = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
  ]

  RATING_CHOICE = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
  description = models.TextField(default='')
  price = models.DecimalField(default=0.0, max_digits=4, decimal_places=2)

  def __str__(self) -> str:
    return f'Chai Variety: {self.name}'
  
# One to Many model
class ChaiReview(models.Model):
  chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField(validators=[
    MinValueValidator(1),
    MaxValueValidator(5)
  ], 
    default=1
  )
  comment = models.TextField()
  date_added = models.DateField(default=timezone.now)

  def __str__(self) -> str:
    return f'{self.user.username} review for {self.chai.name}'


# Many to Many Model
class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

  def __str__(self):
    return self.name
  

# One to One Model
class ChaiCertificate(models.Model):
  chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
  certificate_number = models.CharField(max_length=100)
  issue_date = models.DateTimeField(default=timezone.now)
  valid_until = models.DateField()

  def __str__(self):
    return f'Certificate for {self.chai.name}'
  
