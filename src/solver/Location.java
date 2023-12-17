package solver;

public class Location {
    private int column;
    private int row;

    public Location(int column, int row) {
        this.column = column;
        this.row = row;
    }

    public void setLocation(int column, int row) {
        this.column = column;
        this.row = row;
    }

    public int getColumn() {
        return column;
    }

    public void setColumn(int column) {
        this.column = column;
    }

    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }
}
