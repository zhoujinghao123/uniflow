import traceback
from typing import Any, Mapping,Sequence
from uniflow.node import Node
from uniflow.op.op import Op

class ReduceOp(Op):
    def merge(self,expand_1: Mapping[str, Any],expand_2: Mapping[str, Any]) :
        merged_dict = {}
        expand_1_keys = list(expand_1.keys())
        expand_2_keys = list(expand_2.keys())
        try:
            for i in range(0, len(expand_1)):
                merged_key = f"{expand_1_keys[i]} {expand_2_keys[i]}"
                merged_value = f"{expand_1[expand_1_keys[i]]} {expand_2[expand_2_keys[i]]}"
                merged_dict[merged_key] = merged_value
        except Exception as e:
            traceback.print_exc()

        return merged_dict


    def __call__(self, *args: Sequence[Node]) -> Sequence[Node]:
        """Call op."""
        raise NotImplementedError("Not implemented yet.")