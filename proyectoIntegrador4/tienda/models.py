from django.db import models

class pais(models.Model):
    cod_pais = models.IntegerField(primary_key=True)
    pais = models.CharField(max_length=14)

    def __str__(self):
        return self.pais

class ciudad(models.Model):
    cod_ciud = models.IntegerField(primary_key=True)
    ciudad = models.CharField(max_length=30)
    cod_pais = models.ForeignKey('pais', on_delete=models.CASCADE)

    def __str__(self):
        return self.ciudad

class usuario(models.Model):
    cod_user = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=30)
    clave = models.CharField(max_length=30)
    correo = models.EmailField(max_length=30)
    cod_ciud = models.ForeignKey('ciudad', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    compañia = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    fec_nac = models.DateField('Fecha de nacimiento')

    ACTIVO = 'A'
    INACTIVO = 'X'
    estado_choices = [(ACTIVO, 'Activo'), (INACTIVO, 'Inactivo')]
    estado = models.CharField(max_length=2,choices=estado_choices)

    def __str__(self):
        return self.usuario

class tipo_proveedor(models.Model):
    cod_tipo_prov = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class proveedor(models.Model):
    cod_prov = models.IntegerField(primary_key=True)
    proveedor = models.CharField(max_length=50)
    ruc = models.IntegerField()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField(max_length=30)
    empresa = models.CharField(max_length=50)
    cod_tipo_prov = models.ForeignKey('tipo_proveedor', on_delete=models.CASCADE)
    cod_ciud = models.ForeignKey('ciudad', on_delete=models.CASCADE)
    
    ACTIVO = 'A'
    INACTIVO = 'X'
    estado_choices = [(ACTIVO, 'Activo'), (INACTIVO, 'Inactivo')]
    estado = models.CharField(max_length=2,choices=estado_choices)

    def __str__(self):
        return self.proveedor

class categoria_producto(models.Model):
    cod_cat = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=90)

    def __str__(self):
        return self.categoria

class producto(models.Model):
    cod_prod = models.IntegerField(primary_key=True)
    producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=90)
    cod_cat = models.ForeignKey('categoria_producto', on_delete=models.CASCADE)
    precio = models.IntegerField()
    stock = models.IntegerField()
    cod_prov = models.ForeignKey('proveedor', on_delete=models.CASCADE)
    
    ACTIVO = 'A'
    INACTIVO = 'X'
    estado_choices = [(ACTIVO, 'Activo'), (INACTIVO, 'Inactivo')]
    estado = models.CharField(max_length=2,choices=estado_choices)

    def __str__(self):
        return self.producto

class compra(models.Model):
    cod_compra = models.IntegerField(primary_key=True)
    cod_user = models.ForeignKey('usuario', on_delete=models.CASCADE)
    cod_prod = models.ManyToManyField(producto)
    fecha_compra = models.DateField()
    precio_total = models.IntegerField()

    def __str__(self):
        return '%s' % self.cod_compra