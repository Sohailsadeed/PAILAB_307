import java.util.*;

public class ThreeJugProblem {

    // ---------- STATE CLASS ----------
    static class State {
        int a, b, c;

        State(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        @Override
        public boolean equals(Object o) {
            if (!(o instanceof State)) return false;
            State s = (State) o;
            return a == s.a && b == s.b && c == s.c;
        }

        @Override
        public int hashCode() {
            return Objects.hash(a, b, c);
        }

        @Override
        public String toString() {
            return "(" + a + ", " + b + ", " + c + ")";
        }
    }

    // ---------- BFS SOLUTION ----------
    public static boolean solveBFS(int A, int B, int C, int D) {
        Queue<State> queue = new LinkedList<>();
        Set<State> visited = new HashSet<>();

        State start = new State(0, 0, C);
        queue.add(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            State cur = queue.poll();

            if (cur.a == D || cur.b == D || cur.c == D) {
                System.out.println("BFS reached: " + cur);
                return true;
            }

            for (State next : generateNext(cur, A, B, C)) {
                if (!visited.contains(next)) {
                    visited.add(next);
                    queue.add(next);
                }
            }
        }
        return false;
    }

    // ---------- DFS SOLUTION ----------
    public static boolean solveDFS(int A, int B, int C, int D) {
        Set<State> visited = new HashSet<>();
        State start = new State(0, 0, C);
        return dfs(start, A, B, C, D, visited);
    }

    private static boolean dfs(State cur, int A, int B, int C, int D, Set<State> visited) {
        if (visited.contains(cur)) return false;
        visited.add(cur);

        if (cur.a == D || cur.b == D || cur.c == D) {
            System.out.println("DFS reached: " + cur);
            return true;
        }

        for (State next : generateNext(cur, A, B, C)) {
            if (dfs(next, A, B, C, D, visited)) {
                return true;
            }
        }
        return false;
    }

    // ---------- MOVE GENERATOR ----------
    private static List<State> generateNext(State s, int A, int B, int C) {
        List<State> list = new ArrayList<>();
        int a = s.a, b = s.b, c = s.c;

        // Fill
        list.add(new State(A, b, c));
        list.add(new State(a, B, c));
        list.add(new State(a, b, C));

        // Empty
        list.add(new State(0, b, c));
        list.add(new State(a, 0, c));
        list.add(new State(a, b, 0));

        // Pour operations
        int pour;

        pour = Math.min(a, B - b);
        list.add(new State(a - pour, b + pour, c));

        pour = Math.min(a, C - c);
        list.add(new State(a - pour, b, c + pour));

        pour = Math.min(b, A - a);
        list.add(new State(a + pour, b - pour, c));

        pour = Math.min(b, C - c);
        list.add(new State(a, b - pour, c + pour));

        pour = Math.min(c, A - a);
        list.add(new State(a + pour, b, c - pour));

        pour = Math.min(c, B - b);
        list.add(new State(a, b + pour, c - pour));

        return list;
    }

    // ---------- MAIN ----------
    public static void main(String[] args) {
        int A = 8, B = 5, C = 3, D = 4;

        System.out.println("Using BFS:");
        System.out.println(solveBFS(A, B, C, D));

        System.out.println("\nUsing DFS:");
        System.out.println(solveDFS(A, B, C, D));
    }
}
