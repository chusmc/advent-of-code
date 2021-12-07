type
    BingoNumber = object
        number: int
        marked: bool

proc mark(bingoNumber: var BingoNumber) = bingoNumber.marked = true

var
    bingoNumber : BingoNumber

bingoNumber.mark
echo "number: " ,bingoNumber