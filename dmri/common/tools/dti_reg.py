from dmri.common.tools.base import ExternalToolWrapper

class DTIReg(ExternalToolWrapper):
    def __init__(self,binary_path):
        super().__init__(binary_path)

    