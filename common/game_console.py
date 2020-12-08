from typing import List
from copy import deepcopy


class GameConsole:
    def __init__(self, instructions: List[List[str]]):
        self.instructions = deepcopy(instructions)
        self.accumulator = 0
        self.instruction_index = 0

    def run_one_instruction(self):
        [instruction, argument] = self.instructions[self.instruction_index]
        if instruction == 'acc':
            self.instruction_index += 1
            self.accumulator += int(argument)
        elif instruction == 'jmp':
            self.instruction_index += int(argument)
        elif instruction == 'nop':
            self.instruction_index += 1

    def get_accumulator(self) -> int:
        return deepcopy(self.accumulator)

    def get_instruction_index(self) -> int:
        return deepcopy(self.instruction_index)
