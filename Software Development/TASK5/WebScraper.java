import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.FileWriter;
import java.io.IOException;

public class WebScraper {
    public static void main(String[] args) {
        String url = "https://example-ecommerce-site.com/products"; // Replace with a real e-commerce site
        try {
            Document doc = Jsoup.connect(url).get();
            Elements products = doc.select(".product-item"); // Replace with actual CSS selector
            FileWriter writer = new FileWriter("products.csv");
            writer.write("Name,Price,Rating\n");

            for (Element product : products) {
                String name = product.select(".product-title").text(); // Replace with actual selector
                String price = product.select(".product-price").text(); // Replace with actual selector
                String rating = product.select(".product-rating").text(); // Replace with actual selector
                writer.write(name + "," + price + "," + rating + "\n");
            }

            writer.close();
            System.out.println("Data successfully saved to products.csv");
        } catch (IOException e) {
            System.err.println("Error fetching data: " + e.getMessage());
        }
    }
}
