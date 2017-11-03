# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42131205.py generated: Fri, 03 Nov 2017 08:48:42
#
# Event Type: 42131205
#
# ASCII decay Descriptor: pp -> [W+ -> (rho+ -> pi+ pi0) gamma]cc ...
#
from Configurables import Generation
Generation().EventType = 42131205
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_rho+gamma=DecProdCut.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/ParsInAcc"


from Configurables import LoKi__FullGenEventCut                                             
Generation().addTool( LoKi__FullGenEventCut, "ParsInAcc" )                               
ParsInAcc = Generation().ParsInAcc

ParsInAcc.Code = " ( count ( isGoodW ) > 0 ) "

ParsInAcc.Preambulo += [                                                                  
     "from GaudiKernel.SystemOfUnits import  GeV, mrad"                                     
   , "inCaloAcc   = (in_range(  0.030 , abs ( GPX/GPZ ) , 0.300 ) |  in_range(  0.030 , abs ( GPY/GPZ ) , 0.250 ))"
   , "inAcc       = (in_range(  0.005 , GTHETA , 0.400 ))"
   , "NGoodpim    = (GINTREE((  (('pi-' == GID) )& (GPT >0.3*GeV) & inAcc)))"
   , "NGoodpip    = (GINTREE((  (('pi+' == GID) )& (GPT >0.3*GeV) & inAcc)))"
   , "NGoodpi0    = (GINTREE((  (('pi0' == GID) )& (GPT >0.3*GeV) & inAcc)))"
   , "NGoodPiPip  = (NGoodpip & NGoodpi0)"
   , "NGoodPiPim  = (NGoodpim & NGoodpi0)"
   , "NGoodrho     = (NGoodPiPip | NGoodPiPim)"
   , "NGoodGamma = GINTREE(('gamma' == GABSID) & (GPT >10.0*GeV) & inCaloAcc)"
   , "isGoodW     = ((  'W+' == GABSID ) & NGoodrho & NGoodGamma)" 
   ]

Generation().DecayTool = ""
Generation().Special.DecayTool = ""

from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( Pythia8Production )

Generation().Special.Pythia8Production.Commands += [
"SpaceShower:rapidityOrder = off", 
"WeakSingleBoson:ffbar2W = on",
"24:addChannel = 1 1. 101 213 22", 
"24:onMode = off", 
"24:onIfAny = 213", 
"213:addChannel = 1 1. 101 111 211",
"213:onMode = off",
"213:onIfMatch = 111 211",
                                       ]


