# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11104202.py generated: Fri, 03 Nov 2017 08:48:39
#
# Event Type: 11104202
#
# ASCII decay Descriptor: [B0 -> (phi(1020) -> K+ K-) (K*(892)0 -> K+ pi-) gamma]cc
#
from Configurables import Generation
Generation().EventType = 11104202
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_PhiKstgamma,KKKpi=HighPtGamma,DecProdCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/BRadiativeCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "BRadiativeCut" )
radCut = Generation().BRadiativeCut
radCut.Code = " ( count ( isGoodB ) > 0 ) "
radCut.Preambulo += [
    "from GaudiKernel.SystemOfUnits import  GeV, mrad"
  , "NGoodGamma = GINTREE(('gamma' == GABSID) & (GPT >1.5*GeV))"
  , "isGoodB    = (GBEAUTY & NGoodGamma)"
   ]

