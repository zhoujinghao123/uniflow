import traceback
from typing import Any, Mapping,Sequence
from uniflow.node import Node
from uniflow.op.op import Op

class ExpandOp(Op):
    def expand(self,root_node: Mapping[str, Any]) :
        expand_1_node = {}
        expand_2_node = {}
        keys = list(root_node.keys())
        length = len(root_node) // 2
        try:
            expand_1_node = {k: root_node[k] for k in keys[0:length]}
            expand_2_node = {j: root_node[j] for j in keys[length:len(root_node)]}

        except Exception as e:
            traceback.print_exc()

        return expand_1_node,expand_2_node

    def expand_1(self,root_node: Mapping[str, Any]):
        expand_1_node = self.expand(root_node)[0]
        return expand_1_node

    def expand_2(self,root_node: Mapping[str, Any]):
        expand_2_node = self.expand(root_node)[1]
        return expand_2_node

    def __call__(self, *args: Sequence[Node]) -> Sequence[Node]:
        """Call op."""
        raise NotImplementedError("Not implemented yet.")