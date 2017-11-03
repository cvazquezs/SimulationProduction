# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14745001.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 14745001
#
# ASCII decay Descriptor: [B_c+ -> (JPsi -> mu+ mu-) ({D+,D_s+,D*+,D_s*+} -> X)]cc
#
from Configurables import Generation
Generation().EventType = 14745001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_JpsiInclc,3track,miss=DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
