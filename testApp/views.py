from django.shortcuts import render
from django.forms import *

from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.views import *
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.pagination import PageNumberPagination

from .recommendations import recommendation
import pandas as pd

from .serializers import *
from .models import *

# Create your views here.

# -------------------------------- CREATING DF WITH DB --------------------------------------------------------------
pytdfStr = pd.DataFrame(list(Checks.objects.all().values())).drop(columns=["id", "createtime"])

test_dict = []
for check in Checks.objects.all():
    for tovar in check.tovars.all():
        test_dict.append({"iddoc": check.iddoc, "idtov": tovar.idtov})
test_df = pd.DataFrame(test_dict)



pytdfStr = pd.merge(pytdfStr, test_df, on = "iddoc")   #for checks

pytnames = pd.DataFrame(list(Tovar.objects.all().values())).drop(columns=["id"]) # for tovars

del test_dict, test_df
# ---------------------------------------------------------------------------------------------------------------------




class TovarListPagination(PageNumberPagination):
    page_size = 15


# Заменяет все весь функционал ниже🔽 (get, post, put, delete)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Ограничения

    # Если хотим отредактировать выдачу базы данных (queryset ⬆️ уже необязателен)
    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Book.objects.all()[:3]

        # Не get(), потому что нужен список
        return Book.objects.filter(pk=pk)

    # Если мы хотим дополнительное url( ..api/v1/book/<pk>/author/ )

    @action(methods=["get"], detail=True)
    def author(self, request, pk=None):
        cats = Author.objects.get(pk=pk)
        return Response({"cats": cats.name})


# class TovarViewSet(viewsets.ModelViewSet):
#     queryset = Tovars.objects.all()
#     serializer_class = TovarSerializer
#     pagination_class = TovarListPagination     # Пагинация


class TovarApiView(APIView):
    dfStr = pytdfStr
    names = pytnames

    def get(self, request):
        return Response({"Error": "Only POST"})

    def post(self, request):
        checks_dict = request.data['tovars']

        #Проверка
        if not checks_dict:
            return Response({"recommendations": "Не получаю нормальный JSON!"})


        checks = pd.DataFrame(checks_dict) 
        id_tovars = pd.DataFrame(checks["idtov"], columns=["idtov"])
        checks.drop(columns=["idtov"])

        group_by_iddoc = checks.groupby(['iddoc'])
        check = group_by_iddoc.sum(numeric_only=True) 
        check['count_uniq_good'] = group_by_iddoc.size()
        check.index.name = None


        # Создаем рекомендации (return: dict)   max: 25
        recommended = []
        tryes = 0


        # При ошибке пытаемся 3 раза, потом сдаемся
        while not recommended:
            if tryes > 3:
                recommended = None
                break
            recommending = recommendation.Recommendation(dfStr=self.dfStr, names=self.names)
            recommended = recommending.get_recommendations(check, id_tovars)
            tryes += 1



        if recommended:
            for tovar in recommended:
                tovar["name"] = tovar["name"].replace("  ", '')
        else:
            recommended = "Непонятная ошибка! Проверьте входные данные! Либо товар непопулярен"


        return Response({"recommendations": recommended})











    #
    #
    #
    #
    # --------------------------------------------------------------------------------
    # class BookApiList(generics.ListCreateAPIView):
    #     queryset = Book.objects.all()
    #     serializer_class = BookSerializer
    # class BookApiUpdate(generics.UpdateAPIView):
    #     queryset = Book.objects.all()    # На самом деле выберется только 1 эл.
    #     serializer_class = BookSerializer
    # --------------------------------------------------------------------------------
    # class BookApiView(APIView):
    #     def get(self, request):
    #         lst = Book.objects.all()
    #         return Response({"posts": BookSerializer(lst, many=True).data})
    #     def post(self, request):
    #         serializer = BookSerializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response({"post": serializer.data})
    #     def put(self, request, *args, **kwargs):
    #         pk = kwargs.get('pk', None)
    #         if not pk:
    #             return Response({"error": "Method PUT is not allowed"})
    #         try:
    #             instance = Book.objects.get(pk=pk)
    #         except:
    #             return Response({"error": "Object does not exists"})
    #         serializer = BookSerializer(data=request.data, instance=instance)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response({"post": serializer.data})
    #     def delete(self, request, *args, **kwargs):
    #         pk = kwargs.get("pk", None)
    #         if not pk:
    #             return Response({"error": "Methon DELETE is not allowed"})
    #         try:
    #             Book.objects.get(pk=pk).delete()
    #         except:
    #             return Response({"error": "Incorrect ID of post"})
    #         return Response({"post": f"Post id={pk} has been deleted"})
