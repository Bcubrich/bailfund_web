from django.db import models
from django.core.validators import MinLengthValidator




class Roster(models.Model):
    name = models.CharField(max_length=200, db_column='Arrestee Name')
    housing = models.CharField(max_length=8, db_column='Housing')
    so = models.CharField(max_length=6, db_column='SO #')
    booking = models.CharField(max_length=6, db_column='Booking')
    booking_dt = models.CharField(max_length=6, db_column='Booking Date/Time')
    age = models.CharField(max_length=2, db_column='Age')
    sex = models.CharField(max_length=2, db_column='Sex')
    race = models.CharField(max_length=2, db_column='Race')
    ethnicity = models.CharField(max_length=20, db_column='Ethnicity')
    tp = models.CharField(max_length=2, db_column='TP')
    charges = models.CharField(max_length=400, db_column='Charges')
    dt = models.CharField(max_length=20, db_column='dt')
    firstname = models.CharField(max_length=100, db_column='First Name')
    lastname = models.CharField(max_length=30, db_column='Last Name')
    date_added = models.CharField(max_length=30, db_column='Date_Added')
    bondmean = models.FloatField(max_length=7, db_column='bondmean')
    bondmedian = models.FloatField(max_length=7, db_column='bondmedian')
    bondmin = models.FloatField(max_length=7, db_column='bondmin')
    bondmax = models.FloatField(max_length=7, db_column='bondmax')


    class Meta:
        db_table='roster'
        app_label = 'bailfund'

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Errors(models.Model) :
    so = models.CharField(max_length=6, db_column='SO #')
    error = models.CharField(max_length=6, db_column='error')

    class Meta:
        db_table='errors'
        app_label = 'bailfund'

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Personal(models.Model):

    sex = models.CharField(max_length=2, db_column='Sex')
    age = models.CharField(max_length=3, db_column='Age')
    height = models.CharField(max_length=4, db_column='Height')
    weight = models.CharField(max_length=4, db_column='Weight')
    race = models.CharField(max_length=30, db_column='Race')
    so = models.CharField(max_length=6, db_column='SO #')
    name = models.CharField(max_length=200, db_column='Name')
    date_added = models.CharField(max_length=30, db_column='DateAdded')
    runtime = models.CharField(max_length=8, db_column='RunTime')

    class Meta:
        db_table='personal'
        app_label = 'bailfund'

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Bond(models.Model) :

    case = models.CharField(max_length=6, db_column='Case')
    amount = models.CharField(max_length=11, db_column='Amount')
    status = models.CharField(max_length=200, db_column='Status')
    postedby = models.CharField(max_length=100, db_column='Posted By')
    postdate = models.CharField(max_length=6, db_column='Post Date')
    so = models.CharField(max_length=6, db_column='SO #')
    date_added = models.CharField(max_length=30, db_column='DateAdded')

    class Meta:
        db_table='bond'
        app_label = 'bailfund'

    def __str__(self):
        """String for representing the Model object."""
        return self.name







