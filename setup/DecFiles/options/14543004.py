# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/14543004.py generated: Fri, 03 Nov 2017 08:48:35
#
# Event Type: 14543004
#
# ASCII decay Descriptor: [B_c+ -> (J/psi(1S) -> mu+ mu- {,gamma} {,gamma}) mu+ nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 14543004
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "BcVegPyProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bc_Jpsimunu,mm=BcVegPy,DiLeptonInAcc.dec"
Generation().Special.CutTool = "BcDaughtersInLHCb"
from Configurables import BcDaughtersInLHCb
Generation().Special.addTool( BcDaughtersInLHCb )
Generation().Special.BcDaughtersInLHCb.ChargedThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.ChargedThetaMax = 10.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMin = 0.
Generation().Special.BcDaughtersInLHCb.NeutralThetaMax = 10.
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
