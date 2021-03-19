# Example configurations of global alignment

## Installation
### 1. CMSSW
```
scram project CMSSW_11_3_0_pre4
cd CMSSW_11_3_0_pre4/src
cmsenv
git cms-init
git cms-addpkg CalibPPS/AlignmentGlobal CalibPPS/ESProducers CondFormats/DataRecord CondFormats/PPSObjects
scram b -j 8
```
There might be a newer version of global alignment software at `pps-alignment-global` branch from CTPPS.
```
git remote add ctpps git@github.com:CTPPS/cmssw.git
git fetch ctpps
git checkout -b pps-alignment-global ctpps/pps-alignment-global
scram b -j 8
```

### 2. Data
```
cd ../../
git clone https://github.com/CTPPS/pps-alignment-data.git data
cd data
```

## Example
Configuration:
- year: 2018
- fill: 7334
- xangle: 130
- beta: 0.30
### 1. Reference dataset
At first we need to produce some necessary plots using the reference dataset. Note that it has already been aligned. The process should take about 15 minutes.
```
cd 2018/alig-version-3/fill_6554/xangle_130_beta_0_30
cmsRun run_distributions_cfg.py
```
### 2. Test dataset
Now we perform an analysis of the test dataset. Firstly, we fill the histograms (`run_distributions_cfg.py`). This should take about 2 minutes. Then we analyse the histograms and produce the alignment constants (`run_analysis_manual_cfg.py`). This should take a few seconds.
```
cd ../../../phys-version-1/fill_7334/xangle_130_beta_0_30
cmsRun run_distributions_cfg.py
cmsRun run_analysis_manual_cfg.py
```