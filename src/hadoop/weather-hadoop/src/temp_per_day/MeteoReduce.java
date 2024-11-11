package temp_per_day;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class MeteoReduce extends Reducer<Text, FloatWritable, Text, FloatWritable> {
    private FloatWritable temp_writer = new FloatWritable();

    @Override
    protected void reduce(Text key, Iterable<FloatWritable> values, Context context) throws IOException, InterruptedException {
        
    	float tmp = 0;
    	int i = 0;
    	
        for (FloatWritable value : values) {
            tmp += value.get();
            i += 1;
        }
        
        tmp /= i;
        
        temp_writer.set(tmp);
        context.write(key, temp_writer);
    }
}
