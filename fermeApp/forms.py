from dataclasses import field, fields
from django import forms
from .models import Cliente, DetalleOrden, InvProducto, OfertaProd, OrdenCompra, Proveedor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistroCli(forms.ModelForm):

    contrasenia = forms.CharField(widget= forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ["nombre", "rut_cli", "p_apellido", "s_apellido", "email", "telefono", "usuario", "contrasenia", "pertenencia_emp"]

#Formulario registro usuarios
class NuevoUserCreationForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', "email", "password1", "password2"]

# FORMULARIOS EMPLEADO
class AddProducto(forms.ModelForm):
    
    class Meta:
        model = InvProducto
        fields = ['nombre', 'precio', "fecha_venc", "stock", "stock_crit", "stock_max","fam_producto_id_fam"]

class AddProveedor(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ["rut", "rubro", "celular", "domicilio"]

class AddOferta(forms.ModelForm):

    class Meta:
        model = OfertaProd
        fields = '__all__'

class AddOrden(forms.ModelForm):

    class Meta:
        model = OrdenCompra
        fields = '__all__'

class AddDetalleOrden(forms.ModelForm):

    class Meta:
        model = DetalleOrden
        fields = '__all__'