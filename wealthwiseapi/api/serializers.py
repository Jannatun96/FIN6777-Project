# Response objects can not handle complex data types
# Serializer will convert to JSON
from rest_framework import serializers


class CombinedSerializer(serializers.Serializer):
    first_account_number = serializers.IntegerField()
    first_account_info = serializers.DictField()
    second_account_number = serializers.CharField()
    second_account_info = serializers.DictField()
    total_bank_balance = serializers.IntegerField()

class CombinedPostSerializer(serializers.Serializer):
    first_account_number = serializers.IntegerField()
    first_account_info = serializers.DictField()
    second_account_number = serializers.CharField()
    second_account_info = serializers.DictField()
    total_bank_balance = serializers.IntegerField()
    manual_balance = serializers.IntegerField()



