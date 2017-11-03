# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/46000013.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 46000013
#
# ASCII decay Descriptor: pp -> (X -> ~chi_10 -> l q q' )
#
from Configurables import Generation
Generation().EventType = 46000013
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/BRpVNeutralino_m0200_m12200_lqq.dec"
Generation().Special.CutTool = "PythiaLSP"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().OtherFiles = ["$DECFILESROOT/ppfiles/mSUGRA_m0200_m12200.tbl"]
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/SusyBRpV.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHASpectrumFile = "mSUGRA_m0200_m12200_lqq.LHspc"
