import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
/* add some more imports */

public class FetchAndProcessFromNetworkFast implements FetchAndProcess {
    private Map<String, String> data;

    @Override
    public Map<String, String> exposeData() {
	return data;
    }

    @Override
    public void fetch(List<String> paths) {	
	// Implement here, just do it parallely!
    }

    @Override
    public List<String> process() {
	// Implement here
	// Can you make use of the default implementation here?
	// See https://dzone.com/articles/interface-default-methods-java

	return null;
    }
}
