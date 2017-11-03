from Configurables import Generation, RepeatDecay, Inclusive, DiLeptonInAcceptance
from GaudiKernel.SystemOfUnits import GeV, MeV, mm

Generation().SampleGenerationTool = "RepeatDecay"
Generation().addTool( RepeatDecay ) 
Generation().RepeatDecay.NRedecay =  100
Generation().RepeatDecay.addTool( Inclusive ) 
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().addTool( DiLeptonInAcceptance ) 
Generation().DiLeptonInAcceptance.RequireOppositeSign = True
Generation().DiLeptonInAcceptance.RequireSameSign = False
Generation().DiLeptonInAcceptance.LeptonOnePMin = 3*GeV 
Generation().DiLeptonInAcceptance.LeptonTwoPMin = 3*GeV 
Generation().DiLeptonInAcceptance.MinMass = 4700*MeV
Generation().DiLeptonInAcceptance.MaxMass = 6000*MeV
Generation().DiLeptonInAcceptance.PreselDoca = True
Generation().DiLeptonInAcceptance.DocaCut = 0.4*mm
Generation().DiLeptonInAcceptance.PreselPtProd = True
Generation().DiLeptonInAcceptance.PtProdMinCut = 4*GeV*4*GeV
Generation().DiLeptonInAcceptance.PtProdMaxCut = 1000*GeV*1000*GeV
