# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12165152.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 12165152
#
# ASCII decay Descriptor: [B+ -> K+ (anti-D0 -> (K_S0 -> pi+ pi-) pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 12165152
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0K,KSpipi=TightCut,LooserCuts,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[B+ -> ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^pi+ ^pi-) ^K+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'goodB        = (GP > 25000 * MeV) & (GPT > 1500 * MeV) & (GTIME > 0.05 * millimeter)',
    'goodD        = (GP > 10000 * MeV) & (GPT > 500 * MeV)',
    'goodKS       = (GP > 4000 * MeV) & (GPT > 250 * MeV)',
    'goodDDaugPi  = (GNINTREE (("pi+" == GABSID) & (GP > 1000 * MeV) & inAcc, 1) > 1.5)',
    'goodKsDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 1750 * MeV) & inAcc, 1) > 1.5)',
    'goodBachK    = (GNINTREE (("K+"  == GABSID) & (GP > 4000 * MeV) & (GPT > 400 * MeV) & inAcc, 1) > 0.5)'
]
tightCut.Cuts      =    {
    '[B+]cc'         : 'goodB  & goodBachK',
    '[D0]cc'         : 'goodD  & goodDDaugPi',
    '[KS0]cc'        : 'goodKS & goodKsDaugPi',
    '[pi+]cc'        : 'inAcc'
    }


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "LoKi::GenCutTool/TightCut"

pgun.addTool( Generation().SignalRepeatedHadronization.TightCut.clone(), "TightCut" )

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 521,-521 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_521.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 12165152
