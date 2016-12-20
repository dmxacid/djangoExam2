from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# Create your models here.
class AppointmentManager(models.Manager):
    def add_appointment(self, postData):
        errors = []
        if not len(postData['date']):
            errors.append('Date is required')
        if not len(postData['time']):
            errors.append('Time is required')
        if not len(postData['tasks']):
            errors.append('Task is required')
        if not postData['date']:
            errors.append('Birthdate is required')
        modelsResponse = {}
        if errors:
            #failed ver
            modelsResponse['isValid'] = False
            modelsResponse['errors'] = errors
        else:
            modelsResponse['isValid'] = True
            appointment = self.create(appointDay = postData['date'], appointTime =
            str(postData['time']), tasks = postData['tasks'])
            modelsResponse['appointment'] = appointment
        return modelsResponse
    def edit_appointment(self, postData):
        errors = []
        if not len(postData['date']):
            errors.append('Date is required')
        if not len(postData['time']):
            errors.append('Time is required')
        if not len(postData['tasks']):
            errors.append('Task is required')
        if not len(postData['status']):
            errors.append('Status is required')
        modelsResponse = {}
        if errors:
            #failed ver
            modelsResponse['isValid'] = False
            modelsResponse['errors'] = errors
        else:
            modelsResponse['isValid'] = True
            appointment = self.create(appointDay = postData['date'], appointTime =
            str(postData['time']), tasks = postData['tasks'], status = postData['status'])
            modelsResponse['appointment'] = appointment
        return modelsResponse

class UserManager(models.Manager):
    def add_user(self, postData):
        errors = []
        if not len(postData['first_name']):
            errors.append('First name is required')
        if len(postData['first_name']) < 3:
            errors.append('Name must be at 3 characters long!')
        check_email = self.filter(email = postData['email'])
        if check_email:
            errors.append('Sorry email already exists!')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters!')
        if not postData['password'] == postData['confirm_password']:
            errors.append('Passwords must match!')
        modelsResponse = {}
        if errors:
            #failed ver
            modelsResponse['isRegistered'] = False
            modelsResponse['errors'] = errors
        else:
            #pass
            hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = self.create(first_name = postData['first_name'], email =
            postData['email'], password = hashed_password)
            modelsResponse['isRegistered'] = True
            modelsResponse['user'] = user
        return modelsResponse
    def login_user(self, postData):
        user = self.filter(email = postData['email'])
        errors = []
        modelsResponse = {}
        if not user:
            errors.append('Invalid email!')
        else:
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                modelsResponse['isLoggedIn'] = True
                modelsResponse['user'] = user[0]
            else:
                errors.append('Invalid email/password combination!')
        if errors:
            modelsResponse['isLoggedIn'] = False
            modelsResponse['errors'] = errors
        return modelsResponse
class User(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
class Appointments(models.Model):
    appointDay = models.CharField(max_length=100)
    appointTime = models.CharField(max_length=100)
    tasks = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default = '')
    objects = AppointmentManager()
