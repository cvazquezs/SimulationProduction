# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/12165027.py generated: Fri, 03 Nov 2017 08:48:36
#
# Event Type: 12165027
#
# ASCII decay Descriptor: [B+ -> (D_s+ -> K+ pi- pi+)  K+ K-]cc
#
from Configurables import Generation
Generation().EventType = 12165027
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_Ds+K+K-,Kpipi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

# Mass cut
from Configurables import LoKi__GenCutTool
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool, 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay = '^[ B+ => ^(D_s+ -> ^K+ ^pi- ^pi+) ^K+ ^K- ]CC'
tightCut.Cuts = {
  "[K+]cc"   : "in_range(0.005, GTHETA, 0.400)",
  "[pi+]cc"  : "in_range(0.005, GTHETA, 0.400)",
  "[B+]cc"   : "GMASS('K+' == GID, 'K-' == GID) < 2200 * MeV"
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
pgun.EventType = 12165027
