from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myadmin.models import Detail
import time,json


#====================后台订单详情表===========================
def index(request):
    return render(request,"myadmin/index.html")

# 浏览订单详情
def detailindex(request):
    # 执行数据查询，并放置到模板中
    list = Detail.objects.all()
    context = {"detaillist":list}
    #return HttpResponse(list)
    return render(request,'myadmin/detail/index.html',context)

# 执行订单详情删除
def detaildel(request,uid):
    try:
        ob = Detail.objects.get(id=uid)
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/info.html",context)

# 打开订单详情编辑
def detailedit(request,uid):
    try:
        ob = Detail.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"myadmin/detail/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
    return render(request,"myadmin/info.html",context)

# 执行订单详情编辑
def detailupdate(request,uid):
    try:
        ob = Detail.objects.get(id=uid)
        ob.orderid = request.POST['orderid']
        ob.goodsid = request.POST['goodsid']
        ob.name = request.POST['name']
        ob.price = request.POST['price']
        ob.num = request.POST['num']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myadmin/info.html",context)
