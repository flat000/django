from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random

# Create your views here.
# a. リクエスト情報を受け取る
def index(request):
    # b.レスポンスを生成する
    return HttpResponse('こんにちは、世界!')


def temp(request):
    # a.ビュー変数を準備
    context = {
        'msg':'こんにちは、世界！'
    }
    #b.テンプレートを呼び出す
    return render(request, 'main/temp.html', context)

def list(request):
    # 全ての書籍情報を取得
    books = Book.objects.all()
    return render(request, 'main/list.html',{
        'books':books
    })

def iftag(request):
    return render(request, 'main/iftag.html',{
        # 0~100の乱数を生成
        'random':random.randint(0, 100)
    })

def yesno(request):
    return render(request, 'main/yesno.html',{
        'flag':True
    })

def firstof(request):
    return render(request, 'main/firstof.html',{
        #'a':'おはようございます!',
        #'b':'こんにちは!',
        #'c':'こんばんは!'
    })

def forloop(request):
    return render(request, 'main/forloop.html',{
        'weeks':['月', '火', '水', '木', '金', '土', '日']
    })

def forempty(request):
    return render(request, 'main/forempty.html', {
        'members':['鈴木三郎', '佐藤洋子', '山田次郎']
    })

def fortag(request):
    return render(request, 'main/fortag.html')

def ifchanged(request):
  return render(request, 'main/ifchanged.html', {
      'schedule': [
        (10, 'A企画反省会'),
        (10, 'B書籍脱稿'),
        (15, 'WINGS定例会議'),
        (30, 'C企画打ち合わせ'),
      ]
  })

def regroup(request):
    return render(request, 'main/regroup.html', {
        'members':[
            {'name':'鈴木三郎', 'sex':'男', 'birth':'1980-12-23'},
            {'name':'山田次郎', 'sex':'男', 'birth':'1978-10-13'},
            {'name':'佐藤健司', 'sex':'男', 'birth':'1976-04-06'},
            {'name':'山本花子', 'sex':'女', 'birth':'1981-07-28'},
            {'name':'田中久美', 'sex':'女', 'birth':'1980-09-07'},
        ]
    })

def cycle(request):
    return render(request, 'main/cycle.html', {
        'members':[
            {'name':'鈴木三郎', 'sex':'男', 'birth':'1980-12-23'},
            {'name':'山田次郎', 'sex':'男', 'birth':'1978-10-13'},
            {'name':'佐藤健司', 'sex':'男', 'birth':'1976-04-06'},
            {'name':'山本花子', 'sex':'女', 'birth':'1981-07-28'},
            {'name':'田中久美', 'sex':'女', 'birth':'1980-09-07'},
        ]
    })

def escape(request):
    return render(request, 'main/escape.html', {
        'msg':'''<img src="https://wings.msn.to/image/wings.jpg" title="ロゴ" /><p>WINGへようこそ</p>'''
    })

def temptag(request):
    return render(request, 'main/temptag.html')

def verbatim(request):
    return render(request, 'main/verbatim.html')