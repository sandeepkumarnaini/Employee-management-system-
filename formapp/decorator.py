from django.shortcuts import redirect

def checksuperuser(fun):
    def innerfun(request,eno):
        if request.user.is_superuser==True:
            return fun(request,eno)
        else:
            return redirect('selecturl',pno=1)
    return innerfun