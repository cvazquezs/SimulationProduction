# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23113011.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 23113011
#
# ASCII decay Descriptor: [D_s+ -> pi+ e+ mu-]cc
#
from Configurables import Generation
Generation().EventType = 23113011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_pi+emu=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
