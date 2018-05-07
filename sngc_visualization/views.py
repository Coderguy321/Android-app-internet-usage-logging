# import datetime
# import json
# from django.views import View
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from .models import User
#
# from .models import AppLogs
# from django.http import JsonResponse
# from django.utils.crypto import get_random_string
# from datetime import timedelta
# from django.db.models import Sum, Count, Max, Avg
#
#
#
# class Testing(View):
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(SngcVisualisationView, self).dispatch(request, *args, **kwargs)
#
#     def post(self, request):
#         data = request.POST
#         app_name = data.get('appName')
#         first_timestamp = data.get('firstTimeStamp')
#         last_timestamp = data.get('lastTimeStamp')
#         last_time_used = data.get('lastTimeUsed')
#         total_foreground_time_epoch = data.get('totalTimeInForeground')
#         total_foreground_time = datetime.datetime.fromtimestamp(int(total_foreground_time_epoch)).strftime('%Y-%m-%d %H:%M:%S')
#         model_obj = AppLogs.objects.create(app_name=app_name,first_timestamp=first_timestamp,last_timestamp=last_timestamp,
#                         last_time_used=last_time_used, total_foreground_time=total_foreground_time)
#         return JsonResponse({'success':True})
#
#     def get(self, request, *args, **kwargs):
#         data = json.loads(request.body.decode("UTF-8"))
#         div_id = data.get('deviceId')
#         unique_id = get_random_string(length=10)
#         user = User.objects.get(device_id=div_id)
#         if not User.objects.filter(device_id=div_id):
#             User.objects.create(device_id=div_id, unique_id=unique_id)
#         complete_data = User.objects.get(id=user.id)
#         result = []
#         for data in complete_data:
#             result.append({"values": data.values, "label": data.label})
#
#         return JsonResponse({'data': result})
#
#
#
# class SngcVisualisationView(View):
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(SngcVisualisationView, self).dispatch(request, *args, **kwargs)
#
#     def post(self, request):
#         data = json.loads(request.body.decode("UTF-8"))
#         div_id = data.get('deviceId')
#         unique_id = get_random_string(length=10)
#         if not User.objects.filter(device_id=div_id):
#             User.objects.create(device_id = div_id, unique_id = unique_id)
#
#         user = User.objects.get(device_id=div_id)
#         app_name = data.get('appName')
#         first_timestamp_epoch = int(data.get('firstTimestamp'))/1000
#         last_timestamp_epoch = int(data.get('lastTimestamp'))/1000
#         last_time_used_epoch = int(data.get('lastTimeUsed'))/1000
#         total_foreground_time = int(data.get('totalTimeInForeground'))/1000
#
#         first_timestamp = datetime.datetime.fromtimestamp(int(first_timestamp_epoch)).strftime('%Y-%m-%d %H:%M:%S')
#         last_timestamp =  datetime.datetime.fromtimestamp(int(last_timestamp_epoch)).strftime('%Y-%m-%d %H:%M:%S')
#         last_time_used = datetime.datetime.fromtimestamp(int(last_time_used_epoch)).strftime('%Y-%m-%d %H:%M:%S')
#         last_time_used_datetime = datetime.datetime.fromtimestamp(int(last_time_used_epoch))
#
#         try:
#             last_app_log_entry = AppLogs.objects.filter(user=user.id, app_name=app_name).last()
#             if last_app_log_entry.last_timestamp.date() == last_time_used_datetime.date:
#                 last_app_log_entry.last_timestamp = last_timestamp
#                 last_app_log_entry.save()
#         except Exception as e:
#             model_obj = AppLogs.objects.create(app_name=app_name,first_timestamp=first_timestamp,last_timestamp=last_timestamp,
#                         last_time_used=last_time_used, total_foreground_time=total_foreground_time, user = user)
#
#         return JsonResponse({'success': True})
#
#     def get(self, request, *args, **kwargs):
#             data = request.GET
#             # data = json.loads(request.body.decode("UTF-8"))
#             div_id = data.get('device_id')  # unique
#             previous_datetime = datetime.datetime.today() - timedelta(days=1)
#             user_id = User.objects.get(unique_id=div_id).id
#             today_applogs = AppLogs.objects.filter(user=user_id, last_timestamp__gte=previous_datetime)
#             result = []
#             for applog in today_applogs:
#                 result.append(
#                     {"app_name": applog.app_name, "duration": applog.total_foreground_time, 'time_label': 's'})
#
#             return JsonResponse({'result': result})
#
#
# class CurrentDateView(View):
#     def get(self, request, *args, **kwargs):
#             data = request.GET
#             # data = json.loads(request.body.decode("UTF-8"))
#             div_id = data.get('device_id')  # unique
#             previous_datetime = datetime.datetime.today()
#             current_date_midnight = datetime.datetime(previous_datetime.year, previous_datetime.month, previous_datetime.day, 0,0,0,0);
#             print(current_date_midnight)
#             user_id = User.objects.get(unique_id=div_id).id
#             today_applogs = AppLogs.objects.filter(user=user_id, last_timestamp__gte=current_date_midnight)
#             result = []
#             for applog in today_applogs:
#                 result.append(
#                     {"label": applog.app_name, "value": applog.total_foreground_time})
#
#             return JsonResponse({'result': result})
#
# class TotalTimeView(View):
#     def get(self, request, *args, **kwargs):
#             data = request.GET
#             # data = json.loads(request.body.decode("UTF-8"))
#             div_id = data.get('device_id')  # unique
#             user_id = User.objects.get(unique_id=div_id).id
#             top5_applogs = AppLogs.objects.values('app_name').annotate(total_time=Sum('total_foreground_time')).order_by('-total_time')[:10]
#             result = []
#             for applog in top5_applogs:
#                 print(applog)
#                 result.append(
#                     {"label": applog['app_name'], "value": applog['total_time']})
#
#             return JsonResponse({'result': result})
#
# class WeeklyView(View):
#     def get(self, request, *args, **kwargs):
#             data = request.GET
#             # data = json.loads(request.body.decode("UTF-8"))
#             div_id = data.get('device_id')  # unique
#             user_id = User.objects.get(unique_id=div_id).id
#             weeks_before = 1
#             start_date = datetime.datetime.today() - timedelta(days=(7 * 4 + 1))
#             end_date = datetime.datetime.today() - timedelta(days=7*4)
#             result = {}
#             for week in range(1,5):
#                 start_date = end_date
#                 end_date = end_date + timedelta(days=7)
#
#                 top5_applogs = AppLogs.objects.filter(last_timestamp__gte=start_date, last_timestamp__lte=end_date
#                              ).values('app_name'
#                              ).annotate(total_time=Sum('total_foreground_time')
#                              ).order_by('-total_time')[:5]
#
#                 diff_apps_single_week = []
#                 for applog in top5_applogs:
#                     diff_apps_single_week.append(
#                         {"app_name": applog['app_name'], "duration": applog['total_time']})
#                 result['weeks'+str(weeks_before)] = diff_apps_single_week
#                 weeks_before += 1
#
#             return JsonResponse({'result': result})
#
# class MostUsedView(View):
#     def get(self, request, *args, **kwargs):
#             data = request.GET
#             # data = json.loads(request.body.decode("UTF-8"))
#             div_id = data.get('device_id')  # unique
#             user_id = User.objects.get(unique_id=div_id).id
#
#             max_applog = AppLogs.objects.filter(
#                 user=user_id).values(
#                 'app_name').annotate(
#                 total_time=Sum('total_foreground_time')
#             ).order_by('-total_time').first()
#             return JsonResponse({'result': {'label':max_applog['app_name'],'value':max_applog['total_time']}})
#
# class LeastUsedView(View):
#     def get(self, request, *args, **kwargs):
#             data = request.GET
#             # data = json.loads(request.body.decode("UTF-8"))
#             div_id = data.get('device_id')  # unique
#             user_id = User.objects.get(unique_id=div_id).id
#
#             min_applog = AppLogs.objects.filter(
#                 user=user_id).values(
#                 'app_name').annotate(
#                 total_time=Sum('total_foreground_time')
#             ).order_by('total_time').first()
#             return JsonResponse({'result': {'label':min_applog['app_name'],'value':min_applog['total_time']}})
#
# class Last7DaysView(View):
#     def get(self, request, *args, **kwargs):
#         data = request.GET
#         # data = json.loads(request.body.decode("UTF-8"))
#         div_id = data.get('device_id')  # unique
#         user_id = User.objects.get(unique_id=div_id).id
#
#         start_date = datetime.datetime.today() - timedelta(days=(7 ))
#         top5_applogs = AppLogs.objects.filter(
#             last_timestamp__gte=start_date).values(
#             'app_name').annotate(
#             sum_time = Sum('total_foreground_time'))[:10]
#         result = []
#         for applog in top5_applogs:
#             result.append(
#                 {"label": applog['app_name'], "value": applog['sum_time']})
#
#         return JsonResponse({'result':result})
#
# class MostUsedAllUsersView(View):
#     def get(self, request, *args, **kwargs):
#             # data = request.GET
#             # data = json.loads(request.body.decode("UTF-8"))
#             max_applog = AppLogs.objects.values(
#                 'app_name').annotate(
#                 total_time=Sum('total_foreground_time')
#             ).order_by('-total_time').first()
#             return JsonResponse({'result': {'label':max_applog['app_name'],'value':max_applog['total_time']}})
#
# class MinUsedAllUsersView(View):
#     def get(self, request, *args, **kwargs):
#             # data = request.GET
#             # data = json.loads(request.body.decode("UTF-8"))
#             min_applog = AppLogs.objects.values(
#                 'app_name').annotate(
#                 total_time=Sum('total_foreground_time')
#             ).order_by('total_time').first()
#             return JsonResponse({'result': {'label':min_applog['app_name'],'value':min_applog['total_time']}})
#
# class ActiveUsersLast7View(View):
#     def get(self, request, *args, **kwargs):
#         start_date = datetime.datetime.today() - timedelta(days=30)
#         result = []
#         data = AppLogs.objects.filter(
#             last_timestamp__gte=start_date).values(
#             'user__unique_id','app_name').annotate(
#             sum_time=Sum('total_foreground_time'))
#
#         for d in data:
#             result.append({'user':d['user__unique_id'], 'app_name':d['app_name'], 'time':d['sum_time']})
#         return JsonResponse({'result':result})