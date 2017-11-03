# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11114051.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 11114051
#
# ASCII decay Descriptor: [B0 -> mu+ mu- mu+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 11114051
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_4mu=Gorbunov01,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
