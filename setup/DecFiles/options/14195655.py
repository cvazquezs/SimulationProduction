# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14195655.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 14195655
#
# ASCII decay Descriptor: [ B_c+ => (D*_s+ => (D_s+ -> K- K+ pi+) pi0) (D*(2007)~0 => (D~0 => K+ pi-) gamma) ]cc
#
from Configurables import Generation
Generation().EventType = 14195655
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DsstDst0,Dspi0,KKpi,D0gamma,Kpi=BcVegPy,LooseNeutralCut,HELAMP010.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
