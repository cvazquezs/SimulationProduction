# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/16146146.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 16146146
#
# ASCII decay Descriptor: [Xi_b0 -> pi+ pi- (Lambda0 -> p+ pi-) (J/psi(1S) -> mu+ mu-)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 16146146
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xib0_JpsiLambdapipi,mm=DecProdCut,pCut1600MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 5232,-5232 ]
