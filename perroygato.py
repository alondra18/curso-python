

class mascota(object):

	def __init__(self, animal1, animal2, edad='son bellos'):
		self.animal1= perro
		self.animal2= gato
		self.edad = edad

	def obtener_nombre(self):
		print 'Dentro de clase base'
		return '{perro} {gato} {edad}'.format(

           animal1=self.animal1,
           animal2=self.animal2
           
        )

class perro(mascota):
	def __init__(self, animal1, come_gatos):
   mascota.__init__(self, animal1, "perro")
   self.come_gatos = come_gatos
   

	def come_gatos(self):
		return self.come_gatos

class gato(mascota, perro):
   
    def __init__(self, animal2, mata_perros):
   mascota.__init__(self, animal2, "gato")
   self.mata_perros = mata_perros

   def mata_perros(self):
		return self.mata_perros








