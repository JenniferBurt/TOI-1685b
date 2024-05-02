#----------------------------------------------------------
#File to analyze TOI-1685 RV and TESS data
#----------------------------------------------------------

nplanets = 1
#Filename including all the RV and activity indicators time-series
fname_rv = ['all_rvs.dat']

#MCMC controls
thin_factor = 10
niter = 500
nchains = 100

#Choose the method that we want to use
method = 'mcmc'  #this runs the mcmc fit program
#method = 'plot' #this option create the plots only if a previus run was done

is_rasterized = False
is_seaborn_plot = True
is_plot_correlations = False
is_plot_chains = False

is_clustering = True

#TOI-1685 parameters from Eric's updated analysis:
mstar_mean  = 0.454
mstar_sigma = 0.018
rstar_mean  = 0.4555
rstar_sigma = 0.0128
tstar_mean  = 3434
tstar_sigma = 51

# What units do you prefer for your planet parameters?
# earth, jupiter or solar
unit_mass = 'earth'

fit_rv = [True,True]
is_jitter_rv = True

fit_tr = [False,False]
is_jitter_tr = False

is_ew = False

#Prior section
# f -> fixed value
# u -> Uniform priors
# g -> Gaussian priors
fit_t0 = ['g']
fit_P  = ['g']
fit_ew1= ['f']   #We fix sqrt(e) sin w, it works only if is_ew = True
fit_ew2= ['f']   #We fix sqrt(e) cos w, it works only if is_ew = True
fit_e  = ['f']   #We fix e, it works only if is_ew = False
fit_w  = ['f']   #We fix w, it works only if is_ew = False
fit_b  = ['u']   #We fix the impact factor
fit_a  = ['u']   #We fit a with gaussian priors (given by the stellar parameters)
fit_rp = ['u']   #We fit rp with uniform priors
fit_k  = ['u']   #We fit k with uniform priors
fit_v0 = 'u'         #We fit systemc velicities with uniform priors

#Prior ranges for a parameter A
#if 'f' is selected for the parameter A, A is fixed to the one given by min_A
#if 'u' is selected for the parameter A, sets uniform priors between min_A and max_A
#if 'g' is selected for the parameter A, sets gaussian priors with mean min_A and standard deviation max_A

#Values from Matthew's updated transit fit (TESS + Muscat)
min_t0  = [9910.93830]
max_t0  = [0.00038]
min_P   = [0.66913923]
max_P   = [0.00000040]

min_a   = [1.1]*nplanets
max_a   = [40.]*nplanets
min_b   = [0.0]*nplanets
max_b   = [1.0]*nplanets
min_k   = [0.0]*nplanets
max_k   = [0.05]*nplanets
min_rp  = [0.0]*nplanets
max_rp  = [0.05]*nplanets

min_e = [0.0]*nplanets
max_e = [0.0]*nplanets
min_w = [0.0]*nplanets
max_w = [0.0]*nplanets

min_rv0=[-0.005]
max_rv0=[.005]

#----------------------------------------------------------
# GP Section
#----------------------------------------------------------

telescopes = ['CARMENES','MXB_20','MXR_20','MXB_21','MXR_21','IRD']
telescopes_labels = ['CARMENES','MXB 2020','MXR 2020','MXB 2021','MXR 2021','IRD']

kernel_rv = 'MQ1'

fit_krv = [None]*5 #Define the list with 5 elements
fit_krv[0] = 'u' #A_0
fit_krv[1] = 'f' #A_1
fit_krv[2] = 'u' #lambda_e
fit_krv[3] = 'u' #lambda_p
fit_krv[4] = 'u' #P_GP

krv_priors = [
        0.0,1.5,   #ranges for A_0
        0.0,1.5,   #ranges for A_1
        1,150,      #ranges for lambda_e
        0.01,2.0,  #ranges for lambda_p
        17,20,      #ranges for P_GP
]

#----------------------------------------------------------
#END
#----------------------------------------------------------