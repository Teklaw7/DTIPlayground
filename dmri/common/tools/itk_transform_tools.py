from dmri.common.tools.base import ExternalToolWrapper

class ITKTransformTools(ExternalToolWrapper):
    def __init__(self,binary_path):
        super().__init__(binary_path)

    