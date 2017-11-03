# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14195470.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 14195470
#
# ASCII decay Descriptor: [ B_c+ => (D*(2010)+ => (D0 -> K- pi+) pi+) (D*(2007)~0 => (D~0 => K+ pi-) pi0) ]cc
#
from Configurables import Generation
Generation().EventType = 14195470
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstDst0,D0pi+,Kpi,D0pi0,Kpi=BcVegPy,DecProdCut,HELAMP101.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
