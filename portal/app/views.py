from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from .models import User, Workflow, WFLog
import re
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def Index(request):
    if not request.session.keys():
        return render(request, 'pages/login.html', {"title" : "Login"})    
    return render(request, 'pages/dashboard.html', {"title" : "Dashboard", "valid":"", "user":request.session['user']})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            email = request.POST.get("email")
            password = request.POST.get("pass")
            user = User.objects.get(email=email, password=password)
            request.session['user'] = user.name
            return HttpResponse(json.dumps({"success":True}))
        except:
            return HttpResponse(json.dumps({"success":False}))
        # user = User.objects.get(email=userCred['email'], password=userCred['password'])
        
@csrf_exempt
def add_new(request):
    if request.method == 'GET':
        return render(request, 'pages/new_workflow.html', {"title": "Add New", "user":request.session['user']})
    else:
        try:
            name = request.POST.get("name")
            desc = request.POST.get("desc")
            approver = request.POST.get("approver")

            # created_by = User.objects.get(name=request.session['user'])
            created_by = cache.get_or_set(request.session['user'], User.objects.get(name=request.session['user']))
            approved_by = cache.get_or_set(approver, User.objects.get(name=approver))
            # approved_by = User.objects.get(name=approver)
            workflow = Workflow(name=name, description=desc, created_by=created_by, approver=approved_by)
            workflow.save()

            wf = Workflow.objects.latest('id')
            wf_log = WFLog(wf_id=wf, activity="CREATED")
            wf_log.save()
            return JsonResponse([{"success":True, "id":wf.id}], safe=False)
        except:
            return JsonResponse([{"success": False}], safe=False)

def valid_data(request):
    approver = cache.get_or_set(request.session['user'], User.objects.get(name=request.session['user']))
    # approver = User.objects.get(name=request.session['user'])
    datas = Workflow.objects.filter(approver=approver, status__in=["created", "modified", "rejected", "approved"]).values('id','name', 'description', 'status', 'date', 'created_by')
    data_list = []
    if datas:
        for data in datas:
            data['created_by'] = (User.objects.get(id=data['created_by'])).name
            data_list.append(data)

    return render(request, 'pages/valid_data.html', {"title" : "Valid Data", "data_list": data_list, "user":request.session['user']})

def invalid_data(request):
    creator = cache.get_or_set(request.session['user'], User.objects.get(name=request.session['user']))
    # creator = User.objects.get(name=request.session['user'])
    datas = Workflow.objects.filter(created_by=creator).values('id', 'name', 'description', 'status', 'date')
    data_list = []
    if datas:
        for data in datas:
            data_list.append(data)

    return render(request, 'pages/invalid_data.html', {"title" : "Invalid Data", "data_list": data_list, "user":request.session['user']})

@csrf_exempt
def update_status(request):
    try:
        wf = Workflow.objects.get(pk=request.POST.get('id'))
        wf.status = request.POST.get('val')
        wf.save()

        wflog = WFLog(wf_id=wf, activity=(request.POST.get('val')).upper())
        wflog.save()

        return JsonResponse([{"success":True}], safe=False)
    except:
        return JsonResponse([{"success":False}], safe=False)

@csrf_exempt
def get_wf_log(request):
    wf_id = Workflow.objects.get(pk=request.POST.get('id'))
    wf_log = WFLog.objects.filter(wf_id=wf_id).order_by('id').values('activity', 'date')
    wf_list = []
    if wf_log:
        for wf in wf_log:
            wf_list.append(wf)
            print(wf)
            
    return JsonResponse([{"success":True, "data":wf_list}], safe=False)

@csrf_exempt
def logout(request):
    try:
        del request.session['user']
        return JsonResponse([{"success": True}], safe=False)
    except:
        return JsonResponse([{"success": False}], safe=False)
