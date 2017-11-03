# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11364410.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 11364410
#
# ASCII decay Descriptor: [[B0] -> (D*(2010)- -> (D- ->  pi+ pi- pi- pi0) pi0) (omega -> pi+ pi- pi0) pi+ ]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2XTau.py" )
from Configurables import Generation
Generation().EventType = 11364410
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-omegapi,3pipi0=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]
