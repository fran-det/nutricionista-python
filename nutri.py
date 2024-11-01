"Nutricionista Virtual"

# Solicitar datos al usuario
# Pedir al usuario su peso, altura, edad, sexo, nivel de actividad y objetivo.
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
edad = int(input("Ingrese su edad en años: "))
sexo = input("Ingrese su sexo (hombre/mujer): ")
actividad = input(
    "Ingrese su nivel de actividad (sedentario, ligera, moderada, alta, muy alta): ")
objetivo = input("Ingrese su objetivo (mantenimiento, pérdida, ganancia): ")


def calcular_imc(peso, altura):
    # Calcular el índice de masa corporal (IMC) dividiendo el peso por la altura al cuadrado.
    imc = peso / (altura ** 2)

    # Clasificar el IMC en categorías según el valor calculado.
    clasificacion = (
        "Bajo peso" if imc < 18.5 else
        "Normal" if 18.5 <= imc < 24.9 else
        "Sobrepeso" if 25 <= imc < 29.9 else
        "Obesidad"
    )
    # Retorna el IMC y su clasificación.
    return imc, clasificacion


def calcular_tmb(sexo, peso, altura, edad):
    # Calcular la tasa metabólica basal (TMB) usando fórmulas diferentes para hombres y mujeres.
    if sexo.lower() == 'hombre':
        # Fórmula para hombres.
        return 88.36 + (13.4 * peso) + (4.8 * altura * 100) - (5.7 * edad)
    elif sexo.lower() == 'mujer':
        # Fórmula para mujeres.
        return 447.6 + (9.2 * peso) + (3.1 * altura * 100) - (4.3 * edad)
    else:
        # Si el sexo no es válido, lanza un error indicando que debe ser 'hombre' o 'mujer'.
        raise ValueError(
            "Sexo no válido, por favor ingrese 'hombre' o 'mujer'.")


def calcular_calorias_diarias(tmb, actividad='sedentario'):
    # Definir los factores de actividad física, cada uno multiplica la TMB para ajustar el gasto calórico.
    niveles_actividad = {
        'sedentario': 1.2,
        'ligera': 1.375,
        'moderada': 1.55,
        'alta': 1.725,
        'muy alta': 1.9
    }

    # Multiplicar la TMB por el factor correspondiente al nivel de actividad y lo retorna.
    return tmb * niveles_actividad.get(actividad, 1.2)


def sugerir_macronutrientes(calorias_diarias, objetivo='mantenimiento'):
    # Calcular la distribución de macronutrientes (proteínas, grasas, carbohidratos)
    # en gramos según el objetivo del usuario.
    if objetivo == 'pérdida':
        # Distribución para pérdida de peso.
        return (0.3 * calorias_diarias / 4, 0.25 * calorias_diarias / 9, 0.45 * calorias_diarias / 4)
    elif objetivo == 'ganancia':
        # Distribución para ganancia de peso.
        return (0.25 * calorias_diarias / 4, 0.3 * calorias_diarias / 9, 0.45 * calorias_diarias / 4)
    else:
        # Distribución para mantenimiento de peso.
        return (0.25 * calorias_diarias / 4, 0.3 * calorias_diarias / 9, 0.45 * calorias_diarias / 4)


def generar_ficha_medica(**kwargs):
    # Extraer los datos proporcionados del usuario usando `kwargs`.
    peso = kwargs['peso']
    altura = kwargs['altura']
    edad = kwargs['edad']
    sexo = kwargs['sexo']
    actividad = kwargs.get('actividad', 'sedentario')
    objetivo = kwargs.get('objetivo', 'mantenimiento')

    # Llamar a las funciones previas para calcular el IMC, la TMB y las calorías diarias.
    imc, clasificacion_imc = calcular_imc(peso, altura)
    tmb = calcular_tmb(sexo, peso, altura, edad)
    calorias_diarias = calcular_calorias_diarias(tmb, actividad)

    # Llamar a `sugerir_macronutrientes` para calcular la distribución de macronutrientes.
    proteinas, grasas, carbohidratos = sugerir_macronutrientes(
        calorias_diarias, objetivo)

    # Generar una ficha médica con los datos calculados y las recomendaciones.
    ficha = f"""
    ----------------------------
    Ficha Médica Nutricionista Virtual
    ----------------------------
    Peso: {peso} kg
    Altura: {altura} m
    Edad: {edad} años
    Sexo: {sexo}
    Actividad física: {actividad}
    Objetivo: {objetivo.capitalize()}

    Índice de Masa Corporal (IMC): {imc:.2f} - {clasificacion_imc}
    Tasa Metabólica Basal (TMB): {tmb:.2f} calorías/día
    Ingesta Calórica Recomendada: {calorias_diarias:.2f} calorías/día

    Distribución Recomendada de Macronutrientes:
    - Proteínas: {proteinas:.2f} gramos
    - Grasas: {grasas:.2f} gramos
    - Carbohidratos: {carbohidratos:.2f} gramos
    ----------------------------
    """
    # Retornar el reporte completo.
    return ficha


def guardar_ficha_medica(ficha, nombre_archivo="ficha_medica.txt"):
    # Abrir un archivo de texto en modo escritura y guarda el reporte.
    with open(nombre_archivo, 'w', encoding='utf-8') as file:
        file.write(ficha)


# Almacenar los datos en un diccionario `datos_usuario`.
datos_usuario = {
    'peso': peso,
    'altura': altura,
    'edad': edad,
    'sexo': sexo,
    'actividad': actividad,
    'objetivo': objetivo
}

# Generar la ficha médica con los datos proporcionados.
ficha = generar_ficha_medica(**datos_usuario)

# Guardar la ficha médica en un archivo de texto.
guardar_ficha_medica(ficha)

# Mensaje de finalización
print("El análisis se ha completado y la ficha médica se ha guardado correctamente.")
