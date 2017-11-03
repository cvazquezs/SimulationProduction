# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164235.py generated: Fri, 03 Nov 2017 08:48:50
#
# Event Type: 11164235
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2007)~0 -> (D~0 -> pi+ pi-) gamma ) (K*(892)~0 ->K- pi+) ]cc, [[B0]os -> (D*(2007)0 -> (D0 -> pi- pi+) gamma ) (K*(892)0 ->K+ pi-) ]cc}
#
from Configurables import Generation
Generation().EventType = 11164235
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0Kst0,D0gamma,pipi=DecProdCut,HELAMP010.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
