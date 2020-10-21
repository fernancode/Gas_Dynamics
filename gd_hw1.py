import gas_dynamics as gd

###############################problem 1##########################
atm = 1.01325
p = 2 + atm
p_t = 2.2 + atm
a = gd.sonic_velocity(T=323.15)
M = gd.stgn_pressure(p=p, p_t=p_t, get = 'M')
V1 = a*M
V2 = ((p_t-p)*(2/(p/(287 * 323.15))))**.5
p = 2 + atm
p_t = 5.5 + atm
M = gd.stgn_pressure(p=p, p_t=p_t, get = 'M')
Vc = a*M
Vi = ((p_t-p)*(2/(p/(287 * 323.15))))**.5

print('1a) Compressible velocity is %.2f ''m/s' % V1)
print('1b) Incompressible velocity is %.2f ''m/s' % V2)
#print('1c) Compressible velocity is %.2f m/s' % Vc,' incompressible velocity is %.2f ''m/s''' % Vi)


################################problem 2a################################
gamma = 1.32
p1 = 14
T1 = 500
V1 = 125
R = 518.3
M2 = 0.8

M1 = V1 / gd.sonic_velocity(gamma=gamma, R = R, T = T1)
T2 = gd.temperature_mach_ratio(T1=T1,M1=M1,M2=.8,get='T2',gamma=gamma)
a = gd.sonic_velocity(gamma=gamma,R = R, T = T2)
V2 = M2 * a
p2 = gd.pressure_mach_ratio(p1=p1, M1 = M1, M2 = M2, gamma=gamma, R = R)
a_ratio = gd.area_mach_ratio(M1,M2,gamma=gamma, R = R)

print('\n')
print('2a) Temperature 2 is %.2f' % T2 , 'K and velocity 2 is %.2f m/s' % V2)
print('2b) Pressure 2 assuming no friction losses is %.3f bar' % p2)
print('2c) The area ratio is %.3f ' % a_ratio)

######################## problem 3a ######################
p1 = 7 * 101.325
T1 = 600
p2 = 4 * 101.325
T2 = 550
M2 = .9
gamma = 1.29
R = 189

M1 = gd.temperature_mach_ratio(T1=T2, T2=T1, M1=M2, get='M2',gamma=gamma)
V1 = M1 * gd.sonic_velocity(gamma=gamma, R=R, T=T1)
pt1 = gd.stgn_pressure(p=p1, M=M1, gamma=gamma, get='p_t')
pt2 = gd.stgn_pressure(p=p2, M=M2, gamma=gamma, get='p_t')
ds = gd.entropy_produced(pt1=pt1, pt2=pt2, R=R)
a_ratio = gd.area_mach_ratio(M1, M2, gamma=gamma, R=R , ds=ds)

print('\n')
print('3a) The velocity is %.2f m/s' % V1)
print('3b) The change in entropy is %.2f kJ/Kg K' % ds)
print('3c) Area ratio is %.2f ' % a_ratio)

################ problem 4 #######################

M1 = 0.3
T1 = 450
p1 = 10 * 100 * 1000
A1 = 0.1
a_ratio = gd.a_star_ratio(M=M1)
a_star = A1/a_ratio
p_t = gd.stgn_pressure(p=p1,M=M1)
T_t = gd.stgn_temperature(T=T1, M=M1)
m_dot = a_star * gd.mdot_a_star(p_t=p_t, T_t=T_t)
p_rec = 1.5 * 100 * 1000
M2 = gd.pressure_mach_ratio(p1=p_t, p2=p_rec, M1=0, get='M2')
a2 = a_star * gd.a_star_ratio(M2)
print('\n')
print('4a) Flow rate is %.2f kg/s ' % m_dot)
print('4b) The throat area is %.4f m^2' % a_star)
print('4c) The exit area is %.4f m^2 ' % a2)

############################problem 5############################

T1 = 573.15
p1 = 300000 #kPa to Pa
p2 = 100000 #kPa to Pa
mdot = 0.1
R = 461
gamma = 1.33
M2 = gd.pressure_mach_ratio(p1=p1, p2=p2, M1=0, get='M2', gamma=gamma, R=R)
#problem 5b
a_star = mdot / gd.mdot_a_star(p_t=p1, T_t=T1, R=R, gamma=gamma) 
a_exit = a_star * gd.a_star_ratio(M2, gamma=gamma)
print('\n')
print('5a) Converging-Diverging, exit mach is %.2f '% M2)
print('5b) Throat area is %.6f m^2' % a_star, 'and the exit area is %.6f m^2' % a_exit)

###########################problem 6 #################################

#m_dot = 100
#eta = 0.95
#p1 = 300000
#T1 = 673.15
#gamma = 1.35
#cp = 1100
#p2 = 100000
#exhaust gases, so assume air
#get mdot_astar, divide a_star by mdot_a_starm
#a_star = m_dot / gd.mdot_a_star(p_t=p1, T_t=T1)
#M2s = gd.pressure_mach_ratio(p1=p1, p2=p2, M1=0, get='M2',gamma=gamma)
#A2 = a_star * gd.a_star_ratio(M2s,gamma=gamma)

#T2s = gd.stgn_temperature(T_t=T1, M=M2s, get='T',gamma=gamma)
#V2s = M2s * gd.sonic_velocity(gamma=gamma,T=T2s)

#T2 = (eta*(cp*T1 - cp*T2s) - cp*T1)/(-cp)
#M2 = gd.stgn_temperature(T_t=T1, T=T2, get='M')
#V2 = M2 * gd.sonic_velocity(gamma=gamma, T=T2)

#print('\n')
#print('6a) Throat area is %.2f' % a_star)
#print('6a) Exit area is %.2f' % A2)
#print('6a) Ideal exit mach number and velocity are %.3f' % M2s,' and %.2f m/s' % V2s)
#print('6a) Actual exit mach number and velocity are %.3f' % M2,' and %.2f m/s' % V2)