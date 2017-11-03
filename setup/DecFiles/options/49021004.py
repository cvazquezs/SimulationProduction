# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/49021004.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 49021004
#
# ASCII decay Descriptor: pp => ccbar (=> eX)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/HardQCD_ccbar.py" )
from Configurables import Generation
Generation().EventType = 49021004
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "Pythia8Production"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ccbar=HardQCD,pt18GeV,e.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/HighPtElectronInAcc"

from Configurables import LoKi__FullGenEventCut
Generation().addTool(LoKi__FullGenEventCut, 'HighPtElectronInAcc')
cutTool = Generation().HighPtElectronInAcc
cutTool.Code = 'count(HighPtElectronInAcc) > 0'
cutTool.Preambulo += [
   'from GaudiKernel.SystemOfUnits import ns, GeV, mrad',
   'GPT = LoKi.GenParticles.TransverseMomentum()',
   'isElectron = (GABSID == 11)',
   'highPT = ((GTHETA < 400.0*mrad) & (GPT > 18*GeV))',
   'HighPtElectronInAcc = ((isElectron) & (highPT))'
   ]

