package temp_per_day;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class MeteoMap extends Mapper<Object, Text, Text, FloatWritable> {
    private static final float MISSING = (float) 99999.0; // Temperature missing value
    private Text year = new Text();
    private FloatWritable temperature = new FloatWritable();

    @Override
    protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        
        // Assuming line format: YYYYMMDD TEMP_OTHERDATA
        String yearStr = line.substring(15, 23); // Extract year
        String tempStr = line.substring(87, 93); // Assuming temperature is at a fixed position

        try {
            float temp = Float.parseFloat(tempStr.trim());
            if (temp != MISSING) {
                year.set(yearStr);
                temperature.set(temp/100);
                context.write(year, temperature);
            }
        } catch (NumberFormatException e) {
            // Skip lines with invalid data
        }
    }
}
