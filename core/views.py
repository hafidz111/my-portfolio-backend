from rest_framework import viewsets
from .models import Profile, About, Certification, Education, Skill, Project
from .serializers import ProfileSerializer, AboutSerializer, CertificationSerializer, EducationSerializer, SkillSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import JsonResponse
import os
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json
import traceback

def home(request):
    return JsonResponse({'message': 'Welcome to Portfolio API'})

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not name or not email or not message:
                return JsonResponse({'error': 'All fields are required'}, status=400)

            subject = f"Pesan dari {name} ({email})"
            full_message = f"From: {name}\nEmail: {email}\n\n{message}"

            send_mail(
                subject,
                full_message,
                os.getenv('EMAIL_HOST_USER'),
                [os.getenv('EMAIL_HOST_USER')],
                fail_silently=False,
            )

            return JsonResponse({'success': True, 'message': 'Message sent successfully'})
        except Exception as e:
            print(traceback.format_exc())
            return JsonResponse({'success': False, 'message': 'Failed to sent', 'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)
