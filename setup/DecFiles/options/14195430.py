# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14195430.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 14195430
#
# ASCII decay Descriptor: [B_c+ => (D*(2010)+ => (D+ -> K- pi+ pi+) pi0) (D*(2007)~0 => (D~0 -> K+ pi-) pi0) ]CC
#
from Configurables import Generation
Generation().EventType = 14195430
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstDst0,D+pi0,Kpipi,D0pi0,Kpi=BcVegPy,DecProdCut,HELAMP101.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
