package bigdata.hadoop.mapreduce.calls;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class CallsCounterJob {

	public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {

		Configuration conf = new Configuration();
		
		Job job = Job.getInstance(conf, "calls_counter_job");
		
		job.setJarByClass(CallsCounterJob.class);
		
		job.setMapperClass(CallsMapper.class);

		// job.setCombinerClass(CallsReducer.class);
		
		job.setReducerClass(CallsReducer.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		
		FileInputFormat.addInputPath(job, new Path(args[0]));
		
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
	
		System.exit(job.waitForCompletion(true) ? 0 : 1);
		
		
	}

}
