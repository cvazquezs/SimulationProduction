# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42100003.py generated: Fri, 03 Nov 2017 08:48:45
#
# Event Type: 42100003
#
# ASCII decay Descriptor: pp -> (Z0/gamma* -> tau+ tau- -> l ...) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zg_tautau_condensed.py" )
from Configurables import Generation
Generation().EventType = 42100003
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Zg_tautau_condensed.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 2
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 18*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.MotherOfLeptonMinMass = 40*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
