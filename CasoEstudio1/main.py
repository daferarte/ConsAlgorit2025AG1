from Empleado import Empleado

empleado1 = Empleado('Pepito', 'Perez', 1, 100000)
empleado2 = Empleado('Martina', 'Nieves', 2, 200000)

print(f'El salario del empleado {empleado1.nombre} es: {empleado1.DarSalario()}')
print(f'El salario del empleado {empleado2.nombre} es: {empleado2.DarSalario()}')

print(f'El empleado debe pagar impuestos con valor de: {empleado1.CalcularImpuestos()} para el salario anual de: {empleado1.CalcularSalarioAnual()}')

empleado1.CambiarSalario(150000)
print(f'El nuevo salario del empleado es: {empleado1.DarSalario()}')
print(f'El empleado debe pagar impuestos con valor de: {empleado1.CalcularImpuestos()} para el salario anual de: {empleado1.CalcularSalarioAnual()}')

