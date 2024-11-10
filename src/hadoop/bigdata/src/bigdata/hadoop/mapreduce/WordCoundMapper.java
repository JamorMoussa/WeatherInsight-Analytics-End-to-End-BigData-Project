package bigdata.hadoop.mapreduce;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class WordCoundMapper extends Mapper<Object, Text, Text, IntWritable>{

	private final static IntWritable one = new IntWritable(1);
	private Text word = new Text();

	public void map(Object key, Text value, Context context) throws IOException, InterruptedException{
		
		String line = value.toString();

		line.replaceAll("[.,;:?!'\"`()\\[\\]{}<>/|@#$%^&*\\+-=_~`]", " ");
		String[] words = line.split(" ");
		
		for(String token: words) {
			word.set(token);
			context.write(word, one);
		}
		
	}
}
