from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.utils import timezone


DDOS_TYPE_CHOICES = [('udp', 'udp'), ('others...', 'others...')]


# Create your models here.

class ProgressData(models.Model):
    scenario = models.TextField(max_length=50, default='None')
    stage_1_status = models.IntegerField(default=1)  # 1: off, 2: running, 3: finished
    stage_1_detail = models.TextField(default='None')
    stage_2_status = models.IntegerField(default=1)  # 1: off, 2: running, 3: finished
    stage_2_detail = models.TextField(default='None')
    stage_3_status = models.IntegerField(default=1)  # 1: off, 2: running, 3: finished
    stage_3_detail = models.TextField(default='None')
    stage_4_status = models.IntegerField(default=1)  # 1: off, 2: running, 3: finished
    stage_4_detail = models.TextField(default='None')
    stage_5_status = models.IntegerField(default=1)  # 1: off, 2: running, 3: finished
    stage_5_detail = models.TextField(default='None')
    stage_6_status = models.IntegerField(default=1)  # 1: off, 2: running, 3: finished
    stage_6_detail = models.TextField(default='None')
    stage_7_status = models.IntegerField(default=1)  # 1: off, 2: running, 3: finished
    stage_7_detail = models.TextField(default='None')


class Testbed(models.Model):
    status = models.IntegerField(default=1)  # 1: off, 2: running, 3: finished
    number_of_controller = models.IntegerField(default=1)  # only 1
    number_of_data_logger_server = models.IntegerField(default=1)  # only 1
    number_of_target_server = models.IntegerField(default=1)  # only 1
    number_of_benign_server = models.IntegerField(default=1)  # only 1
    number_of_vulnerable_client = models.IntegerField(default=1)
    number_of_non_vulnerable_client = models.IntegerField(default=1)
    number_of_attacker_server = models.IntegerField(default=1)  # only 1
    number_of_malicious_client = models.IntegerField(default=1)  # only 1


class Controller(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    path = models.CharField(max_length=255)


class DataLoggerServer(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="root")
    password = models.CharField(max_length=255)
    path = models.CharField(max_length=255, default="/root")
    network_interface = models.CharField(max_length=255)
    atop_interval = models.IntegerField(default=1)  # second


class TargetServer(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="root")
    password = models.CharField(max_length=255)
    path = models.CharField(max_length=255, default="/root")


class BenignServer(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="root")
    password = models.CharField(max_length=255)
    path = models.CharField(max_length=255, default="/root")


class VulnerableClient(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="root")
    password = models.CharField(max_length=255)
    path = models.CharField(max_length=255, default="/root")


class NonVulnerableClient(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="root")
    password = models.CharField(max_length=255)
    path = models.CharField(max_length=255, default="/root")


class AttackerServer(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="root")
    password = models.CharField(max_length=255)
    path = models.CharField(max_length=255, default="/root")
    number_of_new_bots = models.IntegerField(default=3)
    DDoS_type = models.CharField(max_length=10, choices=DDOS_TYPE_CHOICES, default="udp")
    DDoS_duration = models.IntegerField(default=30, validators=[MaxValueValidator(1000000), MinValueValidator(10)])


class MaliciousClient(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, default="root")
    password = models.CharField(max_length=255)
    path = models.CharField(max_length=255, default="/root")


class AttackScenario(models.Model):
    mirai = models.BooleanField(default=True)
    ransomware = models.BooleanField(default=True)
    resource_hijacking = models.BooleanField(default=True)
    disk_wipe = models.BooleanField(default=True)
    end_point_dos = models.BooleanField(default=True)






