from django.urls import path
from Frontend import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('disproduct/<itemcatg>/',views.disproduct,name="disproduct"),
    path('productsingle/<int:dataid>',views.productsingle,name="productsingle"),
    path('savecontactus/',views.savecontactus,name="savecontactus"),
    path('weblogin/',views.weblogin,name="weblogin"),
    path('savecustomer/',views.savecustomer,name="savecustomer"),
    path('custemerlogin/',views.custemerlogin,name="custemerlogin"),
    path('logout/',views.logout,name="logout"),

    path('savecart/',views.savecart,name="savecart"),
    path('viewcartpage/',views.viewcartpage,name="viewcartpage"),
    path('deletecartfont/<int:dataid>',views.deletecartfont,name="deletecartfont"),
    path('check/',views.check,name="check"),
    path('savecheck/',views.savecheck,name="savecheck"),
]