from rest_framework import serializers

class FileCheck(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        extension_file = value.name.split('.')[-1]
        if extension_file not in ['csv', 'xlsx']:
            raise serializers.ValidationError("Only CSV and XLSX file formats are allowed.")
        return value
