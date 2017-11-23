from django.conf.urls import url
from . import views,viewsorders

urlpatterns = [
    #===========商品展示==================
    url(r'^$',views.shopindex, name='shopindex'), #网站首页
    url(r'^shoplist$',views.shoplist, name='shoplist'), #商品列表页
    url(r'^shopmeilanx/(?P<gid>[0-9]+)$',views.shopmeilanx, name='shopmeilanx'), #商品详情
    
    #===========会员模块==================
     url(r'^shoplogin$',views.shoplogin, name='shoplogin'), #网站登录
     url(r'^shopregister$',views.shopregister, name='shopregister'), #会员注册
     url(r'^shopinsert$', views.shopinsert, name="shopinsert"),
     url(r'^shopdologin$', views.shopdologin, name="shopdologin"),#会员执行登录
     url(r'^shoplogout$', views.shoplogout, name="shoplogout"),#会员退出

    #===========购物车模块================
    url(r'^shopcart$',viewsorders.shopcart, name='shopcart'), #购物车
    url(r'^shopcartadd/(?P<sid>[0-9]+)$',viewsorders.shopcartadd, name='shopcartadd'), #购物车
    url(r'^shopcartdel/(?P<sid>[0-9]+)$',viewsorders.shopcartdel, name='shopcartdel'), #购物车
    url(r'^shopcartclear$',viewsorders.shopcartclear, name='shopcartclear'), #购物车
    url(r'^shopcartchange$',viewsorders.shopcartchange, name='shopcartchange'), #购物车

    #===========订单路由==================
    url(r'^shoporderform$',viewsorders.shoporderform, name='shoporderform'), #订单表单
    url(r'^shoporderconfirm$',viewsorders.shoporderconfirm, name='shoporderconfirm'), #订单确认
    url(r'^shoporderinsert$',viewsorders.shoporderinsert, name='shoporderinsert'), #执行订单
    url(r'^shoporderinfo$',viewsorders.shoporderinfo, name='shoporderinfo'), #订单详情

    #===========我的订单============================
    url(r'^order$',viewsorders.order, name='order'), #我的订单
    #====================个人中心============================
    url(r'^member$',viewsorders.member, name='member'), #个人中心

]
