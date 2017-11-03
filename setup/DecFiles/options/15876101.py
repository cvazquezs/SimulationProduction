# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/15876101.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 15876101
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> (Lambda0 -> p+ pi-) mu+ nu_mu) (D_s- -> pi- K- K+)]cc
#
from Configurables import Generation
Generation().EventType = 15876101
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LcDs,DsmunuX=cocktail,DsmuInAcc.dec"
Generation().SignalPlain.CutTool = "ListOfDaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]


from Configurables import Generation, Generation, ListOfDaughtersInLHCb
Generation().SignalPlain.addTool( ListOfDaughtersInLHCb )
Generation().SignalPlain.ListOfDaughtersInLHCb.DaughtersPIDList = [ 431 , 13 ]


