from django.shortcuts import render
from django.http import HttpRequest
from Formun.forms import MyForm
from Formun.models import Article
from Formun.forms import AddArticle
from django.contrib.auth.decorators import login_required

def Formun(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'FormunIndex.html')


def Search(request):
    search = request.POST.get('search')
    list = Article.objects.filter(Title__icontains=search)
    return render(request,"List.html",locals())


def List(request):
    try:
        list = Article.objects.all()
    except:
        errormessage = " ( 讀取錯誤! 或沒有權限) "
    return render(request, "List.html", locals())


def Content(request,pk):
    try:
        content = Article.objects.get(pk=pk)
    except:
        errormessage = " ( 讀取錯誤! 或沒有權限) "
    return render(request, "Content.html", locals())

@login_required(login_url='/signin/')
def Add(request):
    form = AddArticle()

    if request.method=="POST":
        Title = request.POST.get("Title")
        Content = request.POST.get("Content")
        CreateBy = request.POST.get("user")
        unit = Article.objects.create(Title=Title,Content=Content,CreateBy=CreateBy)
        unit.save()
        list = Article.objects.all().order_by('-pk')
        return render(request,"List.html",locals())

    context = {
        'form':form,
    }
    return render(request,'Add.html',context)

