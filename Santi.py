# Integrantes: Máximo Oliva y Máximo Fernández

def calcular_calorias_rutina(calorias_base, dias_entrenados, multiplicador_intensidad):
    calorias_totales = 0
    for i in range(dias_entrenados):
        calorias_totales += (calorias_base * multiplicador_intensidad)
    return calorias_totales

def evaluar_progreso_fisico(peso_actual, peso_objetivo, minutos_semanales):
    diagnostico = "Progreso en evaluación estándar"
    if peso_actual > peso_objetivo:
        diagnostico = "Fase de déficit calórico activa. Sigue ajustando tu rutina."
        if minutos_semanales > 150:
            diagnostico += " Excelente constancia, has superado los minutos recomendados."
    return diagnostico

def imprimir_resumen_fit(nombre_usuario, calorias_quemadas, estado_progreso):
    print("\n=== PANEL DE USUARIO ===")
    print(f"Atleta: {nombre_usuario}")
    print(f"Calorías totales quemadas: {calorias_quemadas} kcal")
    print(f"Diagnóstico del sistema: {estado_progreso}")
    print("=========================\n")




def categorizar_esfuerzo(minutos_entrenamiento):
    """Clasifica el nivel de esfuerzo según el tiempo invertido."""
    if minutos_entrenamiento < 30:
        return "Nivel: Ligero (Calentamiento o movilidad)"
    elif 30 <= minutos_entrenamiento <= 60:
        return "Nivel: Moderado (Sesión estándar)"
    else:
        return "Nivel: Intenso (Alto rendimiento)"


def mostrar_cronograma_semanal(lista_ejercicios):
    """Imprime una lista de ejercicios para la semana."""
    print("Plan de ejercicios para los próximos días:")
    for dia, ejercicio in enumerate(lista_ejercicios, start=1):
        print(f"Día {dia}: {ejercicio}")


def cuenta_regresiva_descanso(segundos):
    """Simula un temporizador de descanso entre series."""
    print("Iniciando tiempo de descanso...")
    while segundos > 0:
        print(f"Descanso: {segundos}s restantes")
        segundos -= 10  # Baja de 10 en 10 para no saturar la consola
    print("¡A entrenar de nuevo!")




nombre = "Máximo"
calorias_calculadas = calcular_calorias_rutina(400, 5, 1.2)
reporte_estado = evaluar_progreso_fisico(82, 75, 180)


imprimir_resumen_fit(nombre, calorias_calculadas, reporte_estado)


print(categorizar_esfuerzo(75))
print("-" * 25)
mostrar_cronograma_semanal(["Pecho", "Espalda", "Piernas", "Hombros", "Cardio"])
print("-" * 25)
cuenta_regresiva_descanso(30)