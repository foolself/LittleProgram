import java.net.*;
import java.util.*;
import java.io.*;

class TulingRobot {
	private static String APIKEY = "YOUR KEY";

	public static void main(String[] args) throws IOException {
		String input = "你好啊";
		String INFO = URLEncoder.encode(input, "utf-8");
		String getURL = "http://www.tuling123.com/openapi/api?key=" + APIKEY + "&info=" + INFO;
		URL getUrl = new URL(getURL);
		HttpURLConnection connection = (HttpURLConnection) getUrl.openConnection();
		connection.connect();

		// 取得输入流，并使用Reader读取
		BufferedReader reader = new BufferedReader(new InputStreamReader( connection.getInputStream(), "utf-8"));
		StringBuffer sb = new StringBuffer();
		String line = "";
		while ((line = reader.readLine()) != null) {
			sb.append(line);
		}
		reader.close();
		// 断开连接
		connection.disconnect();
		String result = sb.toString();
		String[] results = new String[10];
		results = result.split(":");
		String answer = results[results.length - 1];
		answer = answer.substring(1, answer.length() - 2);
		System.out.println(answer);
	}
}