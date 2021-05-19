# DTI Playground 

DTI Playground are python based NIRAL pipeline software including DMRIPrep (dmriprep), DTIAtlasBuilder (dmriatlasbuilder), DTIFiberAnalyzer (dmrifiberanalyzer)

### DMRIPrep Usage (dmriprep)

dmriprep is a tool that performs quality control over diffusion weighted images. Quality control is very essential preprocess in DTI research, in which the bad gradients with artifacts are to be excluded or corrected by using various computational methods. The software and library provides a module based package with which users can make his own QC pipeline as well as new pipeline modules.

#### CLI Mode :

1. **init** - Initialize configuration (default: `$HOME/.niral-dti/dmriprep`)

**init** command generates the configuration directory and files with following command. One just needs to execute this command only once unless a different configuration is needed.
```
    $ dmriprep init 
```
If you want to set different directory other than default one :
```
    $ dmriprep --config-dir my/config/dir init 
```
Once run, `config.yml` and `environment.yml` will be in the directory. 

2. **update** - Update if `config.yml` has been changed (e.g. in case of adding user module directory).
Changing `config.yml` file should be followed by updating `environment.yml` with running update command :
```
    $ dmriprep [--config-dir my/config/dir] update
```
This will update module-specific informations such as binary locations or package location used by the corresponding module. It simply updates `environment.yml`

3. **make-protocols** - Generating a default protocol file

The first thing to do QC is to generate default protocol file that has pipeline information.
```
    $ dmriprep make-protocols -i IMAGE_FILENAME [-o OUTPUT_FILENAME_] [-d MODULE1 MODULE2 ... ]
```
if `"-o"` option is omitted, the output protocol will be printed on terminal.`"-d"` option specifies the list of modules for the QC, with which command will generate the default pipeline and protocols of the sequence. Same module can be used redundantly. If `"-d"` option is not specified, the default pipeline will be generated from the file `protocol_template.yml` . You can change the default pipeline in `protocol_template.yml` file

4. **run** - Running pipeline 
To run with default protocol generated from `protocol_template.yml`:

```
    $ dmriprep run -i IMAGE_FILE -o OUTPUT_DIR -d [ MODULE1 MODULE2 ... ]
```
`"-d"` option (default protocol) works as described in **make-protocols** command. But you need to specify `"-d"` for the default pipeline from the template.  If `"-o"` option is omitted, default directory will be set to `Image filename_QC`.

To run with existing protocol file:
```
    $ dmriprep run -i IMAGE_FILE -p PROTOCOL_FILE -o output/directory/
```

`"-p"` option cannot be used with `"-d"` option.

 

#### GUI Mode :

```
    $ dmriprep image_file -p protocol --gui
```

#### Server Mode:
```
    $ dmriprep --server --port 4000
```


### Supported Images

- NRRD 
- NIFTI

### DTIAtlasBuilder Usage (dtiab)

DTIAtlasBuilder is a software to make an atlas from multiple diffusion weighted images. It performs affine/diffeomorphic registrations and finally generates the atlas for all the reference image. 

### DTIFiberAnalyzer Usage (dtifa)

DTIFiberAnalyzer performs statistical computation over the extracted fibers. This enables researchers to get the information of the fiber images easily and fast.

### Developement 

#### Author

- SK Park -  Neuro Image Research and Analysis Laboratory , University of North Carolina @ Chapel Hill

#### References

- [Quality Control of Diffusion Weighted Images - Zhexing Liu, et al](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3864968/)


#### Acknowlegements

DTI Toolkits are funded by National Institute of Health (NIH)

#### LICENSE

MIT

#### Requirements

##### Application required

- Python >= 3.6 
- FSL >= 6.0 (Required for the eddy tools which perform eddymotion/suceptibility correction)

##### Python libraries
- pynrrd==0.4.2
- dipy==1.4.0
- pyyaml==5.3.1

### Todos
- Docker distribution with NIRAL toolchain and FSL 
- Distributed computing - Celery 
- Server mode - Flask 
- GUI client (Single page web app) - Vuejs, React, ...
- FSL integration
- Multi threading
- NIFTI writing
- NRRD-NIFTI conversion
- Output generations for dmriprepModule
- Abstract one more level for dmriprep.module.postProcess (Currently baseline averaging module override the postProcess method due to the forced writing which makes the next module load the file after first run. In the first run, object id is passed.) - Done (2021-04-21)

### Change Log

##### 2021-05-19
- dtiatlasbuilder : 1st refactoring is finished. 

##### 2021-05-14
- dtiatlasbuilder : ported to python3, refactoring

##### 2021-04-21
- dmriprep : Baseline average implemented (DirectAverage, BaselineOptimized)
- dmriprep : Optionalized pipeline implemented 
- dmriprep : dmriprep cli implemented
- dmriprep : initial configuration directory management (default $HOME/.niral-dti/dmriprep)
- dmriprep : Minor bug fixed

##### 2021-04-18
- dmriprep : Slicewise check implemented
- dmriprep : Interlace check implemented
- dmriprep : Continuation from stopped point has been implemented , but if image itself is deformed it won't work. It only has ability to track exclusion of gradients yet.
- dmriprep : Colored output is enabled with the logger. (dmriprep.Color.WARNING, dmriprep.Color.OK ... thingks like that look in __init__.py of dmriprep module)

##### 2021-04-15
- dmriprep : Sequential Pipelining implemented

##### 2021-04-09
- dmriprep : New protocol format (YAML)
- dmriprep : New protocol template (YAML)

##### 2021-04-01
- dmriprep : Deveopement initiated
