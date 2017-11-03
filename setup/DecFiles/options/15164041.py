# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164041.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 15164041
#
# ASCII decay Descriptor: [Lambda_b0 -> (D_s- -> K+ K- pi-) p+]cc
#
from Configurables import Generation
Generation().EventType = 15164041
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Dsp,K+K-pi-=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
