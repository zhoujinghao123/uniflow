from uniflow.flow.flow import Flow
from typing import Any, Mapping,Sequence
from expand_op import ExpandOp
from reduce_op import ReduceOp

class ExpandReduceFlow(Flow):
    def expand(self,root_node: Mapping[str, Any],name:str):
        expand_op = ExpandOp(name)
        expand_1_node = expand_op.expand_1(root_node)
        expand_2_node = expand_op.expand_2(root_node)

        return expand_1_node,expand_2_node

    def reduce(self,expand_1_node: Mapping[str, Any],expand_2_node: Mapping[str, Any],name:str):
        merge_dict = ReduceOp(name)
        result = merge_dict.merge(expand_1_node,expand_2_node)
        return result