import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from rvsearch import search, utils, plots, driver
import rvsearch
import numpy as np
import pandas as pd

m_star=0.454
m_star_err=0.018
star_name='TOI1685_InjRec'

#Load all the RV and mass Data
RV_data = utils.read_from_csv('data/RVS_Data_Resid.csv', binsize=0.0)
#print(RV_data)

#Set up date search range
rv_baseline=np.max(RV_data['jd'])-np.min(RV_data['jd'])

#set up the search
searcher=search.Search(RV_data, starname=star_name, min_per=0.5, max_per = 50, workers=4, mcmc=True, trend=False, verbose=True, jity=0, mstar=[m_star,m_star_err])
searcher.run_search()

#Generate the summary plot
plotter = plots.PeriodModelPlot(searcher, saveplot='TOI-1685_RVS_HalfAU.png')
plotter.plot_summary()

print('Search complete, summary plot created')

#Injection/Recovery

print('Starting I/R now')
args = None
class _args(object):
    def __init__(self):
        self.num_cpus = 6
        self.num_inject = 2000
        self.overwrite = True
        self.mstar = m_star
        self.rstar = 1.
        self.teff = 1.
        self.minP = 0.5
        self.maxP = 50
        self.minK = 0.1
        self.maxK = 100.0
        self.minE = 0.0
        self.maxE = 1.0
        self.betaE = True

args = _args()
args.search_dir = star_name
args.full_grid = False
args.verbose = False
driver.injections(args)
    
args.type = ['recovery']
args.fmt = 'png'
args.mstar = m_star
driver.plots(args)

print(star_name+' I/R Finished!')

#figure out mass sensitivity 

filename=star_name+'/recoveries.csv'
  
data=rvsearch.inject.Completeness.from_csv(filename,mstar=m_star)
data.recoveries.columns
recov=data.completeness_grid((0.03,40),(0.3,20000),resolution=30, xlogwin=0.5, ylogwin=0.5)

fig = plt.figure(figsize=(7.5, 5.25))
plt.subplots_adjust(bottom=0.18, left=0.22, right=0.95)
CS = plt.contourf(recov[0], recov[1], recov[2], 10, cmap=plt.cm.Reds_r, vmax=0.9)
fifty=plt.contour(recov[0], recov[1], recov[2], [0.5], c='black')
coords= fifty.allsegs[0][0]

plt.plot(coords[:,0],coords[:,1],color='blue')
fifty_xx=coords[:,0]
fifty_yy=coords[:,1]

plt.clf()
plt.close()

bluhm_sma = 0.06521
hirano_sma = 0.02845
fiftyday_sma = 0.204
twohundredday_sma = 0.514

hirano_min_mass = np.round(np.interp(hirano_sma,fifty_xx,fifty_yy),decimals=2)
bluhm_min_mass  = np.round(np.interp(bluhm_sma,fifty_xx,fifty_yy),decimals=2)
fiftyday_mass = np.round(np.interp(fiftyday_sma,fifty_xx,fifty_yy),decimals=2)
twohundredday_mass = np.round(np.interp(twohundredday_sma,fifty_xx,fifty_yy),decimals=2)

print('Paper     Mass Sensitivity')
print('Bluhm 21',bluhm_min_mass)
print('Hirano 21',hirano_min_mass)
print('50 day min mass: ',fiftyday_mass)
print('200 day min mass: ',twohundredday_mass)