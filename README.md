# pps-alignment

## Installation
### 1. CMSSW
```
scram project CMSSW_11_2_0_pre6
cd CMSSW_11_2_0_pre6/src
cmsenv
git cms-init
git remote add ctpps git@github.com:CTPPS/cmssw.git
git fetch ctpps
git checkout -b alignment-test ctpps/pps-alignment-global
git cms-addpkg CalibPPS/AlignmentGlobal CalibPPS/ESProducers CondFormats/DataRecord CondFormats/PPSObjects
scram b -j 8
```
### 2. Data
```
cd ../../
git clone https://github.com/CTPPS/pps-alignment-data.git data
cd data
```
## Example
- year: 2018
- fill: 7334
- xangle: 130
- beta: 0.30
### 1. Reference dataset
```
cd 2018/alig-version-3/fill_6554/xangle_130_beta_0_30
cmsRun run_distributions_cfg.py
```
### 2. Test dataset
```
cd ../../../phys-version-1/fill_7334/xangle_130_beta_0_30
cmsRun run_distributions_cfg.py
cmsRun run_analysis_manual_cfg.py
```