# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15154040.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 15154040
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda(1520)0 -> p+ K-) (J/psi -> e+ e-)]cc
#
from Configurables import Generation
Generation().EventType = 15154040
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambda1520Jpsi,ee=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
