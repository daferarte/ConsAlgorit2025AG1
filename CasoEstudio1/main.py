from Empleado import Empleado

empleado1 = Empleado('Pepito', 'Perez', 1, 100000)
print(f'El salario del empleado es: {empleado1.DarSalario()}')

empleado1.CambiarSalario(150000)
print(f'El nuevo salario del empleado es: {empleado1.DarSalario()}')