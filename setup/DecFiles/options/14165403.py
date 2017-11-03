# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14165403.py generated: Fri, 03 Nov 2017 08:48:49
#
# Event Type: 14165403
#
# ASCII decay Descriptor: [B_c+ -> (D_s*+ -> (D_s+ -> K+ pi- pi+) pi0) (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 14165403
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_PhiDsst,KK,Dspi0,Kpipi=DecProdCut,BcVegPy,HELAMP001.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
