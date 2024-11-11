package temp_per_month;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class MeteoMap extends Mapper<Object, Text, Text, FloatWritable> {
    private Text month = new Text();
    private FloatWritable temperature = new FloatWritable();

    @Override
    protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        
        // Assuming line format: YYYYMMDD TEMP_OTHERDATA
        
        String[] splited_line = line.split("\t");
        
        String monthStr = splited_line[0].substring(0, 6).trim(); // Extract year
        String tempStr = splited_line[1]; // Assuming temperature is at a fixed position

        try {
            float temp = Float.parseFloat(tempStr.trim());
        	month.set(monthStr);
            temperature.set(temp);
            context.write(month, temperature);
            
        } catch (NumberFormatException e) {
           System.out.println("Error ..............................................");
        }
    }
}
