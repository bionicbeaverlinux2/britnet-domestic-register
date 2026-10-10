from django.db import models

class Resource(models.Model):
    CLASSIFICATIONS = [
        ('CLASS_A', 'Class A: Government Source'),
        ('CLASS_B', 'Class B: Verified Domestic Resource'),
        ('CLASS_C', 'Class C: Pending Review'),
        ('CLASS_D', 'Class D: Archived'),
        ('CLASS_E', 'Class E: Rejected'),
    ]

    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    classification = models.CharField(max_length=10, choices=CLASSIFICATIONS, default='CLASS_C')
    status = models.CharField(max_length=50, default='PENDING')
    reference_number = models.CharField(max_length=50, unique=True)
    review_date = models.DateField(auto_now_add=True)
    administrative_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.reference_number} - {self.name}"
