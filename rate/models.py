from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):
    trigram = models.CharField('trigramme', max_length=254)
    name = models.CharField('nom', max_length=254)

    def __str__(self):
        return '%s (%s)' % (self.name, self.trigram)

    class Meta:
        verbose_name = 'département'


class Year(models.Model):
    name = models.CharField('année', max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'année'


class Period(models.Model):
    name = models.CharField('période', max_length=254)
    year = models.ForeignKey('Year', on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.name, self.year)

    class Meta:
        verbose_name = 'période'


class Type(models.Model):
    name = models.CharField('type', max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'type'



class Course(models.Model):
    code = models.CharField('code', max_length=32)
    title = models.CharField('titre', max_length=254)
    professor = models.CharField('professeur', max_length=254)
    description = models.TextField('description')
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    period = models.ForeignKey('Period', on_delete=models.CASCADE)
    type = models.ForeignKey('Type', verbose_name='type', on_delete=models.CASCADE)
    has_pale = models.NullBooleanField('pâle')
    has_project = models.NullBooleanField('projet')
    has_presentation = models.NullBooleanField('présentation')
    has_oral = models.NullBooleanField('oral')

    def __str__(self):
        return '%s (%s%s)' % (self.title, self.department.trigram, self.code)

    class Meta:
        verbose_name = 'cours'
        verbose_name_plural = 'cours'


class Student(models.Model):
    user = models.OneToOneField(User, verbose_name='utilisateur', on_delete=models.CASCADE)
    name = models.CharField('nom', max_length=254)
    first_name = models.CharField('prénom', max_length=254)
    last_name = models.CharField('nom de famille', max_length=254)
    promotion = models.CharField('promotion', max_length=12)

    def __str__(self):
        return '%s (%s)' % (self.name, self.promotion)

    class Meta:
        verbose_name = 'élève'


class Assessment(models.Model):
    course = models.ForeignKey('Course', verbose_name='cours', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', verbose_name='élève', on_delete=models.SET_NULL,null=True)
    amphi_grade = models.IntegerField('note d\'amphi')
    pc_grade = models.IntegerField('note de PC')
    interest_grade = models.IntegerField('note d\'intérêt')
    difficulty_grade = models.IntegerField('note de difficulté')
    comment = models.TextField('commentaire')

    def __str__(self):
        total_grade = float(self.amphi_grade + self.pc_grade + self.interest_grade) / 3
        return '%s%s noté par %s (%.1f)' % (self.course.department.trigram, self.course.code, self.student.name, total_grade)

    class Meta:
        verbose_name = 'évalutation'
