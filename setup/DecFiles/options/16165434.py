# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16165434.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 16165434
#
# ASCII decay Descriptor: [Xi_b- -> (Sigma_c(2455)+ -> pi0 (Lambda_c+ -> p K- pi+)) pi- pi-]cc
#
from Configurables import Generation
Generation().EventType = 16165434
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib_Sigmacpipi,Lambdacpi0,pKpi=sqDalitz,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5132,-5132 ]
