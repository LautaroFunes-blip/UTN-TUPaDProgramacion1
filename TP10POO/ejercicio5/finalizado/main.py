try:
    from .Barrio import Barrio
    from .Vivienda import Vivienda
    from .Habitacion import Habitacion
except ImportError:
    from Barrio import Barrio
    from Vivienda import Vivienda
    from Habitacion import Habitacion


def main():
    barrio = Barrio("Los Aromos", "Constructora del Sur S.A.")

    vivienda1 = Vivienda("San Martín", 100, "A", 1, 16000)
    vivienda1.agregarHabitacion(Habitacion("Living", 45.5))
    vivienda1.agregarHabitacion(Habitacion("Dormitorio", 30))
    vivienda1.agregarHabitacion(Habitacion("Cocina", 15))

    vivienda2 = Vivienda("San Martín", 150, "A", 2, 20000)
    vivienda2.agregarHabitacion(Habitacion("Living", 50))
    vivienda2.agregarHabitacion(Habitacion("Dormitorio", 40))
    vivienda2.agregarHabitacion(Habitacion("Cocina", 20))

    vivienda3 = Vivienda("Belgrano", 200, "B", 1, 16000)
    vivienda3.agregarHabitacion(Habitacion("Living", 35.5))
    vivienda3.agregarHabitacion(Habitacion("Dormitorio", 25))

    vivienda4 = Vivienda("Belgrano", 250, "B", 2, 7500)
    vivienda4.agregarHabitacion(Habitacion("Living", 20))
    vivienda4.agregarHabitacion(Habitacion("Dormitorio", 15))
    vivienda4.agregarHabitacion(Habitacion("Baño", 10))

    barrio.agregarVivienda(vivienda1)
    barrio.agregarVivienda(vivienda2)
    barrio.agregarVivienda(vivienda3)
    barrio.agregarVivienda(vivienda4)

    print(f"Barrio: {barrio.nombre}")
    print(f"Empresa constructora: {barrio.empresaConstructora}")
    print()

    print("--- Detalle de viviendas ---")
    for vivienda in barrio.viviendas:
        print(
            f"Calle {vivienda.calle} {vivienda.numero} - "
            f"Manzana {vivienda.manzana} - Casa {vivienda.nroCasa}"
        )
        print(f"  Superficie del terreno: {vivienda.superficieTerreno} m2")
        print(
            f"  Metros cuadrados cubiertos: "
            f"{vivienda.getMetrosCuadradosCubiertos()} m2"
        )
    print()

    print(
        f"Superficie total de terreno del barrio: "
        f"{barrio.getSuperficieTotalTerreno()} m2"
    )
    print(
        f"Superficie total de terreno de la manzana A: "
        f"{barrio.getSuperficieTotalTerrenoXManzana('A')} m2"
    )
    print(
        f"Superficie total de terreno de la manzana B: "
        f"{barrio.getSuperficieTotalTerrenoXManzana('B')} m2"
    )
    print(
        f"Superficie total cubierta del barrio: "
        f"{barrio.getSuperficieTotalCubierta()} m2"
    )


if __name__ == "__main__":
    main()
