# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11144120.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 11144120
#
# ASCII decay Descriptor: [B0 -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) p+ p~-]cc
#
from Configurables import Generation
Generation().EventType = 11144120
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Jpsippbar=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
