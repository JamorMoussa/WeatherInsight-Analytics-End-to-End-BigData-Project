package bigdata.hadoop.mapreduce.calls;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CallsMapper extends Mapper<Object, Text, Text, IntWritable>{
	
	private Text name = new Text();
	private IntWritable time = new IntWritable();
	
	// "2:38"
	public int get_time(String timestr) {
		String[] times = timestr.split(":");
		
		int time = Integer.parseInt(times[0]) * 60 + Integer.parseInt(times[1]);
		
		return time;
	}
	
	public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
		
		String line = value.toString();
		
		String[] tokens = line.split("\\|");
		
		name.set(tokens[0]);
		time.set(get_time(tokens[2]));
		
		context.write(name, time);
	
		
	}

}
