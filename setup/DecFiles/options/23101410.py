# file /home/marinang/GaussDev_v49r3/Gen/DecFiles/options/23101410.py generated: Fri, 03 Nov 2017 08:48:48
#
# Event Type: 23101410
#
# ASCII decay Descriptor: [D_s- -> pi- ( eta -> gamma gamma )]cc
#
from Configurables import Generation
Generation().EventType = 23101410
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_pi+eta,gg=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D_s+ -> ^pi+ ( eta -> gamma gamma )]CC'
tightCut.Cuts      =    {
    '[pi+]cc'    : ' inAcc & piCuts',
    '[D_s+]cc'   : 'Dcuts' }
tightCut.Preambulo += [
    'inAcc = in_range ( 0.005, GTHETA, 0.400 ) ' , 
    'piCuts = ( (GPT > 200 * MeV) & ( GP > 600 * MeV))',
    'Dcuts = (GPT > 1000 * MeV)' ]

