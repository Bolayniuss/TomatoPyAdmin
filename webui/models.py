# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AutomatedActions(models.Model):
    id = models.IntegerField(primary_key=True)
    notifier = models.CharField(max_length=32)
    trigger = models.CharField(max_length=19)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'AutomatedActions'


class DestinationsFilesList(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=64)
    destinationname = models.CharField(db_column='destinationName', max_length=32) # Field name made lowercase.
    path = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'DestinationsFilesList'


class Parameters(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    parameters = models.TextField()

    class Meta:
        managed = False
        db_table = 'Parameters'


class RemoteServices(models.Model):
    servicename = models.CharField(db_column='serviceName', max_length=32) # Field name made lowercase.
    servername = models.CharField(db_column='serverName', max_length=32) # Field name made lowercase.
    parameters = models.TextField()

    class Meta:
        managed = False
        db_table = 'RemoteServices'


class ReplicatorActions(models.Model):
    torrentname = models.CharField(db_column='torrentName', max_length=256) # Field name made lowercase.
    torrentfilename = models.CharField(db_column='torrentFileName', max_length=256) # Field name made lowercase.
    torrentdata = models.TextField(db_column='torrentData') # Field name made lowercase.
    destinationname = models.CharField(db_column='destinationName', max_length=64) # Field name made lowercase.
    destinationrelativepath = models.CharField(db_column='destinationRelativePath', max_length=256) # Field name made lowercase.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ReplicatorActions'


class ReplicatorRemoteUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    lastupdate = models.DateTimeField(db_column='lastUpdate') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReplicatorRemoteUsers'


class TorrentTracker(models.Model):
    hash = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=128)
    status = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'TorrentTracker'


class TrackedDestinations(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    path = models.CharField(max_length=256)
    filter = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'TrackedDestinations'


class TrackedTorrentFiles(models.Model):
    hash = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    timeout = models.BigIntegerField()
    torrenthash = models.CharField(db_column='torrentHash', max_length=64) # Field name made lowercase.
    torrentfilename = models.CharField(db_column='torrentFileName', max_length=256) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrackedTorrentFiles'


class TrackedTorrents(models.Model):
    hash = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=128)
    torrentfile = models.TextField(db_column='torrentFile') # Field name made lowercase.
    magnet = models.TextField()

    class Meta:
        managed = False
        db_table = 'TrackedTorrents'


class TrackedTvShows(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    filter = models.CharField(max_length=64)
    authorfilter = models.CharField(db_column='authorFilter', max_length=64) # Field name made lowercase.
    sizelimits = models.TextField(db_column='sizeLimits') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrackedTvShows'