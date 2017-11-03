# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11202400.py generated: Fri, 03 Nov 2017 08:48:40
#
# Event Type: 11202400
#
# ASCII decay Descriptor: {[[B0]nos => K+ pi- (pi0 -> gamma gamma)]cc, [[B0]os => K- pi+ (pi0 -> gamma gamma)]cc}
#
from Configurables import Generation
Generation().EventType = 11202400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_K+pi-pi0.dec"
Generation().SignalRepeatedHadronization.CutTool = "LHCbAcceptance"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
