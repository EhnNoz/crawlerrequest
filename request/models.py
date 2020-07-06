from django.db import models
from django.utils.translation import ugettext_lazy as _


class Platform(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=200, blank=False, null=False, unique=True)
    active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        verbose_name = _('Platform')
        verbose_name_plural = _('Platforms')

    def __str__(self):
        return self.name


class Config(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=200, blank=False, null=False, unique=True)
    platforms = models.ManyToManyField(Platform, verbose_name='Platforms', blank=True)
    reousrces = models.ManyToManyField('Resource', verbose_name='Resources', blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is None and Config.objects.count() == 1:
            raise Exception(_('Maximum allowed Conf object is 1.'))

        return super(Config, self).save(force_insert=False, force_update=False, using=None,
                                 update_fields=None)


class Resource(models.Model):
    platform = models.ForeignKey(Platform, verbose_name=_('Platform'), on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name=_('Name'), max_length=200, blank=False, null=False, unique=True)
    active = models.BooleanField(verbose_name=_('Active'), default=True)

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')

    def __str__(self):
        return self.name


class Manifest(models.Model):
    keywords = models.CharField(verbose_name=_('KeyWord'), max_length=10000, blank=False)
    resources = models.ManyToManyField(Resource, verbose_name='Resources')
    active = models.BooleanField(verbose_name='Active', default=True)

    class Meta:
        verbose_name = _('Manifest')
        verbose_name_plural = _('Manifests')

    def __str__(self):
        return self.keywords

    def total_crawled_records(self):
        # @todo: must implement
        return 100

    def total_delivered_records(self):
        # @todo: must implement
        return 50
