# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16875032.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 16875032
#
# ASCII decay Descriptor: [Xi_b- -> (Omega_c0 -> p+ K- K- pi+) anti-nu_mu mu-]cc
#
from Configurables import Generation
Generation().EventType = 16875032
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Omegab_Omegac0munu,pKKpi_PPChange,tau=250fs=cocktail.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Xi_b- 122 5132 -1.0 6.050 1.6e-012 Xi_b- 5132 0.000000e+000", "Xi_b~+ 123 -5132 1.0 6.050 1.6e-012 anti-Xi_b+ -5132 0.000000e+000", "Omega_c0   104  4332  0.0  2.6975   2.5000e-013   Omega_c0   4332   0.00", "Omega_c~0   105  -4332  0.0   2.6975   2.5000e-013   anti-Omega_c0  -4332   0.00" ]
