import sys


def main(filename):
    with open(filename, 'r') as f:
        content = ''.join(f.readlines())
        compile_code(content)


def compile_code(code):
    current_idx = 0
    loop_idx = []
    cells = [0]
    cell_idx = 0

    while current_idx < len(code):
        token = code[current_idx]

        if token == '+':
            cells[cell_idx] += 1
        elif token == '-':
            cells[cell_idx] -= 1
        elif token == '>':
            cell_idx += 1

            if cell_idx >= len(cells):
                cells.append(0)

        elif token == '<':
            cell_idx -= 1

            if cell_idx < 0:
                raise Exception('RANGE ERROR')

        elif token == '[':
            loop_idx.append(current_idx)

        elif token == ']':
            if cells[cell_idx] == 0:
                current_idx += 1
                continue

            current_idx = loop_idx[len(loop_idx) - 1] - 1
            loop_idx = loop_idx[:-1]

        elif token == '.':
            if not 0 <= cells[cell_idx] <= 127:
                raise Exception('RANGE ERROR')

            print(chr(cells[cell_idx]), end='')

        current_idx += 1


if __name__ == '__main__':
    main(sys.argv[1])
