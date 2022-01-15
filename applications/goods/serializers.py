from rest_framework import serializers
from .models import Category, Section, Group, Subgroup, Card, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'card',
            'name',
            'description',
            'scope_of_app',
            'diameter',
            'length',
            'colour',
            'image',
            'get_absolute_url',

        ]



class CardDetailSerializer(serializers.ModelSerializer):
    scope_of_apps = serializers.CharField(source="get_all_scope_of_app", read_only=True)
    diameters = serializers.CharField(source="get_all_diameter", read_only=True)
    lenghts = serializers.CharField(source="get_all_length", read_only=True)
    colours = serializers.CharField(source="colour", read_only=True)
    images = serializers.CharField(source="get_all_images", read_only=True)
    cards = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields =  [
            'id',
            'subgroup',
            'name',
            'description',
            'scope_of_apps',
            'diameters',
            'lenghts',
            'colours',
            'image',
            'images',
            'get_absolute_url',
            'cards'
        ]
           
class CardListSerializer(serializers.ModelSerializer):
    scope_of_apps = serializers.CharField(source="get_all_scope_of_app", read_only=True)
    diameters = serializers.CharField(source="get_all_diameter", read_only=True)
    lenghts = serializers.CharField(source="get_all_length", read_only=True)
    colours = serializers.CharField(source="colour", read_only=True)
    images = serializers.CharField(source="get_all_images", read_only=True)
       
    class Meta:
        model = Card
        fields =  [
            'id',
            'subgroup',
            'name',
            'description',
            'scope_of_apps',
            'diameters',
            'lenghts',
            'colours',
            'image',
            'images',
            'get_absolute_url',

        ]


class SubgroupSerializer(serializers.ModelSerializer):
    subgroups = CardListSerializer(many=True, read_only=True)

    class Meta:
        model = Subgroup
        fields = [
            'id',
            'group',
            'name',
            'get_absolute_url',
            'subgroups'
            
        ]






class GroupSerializer(serializers.ModelSerializer):
    groups = SubgroupSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = [
            'id',
            'section',
            'name',
            'get_absolute_url',
            'groups',

        ]
        
        



class SectionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Section
        fields = [
            'id',
            'category',
            'name',
            'get_absolute_url',

        ]

    
        

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'get_absolute_url',
        ]
        



