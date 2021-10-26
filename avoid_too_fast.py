def avoidtoofast():
    try:
        oldtime = 0
        if session.get('time'):
            oldtime = session.get('time')
            print('oldtime',oldtime,type(oldtime))
        session['time'] = datetime.now()
        #time.sleep(0.5) 
        newtime = session.get('time')
        print('newtime',newtime,type(newtime))
        if oldtime != 0:
            time_delta = newtime - oldtime
            print('time_delta',session.get('time'))
            if time_delta < timedelta(seconds=2.7):
                if session.get('times'):
                    tmp = session.get('times')
                    session['times'] = tmp+1
                    if session.get('times')>25:#4
                        flash("您的操作太快了") 
                        session['times'] = 0
                        return 1
                else:
                    session['times'] = 1
                #time.sleep(2)
            else:
                session['times'] = 0
        return 0
    except:
        current_app.logger.error("Catch an exception in func.", exc_info=True)
        abort(500)
