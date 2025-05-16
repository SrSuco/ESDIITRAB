import java.util.*;

public class GrafoValido {

    public static boolean grafoNaoDirecionadoValido(List<List<Integer>> grafo) {
        int V = grafo.size();

        for (int no = 0; no < V; no++) {
            List<Integer> vizinhos = grafo.get(no);
            Set<Integer> vistos = new HashSet<>();

            for (int vizinho : vizinhos) {
                if (vizinho < 0 || vizinho >= V) {
                    return false;
                }

                if (vizinho == no) {
                    return false;
                }

                if (!vistos.add(vizinho)) {
                    return false;
                }

                if (!grafo.get(vizinho).contains(no)) {
                    return false;
                }
            }
        }

        return true;
    }

    public static void main(String[] args) {
        List<List<Integer>> grafoValido = Arrays.asList(
            Arrays.asList(1, 2),
            Arrays.asList(0, 2),
            Arrays.asList(0, 1)
        );

        List<List<Integer>> grafoInvalido = Arrays.asList(
            Arrays.asList(0, 1),
            Arrays.asList(0)
        );

        System.out.println("Grafo válido? " + grafoNaoDirecionadoValido(grafoValido));     // true
        System.out.println("Grafo válido? " + grafoNaoDirecionadoValido(grafoInvalido));   // false
    }
}
