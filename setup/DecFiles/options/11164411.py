# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11164411.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 11164411
#
# ASCII decay Descriptor: {[[B0]nos -> (D*(2007)~0 -> (D~0 -> K+ pi-) (pi0 -> gamma gamma) ) (K*(892)0 ->K+ pi-) ]cc, [[B0]os -> (D*(2007)0 -> (D0 -> K- pi+) (pi0 -> gamma gamma) ) (K*(892)~0 ->K- pi+) ]cc}
#
from Configurables import Generation
Generation().EventType = 11164411
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0Kst0,D0pi0,Kpi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
