import io
from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serializer.is_valid(raise_exception=True)
    json_data = JSONRenderer().render(serializer.data)
    return json_data


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer



# if __name__ == "__main__":
#     car_data = {
#         "manufacturer": "OPEL",
#         "model": "Vectra C",
#         "horse_powers": 120,
#         "is_broken": True,
#         "problem_description": "flat tire"
#     }
#     car = Car(**car_data)
#     print(car)
