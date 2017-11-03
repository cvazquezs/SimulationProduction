# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14197441.py generated: Fri, 03 Nov 2017 08:48:41
#
# Event Type: 14197441
#
# ASCII decay Descriptor: [ B_c+ => (D+ -> K- pi+ pi+) (D*(2007)~0 => (D~0 -> K+ pi- pi+ pi-) pi0) ]CC
#
from Configurables import Generation
Generation().EventType = 14197441
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_D+Dst0,Kpipi,D0pi0,Kpipipi=BcVegPy,DecProdCut.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
