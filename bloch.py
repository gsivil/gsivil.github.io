import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import ode

gamma0 = 0.1
Omega0 = 3
delta0 = 1

y0, t0 = [0, 1, 0, 0], 0
def f(t, y, gamma, Omega, delta):
	return [gamma*y[1]+0.5*1j*(np.conjugate(Omega)*y[3]-Omega*y[2]), -gamma*y[1]+0.5*1j*(np.conjugate(Omega)*y[2]-Omega*y[3]),-(0.5*gamma+1j*delta)*y[2]+0.5*1j*np.conjugate(Omega)*(y[1]-y[0]),-(0.5*gamma-1j*delta)*y[3]+0.5*1j*Omega*(y[0]-y[1])]

r = ode(f).set_integrator('zvode', method='bdf')
r.set_initial_value(y0, t0).set_f_params(gamma0, Omega0, delta0)
t1 = 10
dt = 0.01
while r.successful() and r.t < t1:
	plt.scatter(r.t+dt, np.abs(r.integrate(r.t+dt)[0]), color = "blue")
	plt.scatter(r.t+dt, np.abs(r.integrate(r.t+dt)[1]), color = "red")
	#plt.scatter(r.t+dt, np.real(r.integrate(r.t+dt)[2]), color = "green")
	#plt.scatter(r.t+dt, np.real(r.integrate(r.t+dt)[3]), color = "black")

plt.show()



delta = -5
while delta < 5:
	r = ode(f).set_integrator('zvode', method='bdf')
	r.set_initial_value(y0, t0).set_f_params(gamma0, Omega0, delta)
	plt.scatter(delta, np.abs(r.integrate(t1)[0]), color = "blue")
	plt.scatter(delta, np.abs(r.integrate(t1)[1]), color = "red")
	delta = delta + 0.01

	

plt.show()


