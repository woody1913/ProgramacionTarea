#integrantes:Máximo Oliva y Máximo Fernández
def
calcular_calorias_rutina(calorias_base,dias_entrenados,multiplicador_intensidad):
    calorias_totales=0

    for i in range(dias_entrenados):
        calorias_totales
+=(calorias_base*multiplicador_intensidad)
    return calorias_totales

def
evaluar_progreso_fisico(peso_actual,peso_objetivo,minutos_semanales):
    diagnostico= "progreso en evaluacion estandar"

    if peso_actual >peso_objetivo:
        diagnostico="frase de deficit calorico activa. Sigue ajustando tu rutina"
        if minutos_semanales >150:
            diagnostico +=" Excelente constancia has superado los minutos recomendados"

            return diagnostico
            def 
            imprimir_resumen_fit(nombre_usuario, calorias_quemadas, estado_progreso):
             print ("=== PANEL DE USUARIO ===")
             print (f"Atleta: {nombre_usuario}")
             print (f"Calorías totales quemadas: {calorias_quemadas} kcal")
             print (f"Diagnóstico del sistema: {estado_progreso}")
             print ("=========================")

             calorias_calculadas =  calcular_calorias_rutina(400, 5, 1.2)
             reporte_estado = evaluar_progreso_fisico(82, 75, 180)
             imprimir_resumen_fit(calorias_calculadas, reporte_estado)
