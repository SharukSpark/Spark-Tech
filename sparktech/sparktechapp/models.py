from django.db import models
from django.contrib.auth.models import User




class processor(models.Model):
    categ = (
        (1, 'ryzen3'), (2, 'ryzen5'), (3, 'ryzen7'), (4, 'ryzen9'), 
        (5, 'Threadripper'), (6, 'i3'), (7, 'i5'), (8, 'i7'), (9, 'i9')
    )
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Brand = models.TextField()
    CPU_Manufacture = models.CharField(max_length=255)
    CPU_Model = models.TextField()
    CPU_Speed = models.TextField()
    CPU_Socket = models.TextField()
    About_item1 = models.TextField()
    About_item2 = models.TextField()
    card_name = models.TextField()
    img1 = models.ImageField(upload_to='image')
    img2 = models.ImageField(upload_to='image')
    card_img = models.ImageField(upload_to='image')
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

    def __str__(self):
        return self.name

class motherboard(models.Model):
    categ = (
        (1, 'DDR 5'), (2, 'ThreadRipper Series'), (3, '650 Series'), 
        (4, '550 Series'), (5, '450 Series')
    )
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Brand = models.TextField()
    CPU_Socket = models.TextField()
    Compatible_Devicesl = models.TextField()
    RAM_Memory = models.TextField()
    Compatible_Processors = models.TextField()
    About_item1 = models.TextField()
    About_item2 = models.TextField()
    card_name = models.TextField()
    img1 = models.ImageField(upload_to='image')
    img2 = models.ImageField(upload_to='image')
    card_img = models.ImageField(upload_to='image')
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

class graphiccard(models.Model):
    categ = (
        (1, '4060 Series'), (2, '3050 Series'), (3, '1650 Series')
    )
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Graphics_Coprocessor = models.TextField()
    Brand = models.TextField()
    RAM_Size = models.TextField()
    GPU_Clock_Speed = models.TextField()
    Manufacturer = models.TextField()
    About_item1 = models.TextField()
    About_item2 = models.TextField()
    card_name = models.TextField()
    img1 = models.ImageField(upload_to='image')
    img2 = models.ImageField(upload_to='image')
    card_img = models.ImageField(upload_to='image')
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

class coolingsystem(models.Model):
    categ = (
        (1, 'Liquid Cooler-360mm'), (2, 'Liquid Cooler-240mm'), 
        (3, 'Liquid Cooler-120mm'), (4, 'Custom-RGB CPU Cooler'), 
        (5, 'CPU-RGB Cooler')
    )
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Product_Dimensions = models.TextField()
    Brand = models.TextField()
    Power_Connector_Type = models.TextField()
    Voltage = models.TextField()
    Cooling_Method = models.TextField()
    About_item1 = models.TextField()
    About_item2 = models.TextField()
    card_name = models.TextField()
    img1 = models.ImageField(upload_to='image')
    img2 = models.ImageField(upload_to='image')
    card_img = models.ImageField(upload_to='image')
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')


class ram(models.Model):
    categ = (
        (1, '8GB'), (2, '16GB'), 
        (3, '32GB'), (4, '64GB')
    )
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Computer_Memory_Size = models.TextField()
    Brand = models.TextField()
    RAM_Memory_Technology = models.TextField()
    Memory_Speed = models.TextField()
    Compatible_Devices = models.TextField()
    About_item1 = models.TextField()
    About_item2 = models.TextField()
    card_name = models.TextField()
    img1 = models.ImageField(upload_to='image')
    img2 = models.ImageField(upload_to='image')
    card_img = models.ImageField(upload_to='image')
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')


class ssd(models.Model):
    categ = (
        (1, '256GB'), (2, '500GB'), 
        (3, 'M.2 NVMe 256GB'), (4, 'M.2 NVMe 500GB'),(5, 'M.2 NVMe 1TB')
    )
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Digital_Storage_Capacity = models.TextField()
    Hard_Disk_Interface = models.TextField()
    Connectivity_Technology = models.TextField()
    Brand = models.TextField()
    Hard_Disk_Form_Factor = models.TextField()
    About_item1 = models.TextField()
    About_item2 = models.TextField()
    card_name = models.TextField()
    img1 = models.ImageField(upload_to='image')
    img2 = models.ImageField(upload_to='image')
    card_img = models.ImageField(upload_to='image')
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

class harddrive(models.Model):
    categ = (
        (1, '256GB'), (2, '500GB'), 
        (3, '1TB'), (4, '2TB'),(5, ' 4TB')
    )
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Digital_Storage_Capacity = models.TextField()
    Hard_Disk_Interface = models.TextField()
    Connectivity_Technology = models.TextField()
    Brand = models.TextField()
    Hard_Disk_Form_Factor = models.TextField()
    About_item1 = models.TextField()
    About_item2 = models.TextField()
    card_name = models.TextField()
    img1 = models.ImageField(upload_to='image')
    img2 = models.ImageField(upload_to='image')
    card_img = models.ImageField(upload_to='image')
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

class smbs(models.Model):
    categ = (
        (1, '400W'), (2, '500W'), 
        (3, '600W'), (4, '800W'),(5, '1000W')
    )
    name = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Model_Name = models.TextField()
    Brand = models.TextField()
    Connector_Type = models.TextField()
    Output_Wattage = models.TextField()
    About_item1 = models.TextField()
    About_item2 = models.TextField()
    card_name = models.TextField()
    img1 = models.ImageField(upload_to='image')
    img2 = models.ImageField(upload_to='image')
    card_img = models.ImageField(upload_to='image')
    cat = models.IntegerField(verbose_name='category', choices=categ)
    is_active = models.BooleanField(default=True, verbose_name='Available')

class CART (models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="userid")
    Processor=models.ForeignKey(processor,on_delete=models.CASCADE,db_column="processor",null=True, blank=True)
    Motherboard=models.ForeignKey(motherboard,on_delete=models.CASCADE,db_column="motherboard",null=True, blank=True)
    Graphiccard=models.ForeignKey(graphiccard,on_delete=models.CASCADE,db_column="graphiccard",null=True, blank=True)
    Coolingsystem=models.ForeignKey(coolingsystem,on_delete=models.CASCADE,db_column="coolingsystem",null=True, blank=True)
    Ram=models.ForeignKey(ram,on_delete=models.CASCADE,db_column="ram",null=True, blank=True)
    Ssd=models.ForeignKey(ssd,on_delete=models.CASCADE,db_column="ssd",null=True, blank=True)
    Smbs=models.ForeignKey(smbs,on_delete=models.CASCADE,db_column="smbs",null=True, blank=True)
    qty=models.IntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.CharField(max_length=255)  # This should ideally be a ForeignKey to your Product model
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    


