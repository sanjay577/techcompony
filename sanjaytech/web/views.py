
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import techSerializer
from .models import tech

#def Index(request):
   # return HttpResponse("Sanjaytech")


@api_view(['GET'])
# Create your views here.
def techOverview(request):
    web_urls ={
        'List':'/tech-list/',
        'Detail View':'/tech-detail/<int:id>/',
        'Create':'tech-create',
        'Update':'/tech-update/<int:id>',
        'Delete':'/tech-delete/<int:id>',

    }
    return Response(web_urls);
@api_view(['GET'])
@permission_classes([AllowAny])
def ShowAll(request):
    tech = tech.objects.all()
    serializer = techSerializer(tech, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Viewtech(request, pk):
    tech = tech.objects.get(id=pk)
    serializer = techSerializer(tech, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Createtech(request):
    serializer = techSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updatetech(request, pk):
    tech = tech.objects.get(id=pk)
    serializer = techSerializer(instance=tech, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deletetech(request, pk):
    tech = tech.objects.get(id=pk)
    tech.delete()

    return Response('Items delete successfully!')

