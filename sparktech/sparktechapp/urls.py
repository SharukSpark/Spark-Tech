# sparktechapp/urls.py
from django.urls import path, include
from sparktechapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
   
    path('home/', views.home),
    
    path('about/', views.about),

    path('cart/', views.viewcart),

    path('cart/remove/<int:cid>/', views.remove),

    path('order-history/', views.order_history),

    path('order-detail/<int:order_id>/', views.order_detail),

    path('terms-conditions/', views.terms_conditions),

    path('update/<str:qv>/<int:cid>/', views.updateqty),

    path('checkout/', views.checkout),

    path('account/', views.account_view),   

    path('search-suggestions/', views.search_suggestions, name='search_suggestions'),

    path('search/', views.search_results, name='search_results'),

    path('shipping/<int:order_id>/', views.shipping , name='shipping'),


    path('invoice/<int:order_id>/', views.invoice, name='invoice'),




    path('payment/<int:id>/', views.payment, name='payment'),
    # path('pay/', views.pay, name='pay'),
 

    path('addtocart1/<pid>', views.addtocart_1), 
    path('addtocart2/<pid>', views.addtocart_2), 
    path('addtocart3/<pid>', views.addtocart_3), 
    path('addtocart4/<pid>', views.addtocart_4), 
    path('addtocart5/<pid>', views.addtocart_5), 
    path('addtocart6/<pid>', views.addtocart_6), 
    path('addtocart7/<pid>', views.addtocart_7), 

    path('graphiccargdetails/<int:pid>/', views.graphiccargdetails),
    path('graphiccardlist/',views.graphiccardlist),
    path('Cards_1650/',views.Cards_1650),
    path('Cards_3050/',views.Cards_3050),
    path('Cards_4060/',views.Cards_4060),

    path('coolingsystemdetails/<int:pid>/', views.coolingsystemdetails),
    path('coolingsystemdlist/',views.coolingsystemdlist),
    path('Cooler_120mm/',views.Cooler_120mm),
    path('Cooler_240mm/',views.Cooler_240mm),
    path('Cooler_300mm/',views.Cooler_360mm),
    path('CPU_RGB_Coole/',views.CPU_RGB_Cooler),
    path('Custom_RGB_Cooler/',views.Custom_RGB_Cooler),

    path('processordetails/<int:pid>/', views.processordetails),
    path('processorlist/', views.processorlist),
    path('ryzen3/', views.ryzen3),
    path('ryzen5/', views.ryzen5),
    path('ryzen7/', views.ryzen7),
    path('ryzen9/', views.ryzen9),
    path('Threadripper_Series/', views.Threadripper_Series),
    path('i3_Series/', views.i3_Series),    
    path('i5_Series/', views.i5_Series),
    path('i7_Series/', views.i7_Series),
    path('i9_Series/', views.i9_Series),

    path('motherboarddetails/<int:pid>/', views.motherboarddetails),
    path('motherboardlist/',views.motherboardlist),
    path('DDR_5/', views.DDR_5),
    path('ThreadRipper/', views.ThreadRipper),
    path('board_650/', views.board_650),
    path('board_550/', views.board_550),
    path('board_450/', views.board_450),

    path('ssddetails/<int:pid>/',views.ssddetails),
    path('ssdlist/',views.ssdlist),
    path('ssd_256GB/',views.ssd_256GB),
    path('ssd_500GB/',views.ssd_500GB),
    path('M_2_NVMe_256GB/',views.M_2_NVMe_256GB),
    path('M_2_NVMe_500GB/',views.M_2_NVMe_500GB),
    path('M_2_NVMe_1TB/',views.M_2_NVMe_1TB),

    path('harddrivedetails/<int:pid>/',views.harddrivedetails),
    path('hddlist/',views.hddlist),
    path('hdd_256GB/',views.hdd_256GB),
    path('hdd_500GB/',views.hdd_500GB),
    path('hdd_1TB/',views.hdd_1TB),
    path('hdd_2TB/',views.hdd_2TB),
    path('hdd_4TB/',views.hdd_4TB),

    path('ramdetails/<int:pid>/',views.ramdetails),
    path('ramlist/',views.ramlist),
    path('Ram_8GB/',views.Ram_8GB),
    path('Ram_16GB/',views.Ram_16GB),
    path('Ram_32GB/',views.Ram_32GB),
    path('Ram_64GB/',views.Ram_64GB),

    path('smbsdetails/<int:pid>/',views.smbsdetails),
    path('smbslist/',views.smbslist),
    path('smbs_400W/',views.smbs_400W),
    path('smbs_500W/',views.smbs_500W),
    path('smbs_600W/',views.smbs_600W),
    path('smbs_800W/',views.smbs_800W),
    path('smbs_1000w/',views.smbs_1000W),


    path('login/', views.logindetails),
    path('logout/', views.logoutdetails),
    
    path('register/',views.registerdetails),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

