from copy import deepcopy
from common.game_console import GameConsole

# answer to part one: 1654
# answer to part two: 833
if __name__ == '__main__':
    with open('inputs/day_8.txt', 'r') as file:
        lines = file.readlines()
    lines = map(str.strip, lines)
    instructions = list(map(lambda x: x.split(' '), lines))

    game_console = GameConsole(instructions)
    run_instructions = []
    while True:
        run_instructions.append(game_console.get_instruction_index())
        game_console.run_one_instruction()
        if game_console.get_instruction_index() in run_instructions:
            break

    print(f'answer to part one: {game_console.get_accumulator()}')

    done = False
    limit = 100
    for i, [instruction, _] in enumerate(instructions):
        game_console = GameConsole(instructions)
        if instruction == 'nop':
            game_console.instructions[i][0] = 'jmp'
        elif instruction == 'jmp':
            game_console.instructions[i][0] = 'nop'

        counter = 0
        while True:
            if game_console.get_instruction_index() >= len(instructions):
                done = True
                break
            game_console.run_one_instruction()
            if counter > 100:
                break
            counter += 1
        if done is True:
            break
    print(f'answer to part two: {game_console.get_accumulator()}')

