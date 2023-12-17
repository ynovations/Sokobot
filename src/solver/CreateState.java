//package solver;
//
//public class CreateState {
//    private int[][] mapData;
//    private int[][] itemsData;
//    private CreateState parent;
//    private int cost;
//    private String path;
//    private String stateString;
//    private Integer x;
//    private Integer y;
//
//    public CreateState(char[][] mapData, char[][] itemsData, CreateState par, String dir) {
//        if (par == null && dir == null) {
//            // Initialization for the initial state
//            // 2D Deep Copy
//            this.mapData = new int[mapData.length][];
//            for (int i = 0; i < mapData.length; i++) {
//                this.mapData[i] = new int[mapData[i].length];
//                for (int j = 0; j < mapData[i].length; j++) {
//                    this.mapData[i][j] = mapData[i][j];
//                }
//            }
//            this.itemsData = new int[itemsData.length][];
//            for (int i = 0; i < itemsData.length; i++) {
//                this.itemsData[i] = new int[itemsData[i].length];
//                for (int j = 0; j < itemsData[i].length; j++) {
//                    this.itemsData[i][j] = itemsData[i][j];
//                }
//            }
//            this.parent = null;
//            this.cost = 0;
//            this.path = "";
//            this.stateString = "";
//            this.x = null;
//            this.y = null;
//            this.findPlayerPosition(this.mapData, this.itemsData);
//
//            for (int i = 0; i < itemsData.length; i++) {
//                for (int j = 0; j < itemsData[i].length; j++) {
//                    this.stateString.concat(String.valueOf(itemsData[i][j]));
//                }
//            }
//
//        } else {
//            this.childFromParent(par, dir);
//        }
//    }
//
//    private Location findPlayerPosition(int[][] mapData, int[][] itemsData) {
//        for (int i = 0; i < mapData.length; i++) {
//            for (int j = 0; j < mapData[i].length; j++) {
//                if (itemsData[i][j] == Item.PLAYER) {
////                    this.x = i;  // Store the player's x position
////                    this.y = j;  // Store the player's y position
//                    return new Location(i, j);
//                }
//            }
//        }
//    }
//
//    private void childFromParent(CreateState par, String dir) {
//
//        // Initialization for subsequent states
//        this.parent = par;
//        this.cost = par.cost + 1;
//        this.path = par.path + dir;
//
//        // Make the move
//        char[][] tmp_items_data = move_player(par, dir);
//        this.itemsData = new char[tmp_items_data.length][tmp_items_data[0].length];
//        for (int i = 0; i < tmp_items_data.length; i++) {
//            for (int j = 0; j < tmp_items_data[0].length; j++) {
//                this.itemsData[i][j] = tmp_items_data[i][j];
//            }
//        }
//
//        if (dir.equals("u")) {
//            this.x = par.x - 1;
//            this.y = par.y;
//        } else if (dir.equals("d")) {
//            this.x = par.x + 1;
//            this.y = par.y;
//        } else if (dir.equals("l")) {
//            this.x = par.x;
//            this.y = par.y - 1;
//        } else if (dir.equals("r")) {
//            this.x = par.x;
//            this.y = par.y + 1;
//        }
//
//        // 2D deep copy
//        this.mapData = new char[par.mapData.length][par.mapData[0].length];
//        for (int i = 0; i < par.mapData.length; i++) {
//            for (int j = 0; j < par.mapData[0].length; j++) {
//                this.mapData[i][j] = par.mapData[i][j];
//            }
//        }
//
//        // Recompute the statestring
//        this.stateString = "";
//        for (char[] row : this.itemsData) {
//            for (char c : row) {
//                this.stateString += c;
//            }
//        }
//
//    }
//
//}
