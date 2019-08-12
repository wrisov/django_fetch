from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.views import APIView

#def register(request):
 #   if request.method == 'POST':
  #   form = UserCreationForm(request.POST)
  #   if form.is_valid():
   #     form.save()
    #    username=form.cleaned_data.get('username')
        #message.success(request, f'Account created!')
     #   return redirect('blog-home')
    #else:
     #    form = UserCreationForm()

    #return render(request,'users/register.html',{'form': form})


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)
 
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Create your views here.
