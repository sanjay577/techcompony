
from rest_framework import serializers
from .models import tech


class techSerializer(serializers.ModelSerializer):    
 class meta:
  models = tech
fields = ['id','name','description']