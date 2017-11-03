# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12875520.py generated: Fri, 03 Nov 2017 08:48:46
#
# Event Type: 12875520
#
# ASCII decay Descriptor: [B+ => (D~0 -> (KS0 -> pi+ pi-) pi+ pi-) anti-nu_mu mu+]cc
#
from Configurables import Generation
Generation().EventType = 12875520
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0munu,KSpipi=cocktail,TightCut,BRcorr1.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[B+ => ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^pi+ ^pi-) ^Nu ^mu+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'goodB        = (GFAEVX(abs(GVZ), 0) - GFAPVX(abs(GVZ), 0) > 1.6 * millimeter)',
    'goodD        = (GP > 20000 * MeV) & (GPT > 1900 * MeV)',
    'goodKS       = (GFAEVX(abs(GVZ), 0) < 2500.0 * millimeter)',
    'goodDDaugPi  = (GNINTREE (("pi+" == GABSID) & (GP > 2100 * MeV) & inAcc, 4) > 3.5)',
    'goodKsDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 2500 * MeV) & inAcc, 4) > 1.5)',
    'goodMuon     = (GNINTREE (("mu+" == GABSID) & (GP > 8000 * MeV) & (GPT > 1300 * MeV) & inAcc, 1) > 0.5)',
]
tightCut.Cuts      =    {
    '[B+]cc'         : 'goodB  & goodMuon',
    '[D0]cc'         : 'goodD  & goodDDaugPi',
    '[KS0]cc'        : 'goodKS & goodKsDaugPi',
    '[mu+]cc'        : 'inAcc'
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
pgun.EventType = 12875520
