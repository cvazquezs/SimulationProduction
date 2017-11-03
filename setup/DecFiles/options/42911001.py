# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/42911001.py generated: Fri, 03 Nov 2017 08:48:44
#
# Event Type: 42911001
#
# ASCII decay Descriptor: pp -> (W-> mu nu_mu) (b b~)...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DiJetbbmasscut.py" )
from Configurables import Generation
Generation().EventType = 42911001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_munubb=MassCut.dec"
Generation().Special.CutTool = ""

Generation.AlpGenDict = {
'alpgen_nevxiter' : 100000,
'alpgen_niter' : 2,
'alpgen_nwgtev' : 1000000,
'alpgen_FileLabel' : "wbb",
'alpgen_ihvy' : 5,
'alpgen_njets' : 0, #number of light jets
'alpgen_etabmin' : 1.596, # theta' : 400 mrad
'alpgen_ptbmin' : 3.0,
'alpgen_drbmin' : 0.500,
'alpgen_etabmax' : 10.0,
'alpgen_eta1lmin' : 1.596, # at least one charged lepton must have eta > 1.596,
'alpgen_ptlmin' : 10.0,
'alpgen_drlmin' : 0.,
'alpgen_etalmax' : 10.0,
'alpgen_iwdecmode' : 2,
'alpgen_ndns' : 9,
}


