# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/26165057.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 26165057
#
# ASCII decay Descriptor: [Xi_cc+ -> (D+ => pi+ pi+ K-) p+ K- ]cc
#
from Configurables import Generation
Generation().EventType = 26165057
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "GenXiccProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import GenXiccProduction
Generation().Special.addTool( GenXiccProduction )
Generation().Special.GenXiccProduction.BaryonState = "Xi_cc+"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xicc_D+pK,Kpipi=GenXicc,DecProdCut,WithMinPTv3.dec"
Generation().Special.CutTool = "XiccDaughtersInLHCbAndWithMinPT"
from Configurables import XiccDaughtersInLHCbAndWithMinPT
Generation().Special.addTool( XiccDaughtersInLHCbAndWithMinPT )
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.BaryonState = Generation().Special.GenXiccProduction.BaryonState
from GaudiKernel import SystemOfUnits
Generation().Special.XiccDaughtersInLHCbAndWithMinPT.MinXiccPT = 3200*SystemOfUnits.MeV
