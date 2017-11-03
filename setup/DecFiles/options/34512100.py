# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/34512100.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 34512100
#
# ASCII decay Descriptor: K_S0 -> pi+ mu- nu_mu~
#
from Configurables import Generation
Generation().EventType = 34512100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ks_pimunu.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]
