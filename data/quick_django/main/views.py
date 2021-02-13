from django.shortcuts import render
from django.http import HttpResponse


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