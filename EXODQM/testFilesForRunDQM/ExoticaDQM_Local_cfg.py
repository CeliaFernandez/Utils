import FWCore.ParameterSet.Config as cms
process = cms.Process("ExoticaDQM")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.GlobalTag.globaltag = cms.string("111X_mcRun3_2021_realistic_v3")

process.load("DQM.Physics.ExoticaDQM_cfi")
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")


process.load('DQMOffline.Configuration.DQMOffline_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')

process.DQMStore.verbose = cms.untracked.int32(2)
process.dqmSaver.workflow = cms.untracked.string('/Physics/Exotica/TEST')
process.dqmSaver.convention = cms.untracked.string('RelVal')

## output
#Needed to the the plots locally

process.output = cms.OutputModule("PoolOutputModule",
  fileName       = cms.untracked.string('outputfilename.root'),
  outputCommands = cms.untracked.vstring(
    'drop *_*_*_*',
    'keep *_*_*_ExoticaDQM'
    ),
  splitLevel     = cms.untracked.int32(0),
  dataset = cms.untracked.PSet(
    dataTier   = cms.untracked.string(''),
    filterName = cms.untracked.string('')
  )
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)



process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
       #'/store/relval/CMSSW_8_0_1/JetHT/GEN-SIM-RECO/80X_dataRun2_relval_v3_rereco_RelVal_jetHT2015DReReco-v1/10000/FA5A1EA3-73ED-E511-9B51-0025905B8582.root',
       #'/store/data/Run2011A/MinimumBias/RAW/v1/000/165/121/0699429A-B37F-E011-A57A-0019B9F72D71.root',
       'file:/eos/cms/store/relval/CMSSW_11_1_0_pre6/RelValTTbar_14TeV/GEN-SIM-RECO/111X_mcRun3_2021_realistic_v3-v1/20000/77B9E4C5-C9F3-8D48-859A-1E8BB2494CAD.root'       
       #'/store/relval/CMSSW_8_0_1/RelValTTbar_13/GEN-SIM-DIGI-RECO/80X_mcRun2_asymptotic_v6_FastSim-v1/10000/0402D6BF-BAE4-E511-B293-00248C55CC7F.root',
    )
)

process.load('JetMETCorrections.Configuration.JetCorrectors_cff')

#process.p = cms.Path( process.ExoticaDQM + process.dqmSaver)
#process.p = cms.Path( process.dqmAk4PFCHSL1FastL2L3CorrectorChain + process.ExoticaDQM + process.dqmSaver)


## path definitions
process.p      = cms.Path(
    process.ExoticaDQM

)

process.endjob = cms.Path(
    process.endOfProcess
)

process.fanout = cms.EndPath(
    process.output
)


## schedule definition
process.schedule = cms.Schedule(
    process.p,
    process.endjob,
    process.fanout
)
                          


