# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14197111.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 14197111
#
# ASCII decay Descriptor: [B_c+ -> (D+ -> K- pi+ pi+) (anti-D0 -> (K_S0 -> pi+ pi-) pi+ pi-) ]cc
#
from Configurables import Generation
Generation().EventType = 14197111
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D+D0,KSpipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
