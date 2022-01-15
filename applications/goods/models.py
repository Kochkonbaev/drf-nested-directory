from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/{self.slug}/'
    
    def __str__(self):
        return self.name


class Section(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/{self.category.slug}/{self.slug}/'

    def __str__(self):
        return self.name


class Group(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='sections', null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/{self.section.category.slug}/{self.section.slug}/{self.slug}/'

    def __str__(self):
        return self.name


class Subgroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='groups', null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/{self.group.section.category.slug}/{self.group.section.slug}/{self.group.slug}/{self.slug}/'

    def __str__(self):
        return self.name


class Card(models.Model):
    subgroup = models.ForeignKey(Subgroup, on_delete=models.CASCADE, related_name='subgroups', null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_image', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def get_all_diameter(self):
        diameter_array = [[i for i in f.values()][0] 
               for f in Product.objects.filter(card=self.pk).values('diameter')]
        return diameter_array

    def colour(self):       
        colour_array = [[i for i in f.values()][0] 
               for f in Product.objects.filter(card=self.pk).values('colour')]
        return colour_array

    def get_all_scope_of_app(self):
        scope_of_app_array = [[i for i in f.values()][0] 
               for f in Product.objects.filter(card=self.pk).values('scope_of_app')]
        return scope_of_app_array
    
    def get_all_length(self):
        lenght_array = [[i for i in f.values()][0] 
               for f in Product.objects.filter(card=self.pk).values('length')]
        return lenght_array
    
    def get_all_images(self):
        image_array = [[i for i in f.values()][0] 
               for f in Product.objects.filter(card=self.pk).values('image')]
        return image_array   
    
        
    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/{self.subgroup.group.section.category.slug}/{self.subgroup.group.section.slug}/{self.subgroup.group.slug}/{self.subgroup.slug}/{self.slug}/'

    def __str__(self):
        return self.name


class Product(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='cards', null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    scope_of_app = models.CharField(max_length=255, blank=True, null=True)
    diameter = models.FloatField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    colour = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='product_image', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/{self.card.subgroup.group.section.category.slug}/{self.card.subgroup.group.section.slug}/{self.card.subgroup.group.slug}/{self.card.subgroup.slug}/{self.card.slug}/{self.slug}/'

    def __str__(self):
        return self.name
