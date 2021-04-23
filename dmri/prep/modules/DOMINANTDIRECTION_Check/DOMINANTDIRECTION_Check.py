
import dmri.prep.modules as modules 
import dmri.prep as prep
import yaml

logger=prep.logger.write

class DOMINANTDIRECTION_Check(prep.modules.DTIPrepModule):
    def __init__(self,*args,**kwargs):
        super().__init__(DOMINANTDIRECTION_Check)

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