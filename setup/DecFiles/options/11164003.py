# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164003.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11164003
#
# ASCII decay Descriptor: [[B0]cc -> (D- => K+ pi- pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 11164003
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-pi+,Kpipi=CPVDDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
