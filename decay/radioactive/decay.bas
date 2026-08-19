! Simulation of radioactive decay
! N. Giordano 10-1-94
program decay
    option nolet                            ! can omit the *let* keyword
    library "sgfun*", "sglib*", "decay_subs*"  ! Incluye las librerías gráficas Y tus subrutinas
    
    ! Declaración de arrays y variables
    dim n_uranium(100), t(1000)
    dim tau, dt
    
    ! Declaración de subrutinas externas
    external sub initializate(n_uranium(), t(), tau, dt)
    external sub calculate(n_uranium(), t(), tau, dt)
    external sub display(n_uranium(), t(), tau, dt)
    
    ! Llamadas a las subrutinas
    call initializate(n_uranium(), t(), tau, dt)
    call calculate(n_uranium(), t(), tau, dt)
    call display(n_uranium(), t(), tau, dt)
end