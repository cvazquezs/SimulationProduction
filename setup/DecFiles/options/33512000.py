# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/33512000.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 33512000
#
# ASCII decay Descriptor: [Lambda0 -> p+ mu- anti-nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 33512000
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lambda_pmunu.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 3122,-3122 ]
