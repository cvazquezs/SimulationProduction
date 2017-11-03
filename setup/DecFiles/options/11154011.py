# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11154011.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 11154011
#
# ASCII decay Descriptor: [B0 -> (psi(2S) -> e+ e-) (K*(892)0 -> K+ pi-)]CC
#
from Configurables import Generation
Generation().EventType = 11154011
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_psi2SKst,ee=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
