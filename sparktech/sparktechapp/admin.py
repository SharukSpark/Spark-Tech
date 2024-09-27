from django.contrib import admin
from sparktechapp.models import processor, motherboard, graphiccard, coolingsystem,ram,ssd,harddrive,smbs

class ProcessorAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'Brand', 'CPU_Manufacture', 'CPU_Model', 
        'CPU_Speed', 'CPU_Socket', 'About_item1', 'About_item2', 
        'card_name', 'img1', 'img2', 'card_img', 
        'cat', 'is_active'
    ]
    list_filter = ['cat', 'is_active']

admin.site.register(processor, ProcessorAdmin)

class MotherboardAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'Brand', 'CPU_Socket', 'Compatible_Devicesl', 
        'RAM_Memory', 'Compatible_Processors', 'About_item1', 'About_item2', 
        'card_name', 'img1', 'img2', 'card_img', 
        'cat', 'is_active'
    ]
    list_filter = ['cat', 'is_active']

admin.site.register(motherboard, MotherboardAdmin)

class GraphiccardAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'Graphics_Coprocessor', 'Brand', 'RAM_Size', 
        'GPU_Clock_Speed', 'Manufacturer', 'About_item1', 'About_item2', 
        'card_name', 'img1', 'img2', 'card_img', 
        'cat', 'is_active'
    ]
    list_filter = ['cat', 'is_active']

admin.site.register(graphiccard, GraphiccardAdmin)

class CoolingsystemAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'Product_Dimensions', 'Brand', 'Power_Connector_Type', 
        'Voltage', 'Cooling_Method', 'About_item1', 'About_item2', 
        'card_name', 'img1', 'img2', 'card_img', 
        'cat', 'is_active'
    ]
    list_filter = ['cat', 'is_active']

admin.site.register(coolingsystem, CoolingsystemAdmin)

class RamAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'Computer_Memory_Size', 'Brand', 'RAM_Memory_Technology', 
        'Memory_Speed', 'Compatible_Devices', 'About_item1', 'About_item2', 
        'card_name', 'img1', 'img2', 'card_img', 
        'cat', 'is_active'
    ]
    list_filter = ['cat', 'is_active']

admin.site.register(ram, RamAdmin)

class SsdAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'Digital_Storage_Capacity', 'Hard_Disk_Interface', 'Connectivity_Technology', 
        'Brand', 'Hard_Disk_Form_Factor', 'About_item1', 'About_item2', 
        'card_name', 'img1', 'img2', 'card_img', 
        'cat', 'is_active'
    ]
    list_filter = ['cat', 'is_active']

admin.site.register(ssd, SsdAdmin)

class HarddriveAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'Digital_Storage_Capacity', 'Hard_Disk_Interface', 'Connectivity_Technology', 
        'Brand', 'Hard_Disk_Form_Factor', 'About_item1', 'About_item2', 
        'card_name', 'img1', 'img2', 'card_img', 
        'cat', 'is_active'
    ]
    list_filter = ['cat', 'is_active']

admin.site.register(harddrive, HarddriveAdmin)

class SmbsAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price', 'Model_Name', 'Brand', 
        'Connector_Type', 'Output_Wattage', 'About_item1', 'About_item2', 
        'card_name', 'img1', 'img2', 'card_img', 
        'cat', 'is_active'
    ]
    list_filter = ['cat', 'is_active']

admin.site.register(smbs, SmbsAdmin)
