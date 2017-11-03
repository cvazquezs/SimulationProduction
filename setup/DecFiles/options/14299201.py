# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14299201.py generated: Fri, 03 Nov 2017 08:48:38
#
# Event Type: 14299201
#
# ASCII decay Descriptor: [ B_c+ => (D*(2010)+ => (D0 -> K- pi+ pi- pi+) pi+) (D*(2007)~0 => (D~0 => K+ pi- pi+ pi-) gamma) ]cc
#
from Configurables import Generation
Generation().EventType = 14299201
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_DstDst0,D0pi+,Kpipipi,D0gamma,Kpipipi=BcVegPy,DecProdCut,HELAMP101,D0IncoherentSum.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
