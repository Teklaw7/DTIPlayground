

  
import dmri.prep as prep

import yaml
from pathlib import Path 
import SUSCEPTIBILITY_Correct.utils as utils

logger=prep.logger.write


class SUSCEPTIBILITY_Correct(prep.modules.DTIPrepModule):
    def __init__(self,*args,**kwargs):
        super().__init__(SUSCEPTIBILITY_Correct)

    def generateDefaultEnvironment(self):
        #find fsl path 
        fsldir, fsl_version=utils.find_fsl(['/usr/bin','/mnt/sdb1/scalphunter/bin'])
        res={'fsl_path': fsldir, 'fsl_version' : fsl_version}
        return res
    
    def checkDependency(self,environment): #use information in template, check if this module can be processed
        # FSL should be ready before execution
        if self.name in environment:
            try:
                fslpath=Path(environment[self.name]['fsl_path'])
                fsl_exists=fslpath.exists()
                if fsl_exists:
                    return True, None 
                else:
                    return False, "FSL Path doesn't exist : {}".format(str(fslpath))
            except Exception as e:
                return False, "Exception in finding FSL6 : {}".format(str(e))
        else:
            return False, "Can't locate FSL" #test

    def generateDefaultProtocol(self,image_obj):
        super().generateDefaultProtocol(image_obj)
        ## todos
        return self.protocol

    def process(self): ## self.result_history, self.result , self.template , self.protocol 
        super().process()
        inputParams=self.getPreviousResult()['output']
        logger("NOT IMPLEMENTED YET",prep.Color.ERROR)

        self.result['output']['success']=True
        return self.result