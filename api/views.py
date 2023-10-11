from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from crud.models import Student,  StudentProfile, ClassRoom


from .serializers import ClassRoomSerializer, ClassRoomModelSerializer, StudentModelSerializer, StudentProfileModelSerializer

def hello_world(request):
    response = {
        "message": "Hello World. I'm learning API"
    }

    return JsonResponse(response)


class HelloWorldView(APIView):
      def get(self, *args, **kwargs):
           
         response = {
            "message": "Hello Worldcfrom APIView"
    }
         return Response(response)

class studentView(APIView):
    def get(self, *args, **kwargs):
        student=[
            {"name": "Harke" , "age":30, "address": "KTM"},
            {"name": "Ram", "age": 40, "address": "PKR"}
        ]
        return Response(student)
    
class StudentFromDBView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs["id"]
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({
                "detail": "Invalid Student ID"
            }, status=status.HTTP_400_BAD_REQUEST)
        response = {
            "name":student.name,"age": student.age, "email": student.email, "classroom": student.classroom.name 
            
        }
        return Response(response)
    
class StudentFromDBListView(APIView):
    def get(self, *args, **kwargs):
        students  =Student.objects.all()
        response = []
        for student in students:
            data = {
            "name":student.name,"age": student.age, "email": student.email, "classroom": student.classroom.name
         }
            response.append(data)
        return Response(response)
    def post(self, *args , **kwargs):
        print(self.request.data)
        name = self.request.data.get("name")
        email = self.request.data.get("email")
        age = self.request.data.get("age")
        classroom = self.request.data.get("classroom")
        Student.objects.create(name=name, email=email, age=age, classroom_id=classroom)
        return Response({
            "detail": "Student Created Sucessfully !!"
        }, status=status.HTTP_201_CREATED)
    
class ProfileFromDBListView(APIView):
    def get(self, *args, **kwargs):
        students = StudentProfile.objects.all()
        response = []
        for student in students :
            data = {
                "student": student.student.name,
                "contact": student.contact,
                "address": student.address,
                "pp": student.profile_picture.url if student.profile_picture else None
            }
            response.append(data)
        return Response(response) 

class ClassroomFromDBView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs["id"]
        try:
             classroom = ClassRoom.objects.get(id=id)
        except ClassRoom.DoesNotExist:
            return Response({
                "detail": "Invalid ClassRoom Id!"
            }, status=status.HTTP_400_BAD_REQUEST)
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)


class ClassRoomFromDBListView(APIView):
    def get(self, *args , **kwargs):
        classrooms = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classrooms, many=True)
        return Response (serializer.data)
    
    def post(self, *args, **kwargs):
        serializer = ClassRoomSerializer(data = self.request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            ClassRoom.objects.create(name=name)
            return Response({
                "detail": "ClassRoom Created Sucessfully !! "
            }, status=status.HTTP_201_CREATED)
        return Response({
            "detail": "Invalid Request Data !!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetailView(APIView):
    def get(self, *args, ** kwargs):
        id = kwargs["id"]
        try:
            student = Student.objects.get(id = id)
        except Student.DoesNotExist:
            return Response({
                "detail": "Invalid Student ID"
            }, status=status.HTTP_400_BAD_REQUEST)
            
        serializers = StudentModelSerializer(student)
        return Response(serializers.data)
    
class StudentListView(APIView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many = True, context={"request": self.request})
        return Response(serializer.data)

    def post (self, *args , **kwargs):
        serializer = StudentModelSerializer(data = self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "detail": "Student Added Sucessfully"
            }, status=status.HTTP_201_CREATED)
        return Response({
            "detail": "Invalid request data"
        }, status=status.HTTP_400_BAD_REQUEST)

class StudentProfileListView(APIView): 
        def get(self, request, *args, **kwargs):
            students = StudentProfile.objects.all()
            serializer = StudentProfileModelSerializer(students, many = True, context={"request": request})
            return Response(serializer.data)
        
        def post(self, *args, **kwargs):
            serializer = StudentProfileModelSerializer(data = self.request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                    "detail" : "Student Profile Created Sucessfully"
                }, status=status.HTTP_201_CREATED)

class ClassRoomAPIView(ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer



class ClassRoomCreateAPIView(CreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomUpdateAPIView(UpdateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomDetailAPIView(RetrieveAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer


class ClassRoomDeleteAPIView(DestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    
    




        