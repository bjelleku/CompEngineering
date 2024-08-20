#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:43:13 2019

@author: ah
"""
import numpy as np

def rk4(yn,tn,f,h,*args):
    """ advance an ode solution from time tn to tn+h
    using the Runge-Kutta 4. order method
    yn = vector of solution values
    tn = time
    h  = time step
    f  = right hand side of ode
    *args = additional arguments passed to f"""
    k1=h*f(yn,tn,*args)
    k2=h*f(yn+0.5*k1,tn+0.5*h,*args)
    k3=h*f(yn+0.5*k2,tn+0.5*h,*args)
    k4=h*f(yn+k3,tn+h,*args)
    return yn+(k1+2*k2+2*k3+k4)/6

def ode_solv(yn,t_start,t_final,f,h,*args):
    """ returns the solution of a ode system from
    time t_start to t_final using constant step size
    yn      = initial starting values
    t_start = start time
    t_final = end_time
    f       = right hand side of ode
    h       = step size
    *args additional arguments passed to rk4"""
    y_old = yn
    t = t_start
    sol=[]
    sol.append(y_old)
    while(t<t_final):
        t += h
        #advance the solution one time step
        y_new = rk4(y_old,t,f,h,*args)
        y_old = y_new
        sol.append(np.array(y_old))
    return np.array(sol)