from django.urls import path
from ecomapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing),
    path('Menu1', views.Menu1),
    path('register', views.register),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('catfilter/<cv>', views.catfilter),
    path('sort/<sv>', views.sortbyprice),
    path('pricefilter', views.pricefilter),
    path('search', views.search),
    path('Menudetail/<pid>', views.Menudetail),
    path('addtocart/<pid>', views.addtocart),
    path('viewcart', views.viewcart),
    path('updateqty/<x>/<cid>', views.updateqty),
    path('remove/<cid>', views.remove),
    path('placeholder', views.placeorder),
    path('fetchorder', views.fetchorder),
    path('makepayment', views.makepayment),
    path('paymentsuccess', views.paymentsuccess),
    path('landing', views.landing),
    path('orderhistory', views.orderhistory),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)