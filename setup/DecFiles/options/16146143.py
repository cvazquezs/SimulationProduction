# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16146143.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 16146143
#
# ASCII decay Descriptor: [Xi_b0 -> (Xi*0 -> (Xi- -> (Lambda0 -> p+ pi-) pi-) pi+ ) (J/psi(1S) -> mu+ mu-)]cc
#
from Configurables import Generation
Generation().EventType = 16146143
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_JpsiXist,mm,Xipi,Lambdapi=DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
