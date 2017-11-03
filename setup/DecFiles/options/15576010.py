# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15576010.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 15576010
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c(2593)+ -> (Lambda_c+ -> p+ K- pi+) pi+ pi-) mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 15576010
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Lc2593munu,Lcpipi,pKpi=LHCbAcceptance.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]
