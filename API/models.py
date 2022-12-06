from django.db import models

# Create your models here.
class profile(models.Model):

	AGE_CHOICE = (
    (-0.95197, '18-24'),
        (-0.07854, '25-34'),
        (0.49788, '34-44'),
        (1.09449, '45-54'),
        (1.82213, '55-64'),
        (2.59171, '65+')
    )

	GENDER_CHOICE = (
		(0.48246, 'Male'),
		(-0.48246, 'Female')
	)

	EDUCATION_CHOICE = (
		(-2.43591, 'Left school before 16 years'),
		(-1.73790, 'Left school at 16 years'),
		(-1.43719, 'Left school at 17 years'),
		(-1.22751, 'Left school at 18 years'),
		(-0.61113, 'Some college or university, no certificate or degree'),
		(-0.05921, 'Professional certificate/diploma'),
		(0.45468, 'University Degree'),
		(1.16365, 'Masters degree'),
		(1.98437, 'Doctorate degree')
	)

	COUNTRY_CHOICE = (
		(-0.09765, 'Australia'),
		(0.24923, 'Canada'),
		(-0.46831, 'New Zealand'),
		(-0.28519, 'Other'),
		(0.21128, 'Republic of Ireland'),
		(0.96082, 'UK'),
		(-0.57009, 'USA')
	)

	ETHNICITY_CHOICE = (
		(-0.50212, 'Asian'),
		(-1.10702, 'Black'),
		(1.90725, 'Mixed-Black/Asian'),
		(0.12600, 'Mixed-White/Asian'),
		(-0.22166, 'Mixed-White/Black'),
		(0.11440, 'Other'),
		(-0.31685, 'White')
	)

    age=models.IntegerField(choices=AGE_CHOICE)
    gender=models.IntegerField(choices=GENDER_CHOICE)
    education=models.IntegerField(choices=EDUCATION_CHOICE)
    country=models.IntegerField(choices=COUNTRY_CHOICE)
    ethnicity=models.IntegerField(choices=COUNTRY_CHOICE)
    nScore=models.IntegerField(choices=CSCORE_CHOICE)
    eScore=models.IntegerField(default=0)
    oScore=models.IntegerField(default=0)
    aScore=models.IntegerField(default=0)
    cScore=models.IntegerField(default=0)
    impulsiveness=models.IntegerField(default=0)
    sensationSeeing=models.IntegerField(default=0)

    def __str__(self):
        return self.age, self.impulsiveness