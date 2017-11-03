# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/18114025.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 18114025
#
# ASCII decay Descriptor: Upsilon(3S) -> (Upsilon(2S) -> mu+ mu-) pi+ pi-
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Upsilon.py" )
from Configurables import Generation
Generation().EventType = 18114025
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xb_Upsilon2Spipi,mumu=DecProdCut,10.8GeV.dec"
Generation().Special.CutTool = "UpsilonDaughtersInLHCb"
from Configurables import UpsilonDaughtersInLHCb
Generation().Special.addTool( UpsilonDaughtersInLHCb )
Generation().Special.UpsilonDaughtersInLHCb.SignalPID = 200553
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ " Upsilon(3S)   844   200553  0.0  10.8  1.000000e-020       Upsilon(3S)   200553  1.000000e-004" ]
