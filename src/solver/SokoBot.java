package solver;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URL;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class SokoBot {

    /**
     * Bot can move
     * l - left
     * r - right
     * u - up
     * d - down
     */
    public String solveSokobanPuzzle(int width, int height, char[][] mapData, char[][] itemsData) {
//        PythonInterpreter Python_Interpreter = new PythonInterpreter();
//        Python_Interpreter.set("mapData", mapData);
//        Python_Interpreter.set("itemsData", itemsData);
//        Python_Interpreter.execfile("Python_Files/STree.py");


        try {
            return getSolution(width, height, mapData, itemsData);
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
    }

    private String getSolution(int width, int height, char[][] mapData, char[][] itemsData) throws IOException, InterruptedException {

        HttpClient httpClient = HttpClient.newBuilder().version(HttpClient.Version.HTTP_2).build();
    
        StringBuffer content = new StringBuffer();
    
        // form parameters
        Map<String, String> data = new HashMap<>();
        data.put("width", Integer.toString(width));
        data.put("height", Integer.toString(height));
        data.put("mapData", Arrays.deepToString(mapData));
        data.put("itemsData", Arrays.deepToString(itemsData));
    
        HttpRequest request = HttpRequest.newBuilder().POST(buildFormDataFromMap(data))
                .uri(URI.create("http://127.0.0.1:5000/solver"))
                .setHeader("User-Agent", "Java 11 HttpClient Bot") // add request header
                .header("Content-Type", "application/x-www-form-urlencoded").build();
    
        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
    
        return response.body().isEmpty() ? "" : response.body();
    }
    
    private HttpRequest.BodyPublisher buildFormDataFromMap(Map<String, String> data) {
        var builder = new StringBuilder();
        for (Map.Entry<String, String> entry : data.entrySet()) {
            if (!builder.isEmpty()) {
                builder.append("&");
            }
            builder.append(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8));
            builder.append("=");
            builder.append(URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
        }
        System.out.println(builder.toString());
        return HttpRequest.BodyPublishers.ofString(builder.toString());
    }
}