from chives.types.blockchain_format.program import INFINITE_COST
from chives.types.spend_bundle import SpendBundle
from chives.types.generator_types import BlockGenerator
from chives.consensus.cost_calculator import calculate_cost_of_program, NPCResult
from chives.consensus.default_constants import DEFAULT_CONSTANTS
from chives.full_node.bundle_tools import simple_solution_generator
from chives.full_node.mempool_check_conditions import get_name_puzzle_conditions


def cost_of_spend_bundle(spend_bundle: SpendBundle) -> int:
    program: BlockGenerator = simple_solution_generator(spend_bundle)
    npc_result: NPCResult = get_name_puzzle_conditions(
        program, INFINITE_COST, cost_per_byte=DEFAULT_CONSTANTS.COST_PER_BYTE, safe_mode=True
    )
    cost: int = calculate_cost_of_program(program.program, npc_result, DEFAULT_CONSTANTS.COST_PER_BYTE)
    return cost
