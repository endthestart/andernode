from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Distribution(models.Model):
    ARCH_CHOICES = (
        ('32', '32-bit'),
        ('64', '64-bit'),
    )
    name = models.CharField(
        _("name"),
        max_length=100,
    )
    kernel = models.CharField(
        _("kernel"),
        max_length=255,
        help_text=_("The kernel ")
    )
    arch = models.CharField(
        _("distribution architecture"),
        choices=ARCH_CHOICES,
        max_length=20,
        help_text=_("The architecture of the OS."),
    )


class VirtualMachine(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    label = models.CharField(
        _("label"),
        max_length=100,
    )
    notes = models.TextField(
        _("notes"),
    )
    created_on = models.DateTimeField(
        _("created on"),
    )
    modified_on = models.DateTimeField(
        _("modified on"),
    )
    distribution = models.ForeignKey(
        Distribution,
    )

class Disk(models.Model):
    FS_CHOICES = (
        ("ext3", _("ext3")),
        ("ext4", _("ext4")),
        ("swap", _("swap")),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    label = models.CharField(
        _("label"),
        max_length=100,
        help_text=_("The name of the disk image."),
    )
    size = models.IntegerField(
        _("size"),
        default=0,
        help_text=_("The size of the disk image in MB."),
    )
    filesystem = models.CharField(
        _("filesystem"),
        max_length=20,
        choices=FS_CHOICES,
        help_text=_("The filesystem of the disk."),
    )

class VirtualMachineDisk(models.Model):
    BLOCK_CHOICES = (
        ("xvda", _("/dev/xvda")),
        ("xvdb", _("/dev/xvdb")),
        ("xvdc", _("/dev/xvdc")),
    )
    virtual_machine = models.ForeignKey(
        VirtualMachine,
    )
    disk = models.ForeignKey(
        Disk,
    )
    block = models.CharField(
        _("block device"),
        max_length=20,
        choices=BLOCK_CHOICES,
        help_text=_("The block device assignment for the disk."),
    )