from django.shortcuts import render
from django.views import View
from .models import Localizacion
import json
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class LocalizacionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if(id>0):
            #Filtrar por persona
            localizaciones=list(Localizacion.objects.filter(id=id).values())
            if len(localizaciones)>0:
                localizacion=localizaciones[0]
                datos={'message':"Success", 'code':"200",'localizacion':localizacion}
            else:
                datos={'message':"Localizaciones not found ..."}
            return JsonResponse(datos)
        else:
            localizaciones=list(Localizacion.objects.values())
            if len(localizaciones)>0:
                datos={'message':"Success", 'code':"200",'localizaciones':localizaciones}
            else:
                datos={'message':"Localizaciones not found ..."}
            return JsonResponse(datos)  

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Localizacion.objects.create(title=jd['title'],description=jd['description'],urlimagen=jd['urlimagen'],
        date=jd['date'],urlmapa=jd['urlmapa'])
        datos= {'message':"Success"}
        return JsonResponse(datos)


    def put(self, request,id):
        jd=json.loads(request.body)
        localizaciones=list(Localizacion.objects.filter(id=id).values())
        if len(localizaciones)>0:
            localizacion=Localizacion.objects.get(id=id)
            localizacion.title=jd['title']
            localizacion.description=jd['description']
            localizacion.urlimagen=jd['urlimagen']
            localizacion.date=jd['date']
            localizacion.urlmapa=jd['urlmapa']
            localizacion.save()
            datos={'message':"Success"}
        else:
            datos={'message':"Localizaciones not found ..."}
        return JsonResponse(datos)

    def delete(self, request,id):
        localizaciones=list(Localizacion.objects.filter(id=id).values())
        if len(localizaciones)>0:
            Localizacion.objects.filter(id=id).delete()
            datos={'message':"Localizacion Eliminada"}
        else:
            datos={'message':"Localizaciones not found ..."}
        return JsonResponse(datos)
            
        


