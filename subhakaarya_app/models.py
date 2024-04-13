from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from account.models import Vendor


class Service(models.Model):
    class Meta:
        ordering = ['rank']

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to='uploads/services/', blank=True)
    rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        is_created = self.pk is None

        # set rank to max_rank + 1 if not given
        if not self.rank:
            max_rank = Service.objects.all().aggregate(models.Max('rank')).get('rank__max')
            self.rank = 1 if not max_rank else max_rank + 1

        super(Service, self).save(*args, **kwargs)


class Plan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/plans/', blank=True)

    def __str__(self):
        return self.title


class Vendorlist(models.Model):
    title = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/vendorlist/', blank=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    owner = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    number_of_people = models.IntegerField()
    event_date = models.DateField()
    event_location = models.TextField()
    environment = models.TextField()
    plan = models.ForeignKey(
        Plan, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.owner + "-" + self.phone + "-" + self.event_location


class VendorService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.FloatField()
    locations = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(
        upload_to='uploads/vendor-services/', blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)


@receiver(pre_save, sender=Service)
def update_rank(sender, instance, **kwargs):
    # update ranking if provided explicitly
    if instance.rank and instance.pk is None:
        services = Service.objects.filter(rank__gte=instance.rank)
        for service in services:
            service.rank = service.rank + 1
            service.save()
