class BingoNumber
    def initialize(@number : Int32, @marked : Bool)
    end

    def number
        @number
    end

    def marked?
        @marked
    end

    def mark
        @marked = true
    end
end

class BingoBoard
    @last_marked : BingoNumber?
    @number_of_rows : Int32
    @board_numbers : Array(BingoNumber)
    def initialize(@row_size : Int32, numbers : Array(Int32))
        @number_of_rows = (numbers.size // row_size)
        @board_numbers = numbers.map { |n| BingoNumber.new n, false }
    end

    def mark_number(number)
        @board_numbers.find { |bn| bn.number == number }.try do |n| 
            n.mark
            @last_marked = n
        end
    end

    def is_winner?
        (0..@number_of_rows-1).each do |r| 
            c = 0
            while c < @row_size && @board_numbers[r * @row_size + c].marked?
                c += 1
            end
            return true if c == @row_size
        end
        
        
        (0..@row_size-1).each do |c| 
            r = 0
            while r < @number_of_rows && @board_numbers[r * @row_size + c].marked?
                r += 1
            end
            return true if r == @number_of_rows
        end

        return false
    end

    def score
        return @board_numbers.select { |bn| !bn.marked? }.map { |bn| bn.number }.sum * @last_marked.not_nil!.number
    end
    
end
    
   
boards = [] of BingoBoard
board_numbers = [] of Int32

file = File.open("input.txt").each_line
draw = file.next.to_s.split(',').map &.to_i 

file.each do |line|
    if line.strip.empty?
        if !board_numbers.empty?
            boards << BingoBoard.new(5, board_numbers)
            board_numbers = [] of Int32
        end
    else
        board_numbers += line.split.map &.to_i
    end
end
if !board_numbers.empty?
    boards << BingoBoard.new(5, board_numbers)
end


draw.each do |draw_number|
    boards.each do |board|
        board.mark_number(draw_number)
        if board.is_winner?
            print "solution: ", board.score, "\n"
            exit
        end
    end

end

