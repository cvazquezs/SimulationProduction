# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14145011.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 14145011
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- ) p+ p~- pi+]cc
#
from Configurables import Generation
Generation().EventType = 14145011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsippbarpi=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
