from rest_framework import serializers
from mascotar_app.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
    
    
    
    
    
    # def validate(self, data):
    #     if data['nombre'] ==data['descripcion']:
    #         raise serializers.ValidationError("La descripcion y el nombre debens er diferentes")
    #     else:
    #         return data        
    
    # def validate_linkImagen(self, data):
    #     if len(data) < 2:
    #         raise serializers.ValidationError("La url debe tener al menos 2 caracteres")
    #     else:
    #         return data


# def column_longitud(value):
#     if len(value) < 1:
#         raise serializers.ValidationError("El valor es demasiado corto")


# class ProductoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     nombre = serializers.CharField(validators=[column_longitud])
#     precio = serializers.IntegerField(validators=[column_longitud])
#     descripcion = serializers.CharField()
#     linkImagen = serializers.CharField()
    
#     def create(self, validated_data):
#         return Producto.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.nombre = validated_data.get('nombre', instance.nombre)
#         instance.precio = validated_data.get('precio', instance.precio)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.linkImagen = validated_data.get('linkImagen', instance.linkImagen)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['nombre'] ==data['descripcion']:
#             raise serializers.ValidationError("La descripcion y el nombre debens er diferentes")
#         else:
#             return data        
    
#     def validate_linkImagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError("La imagen debe tener al menos 2 caracteres")
#         else:
#             return data