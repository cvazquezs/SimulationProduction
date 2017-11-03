# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104141.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 11104141
#
# ASCII decay Descriptor: [B0 -> p- pi+ (Lambda -> p+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104141
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Lambdap-pi+=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
