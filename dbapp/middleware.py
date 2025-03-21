from django.core.exceptions import ValidationError

class Mymiddleware:
    def __init__(self,get_respons):
        self.get_response=get_respons
    def __call__(self,request):
        if request.method=='POST':
            if int(request.POST['sal'])>0:
                resp=self.get_response(request)
                return resp
            else:
                raise ValidationError('negative values are not allowed')
        else:
            resp=self.get_response(request)
            return resp
    
