//package solver;
//
//import java.util.ArrayList;
//import java.util.HashMap;
//import java.util.List;
//import java.util.Map;
//
//public class MovePlayer {
//    public static void main(String[] args) {
//        // Define the move direction
//        String dir = "u"; // Change this to 'd', 'l', or 'r' for down, left, and right moves respectively
//
//        // Define the old map and items
//        Map<String, String> old_map = new HashMap<>();
//        Map<String, String> old_items = new HashMap<>();
//
//        // Define the new map and items
//        Map<String, String> new_map = new HashMap<>();
//        Map<String, String> new_items = new HashMap<>();
//
//        // Define the player position
//        String x = "x"; // Change this to the player's x-coordinate
//        String y = "y"; // Change this to the player's y-coordinate
//
//        // Define the cost
//        int cost = 0; // Initialize the cost to zero
//
//        // Find the player's position in the old map
//        String posX = old_map.get(x);
//        String posY = old_map.get(y);
//
//        // Update the new map and items
//        if (posX != null && posY != null) {
//            if (dir.equals("u")) {
//                // Check if there is a box above the player
//                if (old_items.get(posX + " " + posY).equals("$")) {
//                    cost++;
//                    if (old_map.get(posX + " " + (posY - 2)).equals(" ")) {
//                        new_items.put(posX + " " + (posY - 2), "$");
//                        new_items.put(posX + " " + posY, "@");
//                        new_map.put(posX + " " + posY, " ");
//                    }
//                }
//                if (old_map.get(posX + " " + (posY - 2)).equals(" ")) {
//                    new_items.put(posX + " " + (posY - 2), "@");
//                    new_map.put(posX + " " + posY, " ");
//                }
//            }
//            if (dir.equals("d"))
