//package solver;
//
//import java.util.Date;
//import java.util.Queue;
//import java.util.LinkedList;
//import java.io.File;
//import java.io.FileWriter;
//import java.io.IOException;
//import java.io.BufferedWriter;
//
//public class StateTree {
//    private static boolean JUSTKEEPSWIMMING = true;
//    private State root;
//
//    public StateTree(MapData root_mapData, ItemsData root_itemsData) {
//        this.root = new State(root_mapData, root_itemsData);
//        this.clean_log();
//    }
//
//    private void clean_log() {
//        try {
//            File logFile = new File("log.txt");
//            BufferedWriter writer = new BufferedWriter(new FileWriter(logFile));
//            writer.write(new Date().toString());
//            writer.newLine();
//            writer.close();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }
//
//    public State get_root() {
//        return this.root;
//    }
//
//    public static Object[] solution(State solution, int generated, int repeated, int fringe, int seen, Date start) {
//        JUSTKEEPSWIMMING = false;
//        long time = (new Date().getTime() - start.getTime()) / 1000;
//        return new Object[]{
//                solution.get_path(),
//                "\n",
//                "Generated: " + generated,
//                "Repeated: " + repeated,
//                "Fringe: " + fringe,
//                "Explored: " + seen,
//                "Duration: " + time
//        };
//    }
//
//    public static Object[] failure() {
//        return new Object[]{"Search Completed and No Solution Found"};
//    }
//
//    public Object[] bfs() {
//        JUSTKEEPSWIMMING = true;
//        Date start = new Date();
//        int rep = 0;
//        int gen = 1;
//        State node = this.root;
//        Set<State> explored = new HashSet<>();
//        Queue<State> frontier = new LinkedList<>();
//        frontier.add(node);
//        if (node.is_goal()) {
//            return solution(node, gen, rep, frontier.size(), explored.size(), start);
//        }
//        while (JUSTKEEPSWIMMING) {
//            if (frontier.isEmpty()) {
//                return failure();
//            }
//        }
//    }
//}
