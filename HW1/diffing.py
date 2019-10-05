# TODO: Your name, Cornell NetID
# TODO: Your Partner's name, Cornell NetID

import dynamic_programming

# DO NOT CHANGE THIS CLASS
class DiffingCell:
    def __init__(self, s_char, t_char, cost):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)"%(self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
def fill_cell(table, i, j, s, t, cost):
    s = "-" + s
    t = "-" + t
    currentCost = costfunc(s[i], t[j])
    if (i == 0 and j == 0 ) or (i == 0 and j == 1) or (j == 0 and i == 1):
        return DiffingCell(s[i], t[j], currentCost)
    if (i == 0):
        cellLeft = table.get(i, j-1).cost
        return DiffingCell(s[i], t[j], cellLeft + currentCost)
    if (j == 0):
        cellUp = table.get(i-1, j).cost
        return DiffingCell(s[i], t[j], cellUp + currentCost)
    else:
        cellLeft = table.get(i, j-1).cost
        cellUp = table.get(i-1, j).cost
        cellDiag = table.get(i-1, j-1).cost
        costDashUp = costfunc(s[0], t[j])
        costDashLeft = costfunc(s[i], t[0])
        minimum = min(cellLeft + costDashUp, cellDiag + currentCost, cellUp + costDashLeft)
        return DiffingCell(s[i], t[j] , minimum)
    return DiffingCell(s[i], t[j] , minimum)

# Input: n and m, represents the sizes of s and t respectively.
# Should return a list of (i,j) tuples, in the order you would like fill_cell to be called
def cell_ordering(n,m):
    return [(a, b) for a in range(n+1) for b in range(m+1)]

# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.
def diff_from_table(s, t, table):
    # TODO: YOUR CODE HERE
    print_table(table._table)
    return (0, "", "")

def print_table(table):
    print("-----")
    for row in table:
        print(row)    

# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char: return 0
        if s_char == 'a':
            if t_char == 'b': return 5
            if t_char == 'c': return 3
            if t_char == '-': return 2
        if s_char == 'b':
            if t_char == 'a': return 1
            if t_char == 'c': return 4
            if t_char == '-': return 2
        if s_char == 'c':
            if t_char == 'a': return 5
            if t_char == 'b': return 5
            if t_char == '-': return 1
        if s_char == '-':
            if t_char == 'a': return 3
            if t_char == 'b': return 3
            if t_char == 'c': return 3

    import dynamic_programming
    s = "acb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t, cost=costfunc)
    (cost, align_s, align_t) = diff_from_table(s,t, D)
    print align_s
    print align_t
    print "cost was %d"%cost
