# base counter for total policy

def counter(request):
    # from django.contrib.auth.decorators import login_required
    from dashboard.models import Lic
    from account.models import register_table
    from django.contrib.auth.models import User
    from datetime import datetime, timedelta
    
    # @login_required
    if(request.user.id):
        # today=datetime.date.today()
        # print(today)
        
        context = {}
        data = register_table.objects.get(user__id=request.user.id)
        context["data"] = data

        
        user = User.objects.get(username = request.user)
        lics = Lic.objects.filter(user__pk=user.id)
        dues= Lic.objects.filter(user__pk=user.id,renew_date__range=[datetime.now().date(),datetime.now().date()+timedelta(days=7)],status=1).count()
        # dues= Lic.objects.filter(user__pk=user.id,renew_date__in=timedelta(days=7),status=1).count()
        active = Lic.objects.filter(user__pk=user.id,status=1).count()
        count = lics.count()
        return {
        'count':count,
        'active':active,
        'dues':dues,
        'data': data
        }
    return {}



# def image(request):

#     from dashboard.models import register_table

#     context = {}
#     check = register_table.objects.filter(user__id=request.user.id)
#     if len(check)>0:
#         data = register_table.objects.get(user__id=request.user.id)
#         context["data"] = data
#         return {
#         'context':context,
#         }
#     return {}  