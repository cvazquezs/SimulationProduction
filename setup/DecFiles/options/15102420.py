# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15102420.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 15102420
#
# ASCII decay Descriptor: [ Lambda_b0 -> p+ pi- pi0 ]cc
#
from Configurables import Generation
Generation().EventType = 15102420
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_ppipi0=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
