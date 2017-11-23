from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from myadmin.models import Orders
import time,json

def index(request):
    return render(request,"myadmin/index.html")

#订单列表
#浏览订单
def ordersindex(request):
    # 执行数据查询，并放置到模板中
    list = Orders.objects.all()
    context = {"orderslist":list}
    #return HttpResponse(list)
    return render(request,'myadmin/orders/index.html',context)
# 执行订单信息删除
def ordersdel(request,uid):
    try:
        ob = Orders.objects.get(id=uid)
        ob.delete()
        context = {'info':'删除成功！'}
    except:
        context = {'info':'删除失败！'}
    return render(request,"myadmin/info.html",context)

# 打开会员信息编辑表单
def ordersedit(request,uid):
    try:
        ob = Orders.objects.get(id=uid)
        context = {'user':ob}
        return render(request,"myadmin/orders/edit.html",context)
    except:
        context = {'info':'没有找到要修改的信息！'}
    return render(request,"myadmin/info.html",context)

# 执行会员信息编辑
def ordersupdate(request,uid):
    try:
        ob = Orders.objects.get(id=uid)
        ob.linkman = request.POST['linkman']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.total = request.POST['total']
        ob.status = request.POST['status']
        ob.save()
        context = {'info':'修改成功！'}
    except:
        context = {'info':'修改失败！'}
    return render(request,"myadmin/info.html",context)

