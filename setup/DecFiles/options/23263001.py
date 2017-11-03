# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23263001.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 23263001
#
# ASCII decay Descriptor: [D_s+ => K- K+ pi+]cc
#
from Configurables import Generation
Generation().EventType = 23263001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Ds=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
