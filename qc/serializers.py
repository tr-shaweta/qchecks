from rest_framework import serializers
from .models import Inspection

class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'
    # Define the fields for steps and carton details
    constructionItemStep1 = serializers.CharField(required=False, allow_blank=True)
    constructionItemStep2 = serializers.CharField(required=False, allow_blank=True)
    constructionItemStep3 = serializers.CharField(required=False, allow_blank=True)
    constructionItemStep4 = serializers.CharField(required=False, allow_blank=True)
    constructionItemStep5 = serializers.CharField(required=False, allow_blank=True)
    constructionItemStep6 = serializers.CharField(required=False, allow_blank=True)
    constructionItemStep7 = serializers.CharField(required=False, allow_blank=True)
    constructionItemStep8 = serializers.CharField(required=False, allow_blank=True)
    constructionItemStep9 = serializers.CharField(required=False, allow_blank=True)
    
    assemblyStep1 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep2 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep3 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep4 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep5 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep6 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep7 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep8 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep9 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep10 = serializers.CharField(required=False, allow_blank=True)
    assemblyStep11 = serializers.CharField(required=False, allow_blank=True)
    
    cartonDetailsStep1 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep1value = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep2 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep2value = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep3 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep3value = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep4 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep4value = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep5 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep5value = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep6 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep6value = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep7 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep7value = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep8 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep8value = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep9 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep9value = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep10 = serializers.CharField(required=False, allow_blank=True)
    cartonDetailsStep10value = serializers.CharField(required=False, allow_blank=True)
   


    def create(self, validated_data):
        # Extract individual steps for construction, assembly, and carton details
       
        constructionSteps = {
            "constructionItemStep1": validated_data.pop('constructionItemStep1', ''),
            "constructionItemStep2": validated_data.pop('constructionItemStep2', ''),
            "constructionItemStep3": validated_data.pop('constructionItemStep3', ''),
            "constructionItemStep4": validated_data.pop('constructionItemStep4', ''),
            "constructionItemStep5": validated_data.pop('constructionItemStep5', ''),
            "constructionItemStep6": validated_data.pop('constructionItemStep6', ''),
            "constructionItemStep7": validated_data.pop('constructionItemStep7', ''),
            "constructionItemStep8": validated_data.pop('constructionItemStep8', ''),
            "constructionItemStep9": validated_data.pop('constructionItemStep9', ''),
        }

        assemblySteps = {
            "assemblyStep1": validated_data.pop('assemblyStep1', ''),
            "assemblyStep2": validated_data.pop('assemblyStep2', ''),
            "assemblyStep3": validated_data.pop('assemblyStep3', ''),
            "assemblyStep4": validated_data.pop('assemblyStep4', ''),
            "assemblyStep5": validated_data.pop('assemblyStep5', ''),
            "assemblyStep6": validated_data.pop('assemblyStep6', ''),
            "assemblyStep7": validated_data.pop('assemblyStep7', ''),
            "assemblyStep8": validated_data.pop('assemblyStep8', ''),
            "assemblyStep9": validated_data.pop('assemblyStep9', ''),
            "assemblyStep10": validated_data.pop('assemblyStep10', ''),
            "assemblyStep11": validated_data.pop('assemblyStep11', ''),
        }

        cartonDetails = {
            "cartonDetailsStep1": validated_data.pop('cartonDetailsStep1', ''),
            "cartonDetailsStep1value": validated_data.pop('cartonDetailsStep1value', ''),
            "cartonDetailsStep2": validated_data.pop('cartonDetailsStep2', ''),
            "cartonDetailsStep2value": validated_data.pop('cartonDetailsStep2value', ''),
            "cartonDetailsStep3": validated_data.pop('cartonDetailsStep3', ''),
            "cartonDetailsStep3value": validated_data.pop('cartonDetailsStep3value', ''),
            "cartonDetailsStep4": validated_data.pop('cartonDetailsStep4', ''),
            "cartonDetailsStep4value": validated_data.pop('cartonDetailsStep4value', ''),
            "cartonDetailsStep5": validated_data.pop('cartonDetailsStep5', ''),
            "cartonDetailsStep5value": validated_data.pop('cartonDetailsStep5value', ''),
            "cartonDetailsStep6": validated_data.pop('cartonDetailsStep6', ''),
            "cartonDetailsStep6value": validated_data.pop('cartonDetailsStep6value', ''),
            "cartonDetailsStep7": validated_data.pop('cartonDetailsStep7', ''),
            "cartonDetailsStep7value": validated_data.pop('cartonDetailsStep7value', ''),
            "cartonDetailsStep8": validated_data.pop('cartonDetailsStep8', ''),
            "cartonDetailsStep8value": validated_data.pop('cartonDetailsStep8value', ''),
            "cartonDetailsStep9": validated_data.pop('cartonDetailsStep9', ''),
            "cartonDetailsStep9value": validated_data.pop('cartonDetailsStep9value', ''),
            "cartonDetailsStep10": validated_data.pop('cartonDetailsStep10', ''),
            "cartonDetailsStep10value": validated_data.pop('cartonDetailsStep10value', ''),
        }

        # Assign the extracted data to the validated_data dictionary
        validated_data['constructionSteps'] = constructionSteps
        validated_data['assemblySteps'] = assemblySteps
        validated_data['cartonDetails'] = cartonDetails

        return Inspection.objects.create(**validated_data)

    def validate(self, data):
        # Print or log validated data for debugging
      
        return super().validate(data)
