# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15164410.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 15164410
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p K+ pi- pi0) pi-]cc
#
from Configurables import Generation
Generation().EventType = 15164410
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lambdacpi,pKpipi0=PHSP,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
