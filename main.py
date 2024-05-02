import init_django_orm  # noqa: F401

import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = JSONRenderer().render(serializer.data)
    return json_data


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


if __name__ == "__main__":
    car_data = {"manufacturer": "Audi", "model": "A4", "horse_powers": 200, "is_broken": True}

    print(car_data)

    serialized_data = serialize_car_object(car_data)
    print(serialized_data)

    deserialized_car = deserialize_car_object(serialized_data)
    print(deserialized_car)

    car_to_delete = Car.objects.get(pk=deserialized_car["id"])
    car_to_delete.delete()
