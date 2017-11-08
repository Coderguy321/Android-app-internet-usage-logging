import datetime
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import User

from .models import AppLogs
from django.http import JsonResponse
from django.utils.crypto import get_random_string

class Testing(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SngcVisualisationView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.POST
        app_name = data.get('appName')
        first_timestamp = data.get('firstTimeStamp')
        last_timestamp = data.get('lastTimeStamp')
        last_time_used = data.get('lastTimeUsed')
        total_foreground_time_epoch = data.get('totalTimeInForeground')
        total_foreground_time = datetime.datetime.fromtimestamp(int(total_foreground_time_epoch)).strftime('%Y-%m-%d %H:%M:%S')
        model_obj = AppLogs.objects.create(app_name=app_name,first_timestamp=first_timestamp,last_timestamp=last_timestamp,
                        last_time_used=last_time_used, total_foreground_time=total_foreground_time)
        return JsonResponse({'success':True})

    def get(self, request, *args, **kwargs):
        f ={
              "chart": {
                "caption": "App Usage Analysis",
                "subCaption": "",
                "xAxisName": "App",
                "yAxisName": "Usage Duration (in miliseconds)",
                "theme": "fint"
              },

                "data": [{
                "label": "Whatsapp",
                "value": "4009"
                }, {
                    "label": "Facebook",
                    "value": "3010"
                }, {
                    "label": "Instagram",
                    "value": "749"
                }, {
                    "label": "Zomato",
                    "value": "809"
                }, {
                    "label": "Quora",
                    "value": "1003"
                }, {
                    "label": "Camera",
                    "value": "501"
                }, {
                    "label": "Notes",
                    "value": "889"
                }, {
                    "label": "Ola",
                    "value": "1200"
                }, {
                    "label": "Uber",
                    "value": "978"
                }]

            }
        return JsonResponse(f)


class SngcVisualisationView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SngcVisualisationView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = json.loads(request.body.decode("UTF-8"))
        div_id = data.get('deviceId')
        unique_id = get_random_string(length=10)
        if not User.objects.filter(device_id=div_id):
            User.objects.create(device_id = div_id, unique_id = unique_id)

        user = User.objects.get(device_id=div_id)
        app_name = data.get('appName')
        first_timestamp = data.get('firstTimeStamp')
        last_timestamp_epoch = int(data.get('lastTimestamp'))/1000
        last_time_used_epoch = int(data.get('lastTimeUsed'))/1000
        total_foreground_time_epoch = int(data.get('totalTimeInForeground'))/1000
        last_timestamp =  datetime.datetime.fromtimestamp(int(last_timestamp_epoch)).strftime('%Y-%m-%d %H:%M:%S')
        last_time_used = datetime.datetime.fromtimestamp(int(last_time_used_epoch)).strftime('%Y-%m-%d %H:%M:%S')
        total_foreground_time = datetime.datetime.fromtimestamp(int(total_foreground_time_epoch)).strftime('%Y-%m-%d %H:%M:%S')
        print(app_name, total_foreground_time)
        model_obj = AppLogs.objects.create(app_name=app_name,first_timestamp=first_timestamp,last_timestamp=last_timestamp,
                        last_time_used=last_time_used, total_foreground_time=total_foreground_time, user = user)

        return JsonResponse({'success': True})


    def get(self, request, *args, **kwargs):
        data = request.GET
        authentication_token = data.get('key')
        id = None
        applog = None
        try:
            id = User.objects.get(unique_id = authentication_token)
        # todo: change the exception type to DoesNotExist exception
        except:
            print ("No entry in table for user_id: " + str(authentication_token))

        try:
            applogs = AppLogs.objects.filter(user=id)
        except:
            print ("No App logs for user_id: " + str(authentication_token))

        return JsonResponse({'data':
            [
              {
                  "label": "Whatsapp",
                  "value": "4009"
              },
              {
                  "label": "Facebook",
                  "value": "3010"
              },
              {
                  "label": "Instagram",
                  "value": "749"
              },
              {
                  "label": "Zomato",
                  "value": "809"
              },
              {
                  "label": "Quora",
                  "value": "1003"
              },
              {
                  "label": "Camera",
                  "value": "501"
              },
              {
                  "label": "Notes",
                  "value": "889"
              },
              {
                  "label": "Ola",
                  "value": "1200"
              },
              {
                  "label": "Uber",
                  "value": "978"
              }
            ]})

    def get(self, request, *args, **kwargs):
        data = request.GET
        unique_id = data.get('id')
        user_id = User.objects.get(unique_id = unique_id).id
        appLogs = AppLogs.objects.filter(user = user_id)

        result = []
        for entry in appLogs:
            value = entry.total_foreground_time
            label = entry.app_name
            result.append({"label": label,"value": value})
        return JsonResponse({"data": result})

