from ejercicio5.Habitacion import Habitacion
from ejercicio5.Vivienda import Vivienda
from ejercicio5.Barrio import Barrio


def main():

    barrio = Barrio(nombre="Barrio San Martín", empresa_constructora="Constructora Cuyo S.A.")

    v1 = Vivienda(calle="Av. San Martín", numero=123, manzana="A", nroCasa=1, superficie_terreno=300.0)
    v1.agregar_habitacion(Habitacion("Cocina/Comedor", 30.0))
    v1.agregar_habitacion(Habitacion("Dormitorio Principal", 20.0))
    v1.agregar_habitacion(Habitacion("Baño", 6.0))

    v2 = Vivienda(calle="Av. San Martín", numero=127, manzana="A", nroCasa=2, superficie_terreno=250.0)
    v2.agregar_habitacion(Habitacion("Living", 25.0))
    v2.agregar_habitacion(Habitacion("Dormitorio", 15.0))
    v2.agregar_habitacion(Habitacion("Baño", 5.0))

    v3 = Vivienda(calle="Calle Belgrano", numero=450, manzana="B", nroCasa=1, superficie_terreno=400.0)
    v3.agregar_habitacion(Habitacion("Estar", 40.0))
    v3.agregar_habitacion(Habitacion("Dormitorio 1", 18.0))
    v3.agregar_habitacion(Habitacion("Dormitorio 2", 18.0))
    v3.agregar_habitacion(Habitacion("Baño Suite", 10.0))

    barrio.agregar_vivienda(v1)
    barrio.agregar_vivienda(v2)
    barrio.agregar_vivienda(v3)

    print(f"=== REPORTE DE {barrio.nombre.upper()} ===")
    print(f"Empresa Constructora: {barrio.empresa_constructora}\n")

    total_terreno = barrio.get_superficie_total_terreno()
    print(f"a) Superficie Total de Terreno del Barrio: {total_terreno} m²")

    manzana_a = barrio.get_superficie_total_terreno_x_manzana("A")
    manzana_b = barrio.get_superficie_total_terreno_x_manzana("B")
    print(f"b) Superficie Terreno Manzana 'A': {manzana_a} m²")
    print(f"   Superficie Terreno Manzana 'B': {manzana_b} m²")

    print(f"c) Metros cubiertos Vivienda 1: {v1.get_metros_cuadrados_cubiertos()} m²")

    total_cubierto = barrio.get_superficie_total_cubierta()
    print(f"d) Superficie Total Cubierta del Barrio: {total_cubierto} m²")


if __name__ == "__main__":
    main()