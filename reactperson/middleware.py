
import datetime
from django.http import JsonResponse


class TimeOutReloginMiddleware(object):
    # 所有请求之前触发
    def process_view(self, request, view_func, *args, **kwargs):
        # print(request.path)
        try:
            loginTime = request.session.get('loginTime')
            if loginTime:
                access_end = datetime.datetime.now()
                # access_end_str = access_end.strftime('%Y-%m-%d %H:%M:%S')
                # lastActiveTime = access_end_str
                print('yyy')
                # print(loginTime)

                '''
                2019-04-08 10:04:35

                '''
                timeStr = loginTime
                year_hour = timeStr.split(' ')
                timeY = year_hour[0].split('-')
                timeH = year_hour[1].split(':')
                a, b, c = timeY
                d, e, f = timeH
                a = int(a)
                b = int(b)
                c = int(c)
                d = int(d)
                e = int(e)
                f = int(f)
                # print(strY)
                firstTime = datetime.datetime(a, b, c, d, e, f)
                print((access_end - firstTime).seconds)

                if (access_end - firstTime).seconds > 3600:
                    request.session['isLogin'] = False
                    if request.path!='/login':
                        return JsonResponse({'code': 200, 'message': '请重新登录', 'pathname': '/login'})
                else:
                    access_start = datetime.datetime.now()
                    access_start_str = access_start.strftime('%Y-%m-%d %H:%M:%S')
                    request.session['loginTime'] = access_start_str
        except Exception as e:
            print('rrr')
            print(request.session.get('loginTime'))
            #print('pp', (lastActiveTime - loginTime).seconds)
            pass








