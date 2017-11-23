from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from myweb.models import Types,Goods,Users
from django.core.urlresolvers import reverse
import time,json

def loadinfo():
	context={}
	context['type0list'] = Types.objects.filter(pid=0)
	return context
#网站首页
def shopindex(request):
	context = loadinfo()
	return render(request,"myweb/shopindex.html",context)

#商品列表页
def shoplist(request):
	context = loadinfo()
	list = Goods.objects.filter()
	if request.GET.get('tid','') != '':
		tid = str(request.GET.get('tid',''))
		list = list.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+tid+','))
	context['goodslist'] = list
	return render(request,"myweb/shoplist.html",context)
#商品详情页
def shopmeilanx(request,gid):
    context = loadinfo()
    ob = Goods.objects.get(id=gid)
    #累加点击量
    ob.clicknum += 1
    ob.save()
    context['goods'] = ob
    return render(request,"myweb/shopmeilanx.html",context)

# ==============后台管理员操作====================	
#会员登录
def shoplogin(request):
    return render(request,"myweb/shoplogin.html")
# 会员执行登录
def shopdologin(request):
    try:
        #根据账号获取登录者信息
        user = Users.objects.get(username=request.POST['username'])
        #判断当前用户是否是后台管理员用户
        if user.state == 0 or user.state == 1:
            # 验证密码
            import hashlib
            m = hashlib.md5() 
            m.update(bytes(request.POST['password'],encoding="utf8"))
            if user.password == m.hexdigest():
                # 此处登录成功，将当前登录信息放入到session中，并跳转页面
                request.session['vipuser'] = user.toDict()
                #print(json.dumps(user))
                return redirect(reverse('shopindex'))
            else:
                context = {'info':'登录密码错误！'}
        else:
            context = {'info':'此用户非会员用户！'}
    except:
        context = {'info':'登录账号错误！'}
    return render(request,"myweb/shoplogin.html",context)

# 会员退出
def shoplogout(request):
    # 清除登录的session信息
    del request.session['adminuser']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('shoplogin'))
    # 加载登录页面(url地址不变)
    # return render(request,"myweb/shopindex.html")
#会员注册
def shopregister(request):
    return render(request,"myweb/shopregister.html")
    
#执行会员信息添加    
def shopinsert(request):
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = '请输入用户名'
        #获取密码并md5
        import hashlib
        m = hashlib.md5() 
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.sex = 1
        ob.address = '北京'
        ob.code = 0
        ob.phone = 0
        ob.email = '150000'
        ob.state = 1
        ob.addtime = time.time()
        ob.save()
        context = {'info':'添加成功！'}
    except:
        context = {'info':'添加失败！'}

    return render(request,"myweb/shoplogin.html",context)





