from mmic.components.blueprints.generic_component import GenericComponent
from mmelemental.models.util.output import FileOutput
from mmelemental.models.util.input import FileInput
from mmic_param.models.input import ParamInput, ComputeInput
from typing import Dict, Any, List, Tuple, Optional

class PrepComponent(GenericComponent):
    """ A component for converting a Molecule object to a FileOutput. """
    @classmethod
    def input(cls):
        return ParamInput

    @classmethod
    def output(cls):
        return ComputeInput

    def execute(
        self,
        inputs: Dict[str, Any],
        extra_outfiles: Optional[List[str]] = None,
        extra_commands: Optional[List[str]] = None,
        scratch_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> Tuple[bool, Dict[str, Any]]:

        fname = FileOutput.rand_name() + '.pdb'
        inputs.mol.to_file(fname)

        mol = FileInput(path=fname)
        mol.read()

        return True, ComputeInput(mol=mol, forcefield=inputs.forcefield)
