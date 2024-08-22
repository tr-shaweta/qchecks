from django.db import models

# Create your models here.
class Inspection(models.Model):
    clientName = models.CharField(max_length=255)
    skuNumber= models.CharField(max_length=255)
    itemDescription = models.TextField()
    poNumber = models.CharField(max_length=255)
    qtyPieces = models.IntegerField()
    factoryName = models.CharField(max_length=255)
    inspectedBy = models.CharField(max_length=255)
    dateTime = models.DateTimeField(auto_now=True)
    inspectionResult = models.CharField(max_length=255)
    constructionSteps = models.JSONField(default=dict)  # To store all construction steps
    assemblySteps = models.JSONField(default=dict)  # To store all assembly steps
    cartonDetails = models.JSONField(default=dict)  # To store carton details
    cartonLength = models.FloatField()
    cartonWidth = models.FloatField()
    cartonWeight = models.FloatField()
    grossWeight = models.FloatField()
    netWeight = models.FloatField()
    
    