! Archivo: decay_subs.bas

SUB initializate(nuclei(), t(), time_constant, dt)
    ! Inicialización de variables
    INPUT PROMPT "Ingrese el número de núcleos iniciales -> ": nuclei(1)
    LET t(1) = 0
    INPUT PROMPT "Ingrese la constante de tiempo (tau) -> ": time_constant
    INPUT PROMPT "Ingrese el paso de tiempo (dt) -> ": dt
END SUB

SUB calculate(n_uranium(), t(), tau, dt)
    ! Cálculo de la desintegración radioactiva
    ! Ecuación: dN/dt = -N/τ  =>  N(t+dt) = N(t) * (1 - dt/τ)
    FOR i = 1 TO SIZE(t) - 1
        LET n_uranium(i+1) = n_uranium(i) * (1 - dt/tau)
        LET t(i+1) = t(i) + dt
    NEXT i
END SUB

SUB display(n_uranium(), t(), tau, dt)
    ! Gráfica y visualización de resultados
    CALL settitle("Desintegración Radioactiva")
    CALL sethlabel("Tiempo (s)")
    CALL setvlabel("Número de núcleos")
    CALL datagraph(t(), n_uranium(), 4, 0, "black")
    
    SET CURSOR 5, 30
    PRINT "Constante de tiempo: "; dt
END SUB