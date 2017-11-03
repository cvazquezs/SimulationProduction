# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164322.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 15164322
#
# ASCII decay Descriptor: [Lambda_b0 -> (anti-D0 -> K+ K-) (Sigma0 -> (Lambda -> p+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15164322
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_antiD0Sigma,KKLambdagamma,ppi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
