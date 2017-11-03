# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/11196411.py generated: Fri, 03 Nov 2017 08:48:34
#
# Event Type: 11196411
#
# ASCII decay Descriptor: [B0 -> K+ (D*0 -> (D0 -> K- pi+) pi0) (anti-D0 -> K+ pi-) pi-]cc
#
from Configurables import Generation
Generation().EventType = 11196411
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst0D0Kpi,D0pi0,Kpi,PHSP=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool , 'TightCut')
acceptance = Generation().SignalRepeatedHadronization.TightCut
acceptance.Decay = "[B0 => ^(D*(2007)0 => ^(D0 => ^K- ^pi+) pi0 )  ^(D~0 => ^K+ ^pi-) ^K+ ^pi-  ]CC"
acceptance.Preambulo += [ "from LoKiCore.functions import in_range",
                          "from GaudiKernel.SystemOfUnits import  GeV, mrad",
                          "inAcc = ( in_range( 5*mrad, GTHETA, 400*mrad) ) ",
                          "goodPi_Dau = (GNINTREE( ('pi+'==GABSID) & inAcc, 1)  >0.5 )",
                          "goodK_Dau  = (GNINTREE( ('K+'==GABSID)  & inAcc ,1) > 0.5 )",
                          ]
acceptance.Cuts = {
    '[D0]cc'       : 'goodPi_Dau & goodK_Dau',
    '[D~0]cc'      : 'goodPi_Dau & goodK_Dau',
    '[B0]cc'       : 'goodPi_Dau & goodK_Dau'}


