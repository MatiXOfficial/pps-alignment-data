# Example configurations of global alignment

## Installation
### 1. CMSSW
```
scram project CMSSW_12_0_0_pre1
cd CMSSW_12_0_0_pre1/src
cmsenv
git cms-init
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
Now we perform an analysis of the test dataset. Firstly, we fill the histograms (`run_distributions_cfg.py`). This should take about 2 minutes. Then we analyse the histograms and produce the alignment constants (`run_analysis_cfg.py`). This should take a few seconds.
```
cd ../../../phys-version-1/fill_7334/xangle_130_beta_0_30
cmsRun run_distributions_cfg.py
cmsRun run_analysis_cfg.py
```
## Local DB example
Now, we will use SQLite files as Conditions input and output.

Configuration:
- year: 2018
- fill: 7334
- xangle: 160
- beta: 0.30

### 1. Reference dataset
Reference dataset analysis ought to be done by an expert. We can assume that we already have the DQM files with the reference plots. Here we can produce them without DB integration (as in the previous example).
```
cd 2018/alig-version-3/fill_6554/xangle_160_beta_0_30
cmsRun run_distributions_cfg.py
```
Now we can write an SQLite file with the reference config. It will include the reference data for the horizontal alignment (matching graphs).
```
cmsRun write_config_cfg.py
```

### 2. Test dataset
At first, we have to write an SQLite file with the config.
```
cd ../../../phys-version-1/fill_7334/xangle_160_beta_0_30
cmsRun ../../../../write_config_cfg.py
```
After that, we need to modify the configs so that they use the SQLite file.
1. In `run_distributions_cfg.py`: change `conditions_input` to `sqlite_local`.
2. In `run_analysis_cfg.py`: change `conditions_input` and `conditions_input_reference` to `sqlite_local`.
3. To write alignment results to an SQLite file too, change `write_sqlite_results` to True in `run_analysis_cfg.py`.

Now we perform an analysis of the test dataset.
```
cmsRun run_distributions_cfg.py
cmsRun run_analysis_cfg.py
```
If `write_sqlite_results` was set to `True`, an SQLite file with the results has been produced. To retrieve the results, use:
```
cmsRun ../../../../retrieve_CTPPSRPAlignmentCorrectionsData.py 325159
```
First argument is the run number. A `.log` file with the results should be produced.

## Online DB example
Configs for fill 7334, xangle 160 have been uploaded to the conditions DB with the tag `PPSAlignmentConfig_test_v1_prompt`

Configuration:
- year: 2018
- fill: 7334
- xangle: 160
- beta: 0.30

### 1. Reference dataset
Here, we don't have to do anything, since the reference data will be delivered from the DB.

### 2. Test dataset
```
cd 2018/phys-version-1/fill_7334/xangle_160_beta_0_30
```

We need to modify the configs so that they retrieve conditions from the DB.
1. In `run_distributions_cfg.py`: change `conditions_input` to `db`.
2. In `run_analysis_cfg.py`: change `conditions_input` and `conditions_input_reference` to `db`.
3. We can handle writing results to an SQLite file in the same way as in the previous example.

Now we perform an analysis of the test dataset.
```
cmsRun run_distributions_cfg.py
cmsRun run_analysis_cfg.py
```
