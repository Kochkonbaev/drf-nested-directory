from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product, Section, Group, Subgroup, Card
from .serializers import (CategorySerializer, ProductSerializer,
                        SectionSerializer,GroupSerializer,
                        SubgroupSerializer, 
                        CardDetailSerializer, CardListSerializer)


class CategoryList(APIView):
    """ Список категорий """
    def get(self, request,  format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class SectionList(APIView):
    """ Список секций """
    def get(self, request, category_slug, format=None):
        sections = Section.objects.filter(category__slug=category_slug)
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)


class GroupList(APIView):
    """ Список групп """
    def get(self, request, category_slug, section_slug, format=None):
        groups = Group.objects.filter(section__slug=section_slug)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)


class SubgroupList(APIView):
    """ Список подгрупп """
    def get(self, request, category_slug, section_slug, group_slug, format=None):
        subgroups = Subgroup.objects.filter(group__slug=group_slug)
        serializer = SubgroupSerializer(subgroups, many=True)
        return Response(serializer.data)


class CardList(APIView):
    """ Список карточек """
    def get(self, request, category_slug, section_slug, group_slug, subgroup_slug, format=None):
        cards = Card.objects.filter(subgroup__slug=subgroup_slug)
        serializer = CardListSerializer(cards, many=True)
        return Response(serializer.data)


class CardDetail(APIView):
    """ Детальный вид карточки """
    def get_object(self, subgroup_slug, card_slug):
        try:
            return Card.objects.filter(subgroup__slug=subgroup_slug).get(slug=card_slug)
        except Card.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, section_slug, group_slug, subgroup_slug, card_slug, format=None):
        card = self.get_object(subgroup_slug, card_slug)
        serializer = CardDetailSerializer(card)
        return Response(serializer.data)

class ProductDetail(APIView):
    """ Детальный вид Продукта """
    def get_object(self, card_slug, prod_slug):
        try:
            return Product.objects.filter(card__slug=card_slug).get(slug=prod_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, section_slug, group_slug, subgroup_slug, card_slug, prod_slug, format=None):
        card = self.get_object(card_slug, prod_slug)
        serializer = ProductSerializer(card)
        return Response(serializer.data)
