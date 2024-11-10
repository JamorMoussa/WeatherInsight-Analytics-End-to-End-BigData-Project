package bigdata.hadoop.mapreduce.calls;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class CallsReducer extends Reducer<Text, IntWritable, Text, IntWritable>{

	private IntWritable total_time = new IntWritable();
	
	public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
		
		int sum = 0;
		
		for(IntWritable value: values) {
			sum += value.get();
		}
		
		total_time.set(sum);
		
		context.write(key, total_time);
	}
}