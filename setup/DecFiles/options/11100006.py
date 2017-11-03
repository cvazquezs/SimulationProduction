# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11100006.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 11100006
#
# ASCII decay Descriptor: [B0-> (K*0 -> Kspi0) (phi -> K+K-)]cc
#
from Configurables import Generation
Generation().EventType = 11100006
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Kst0Phi,KsPi0K+K-=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
