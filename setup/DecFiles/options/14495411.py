# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14495411.py generated: Fri, 03 Nov 2017 08:48:47
#
# Event Type: 14495411
#
# ASCII decay Descriptor: [B_c+ => (D*(2010)+ => (D+ -> K- pi+ pi+) (pi0||gamma)) (D*(2007)~0 => (D~0 -> K+ pi-) (pi0||gamma)) ]CC
#
from Configurables import Generation
Generation().EventType = 14495411
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstDst0,Kpipi,Kpi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
