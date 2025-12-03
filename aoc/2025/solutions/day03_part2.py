def solve(data: list[str]) -> int:
    """
    For each bank of battery joltages, select twelve digits in order that form
    the largest possible twelve-digit number. Return the sum of these maximum
    joltages across all banks.
    """

    keep = 12
    total = 0

    for line in data:
        stack = []
        to_remove = len(line) - keep
        for ch in line:
            while to_remove > 0 and stack and stack[-1] < ch:
                stack.pop()
                to_remove -= 1
            stack.append(ch)
        total += int(''.join(stack[:keep]))


    return total
