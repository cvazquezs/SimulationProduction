# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14103041.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 14103041
#
# ASCII decay Descriptor: [B_c+ -> (B_s0 -> K+ K-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 14103041
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Bspi+,KK=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
