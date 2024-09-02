import json
from django.shortcuts import render
from django.http import JsonResponse


from .models import Car,User
from django.forms import model_to_dict

# Create your views here.

def create_car_data(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        car_name = data.get('car_name')
        try:
            speed = int(data.get('speed', 50))
        except ValueError:
            return JsonResponse({'error': 'Speed must be an integer'}, status=400)
        
        car = Car.objects.create(car_name=car_name, speed=speed)
        car_dict = model_to_dict(car)
        return JsonResponse(car_dict, status=201)

    
def read_data(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        cars_list = [model_to_dict(car) for car in cars]
        return JsonResponse(cars_list, safe=False)
    

def update_data(request,car_id):

    if request.method=='PUT':
        try:
            car=Car.objects.get(id=car_id)
            data=json.loads(request.body)

            car.car_name=data.get("car_anme",car.car_name)
            car.speed=int(data.get("speed",car.speed))

            car.save()

            return JsonResponse(model_to_dict(car))
        except Car.DoesNotExist:
            return JsonResponse({'error': 'Car not found'}, status=404)
        except ValueError:
            return JsonResponse({'error': 'speed must be an integer'}, status=400)
    else:
        return JsonResponse({'error': 'method not allowed'}, status=405)



def delete_data(request, car_id):

    if request.method == 'DELETE':
        try:
            cars=Car.objects.filter(id=car_id)
            if cars.exists:
                cars.delete()

            return JsonResponse({'message': 'Car deleted successfully'}, status=400)

        except Car.DoesNotExist:
            return JsonResponse({'error': 'Car not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



def create_user_data(request):

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_name = str(data.get("user_name"))
            booking_car_id = int(data.get("booking_car"))

            booking_car = Car.objects.get(id=booking_car_id)
            
            user = User.objects.create(user_name=user_name, booking_car=booking_car)
            user_dict = model_to_dict(user)

            return JsonResponse(user_dict, status=201)
        
        except Car.DoesNotExist:
            return JsonResponse({'error': 'Car not found'}, status=404)
        except KeyError as e:
            return JsonResponse({'error': f'Missing field: {str(e)}'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



def read_user(request):

    if request.method=='GET':
        users=User.objects.all()
        user_list=[model_to_dict(user) for user in users]

        return JsonResponse(user_list,safe=False)


def update_user_data(request, booking_id):

    if request.method == 'PUT':
        try:
            user = User.objects.get(id=booking_id)
            data = json.loads(request.body)

            user.user_name=data.get("user_name",user.user_name)
            booking_cars=Car.objects.get(id=int(data["booking_car"]))
            user.booking_car=booking_cars

            user.save()
            return JsonResponse(model_to_dict(user))
        
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except ValueError:
            return JsonResponse({'error':'booking id should intiger'},status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    

def delete_user_data(request,user_id):

    if request.method=='DELETE':
        try:
            users=User.objects.filter(id=user_id)
            if users.exists:
                users.delete()

            return JsonResponse({'message':'user deleted successfully'},status=404)
        except User.DoesNotExist:
            return JsonResponse({'error':'user does not exist'})
        
    else:
        return JsonResponse({'error':'method not allowed'})

