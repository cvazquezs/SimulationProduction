# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/53230200.py generated: Fri, 03 Nov 2017 08:48:43
#
# Event Type: 53210000
#
# ASCII decay Descriptor: pi+,pi- => ?
#
from Configurables import ParticleGun
from Configurables import MomentumRange
ParticleGun().addTool( MomentumRange )
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMin = 200.0*SystemOfUnits.MeV
from GaudiKernel import SystemOfUnits
ParticleGun().MomentumRange.MomentumMax = 200.0*SystemOfUnits.MeV
ParticleGun().EventType = 53230200
ParticleGun().ParticleGunTool = "MomentumRange"
ParticleGun().NumberOfParticlesTool = "FlatNParticles"
ParticleGun().MomentumRange.PdgCodes = [ 211, -211 ]
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/pi+pi-,fixP=TrkAcc.dec"
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TrackersAcceptance.py" )
