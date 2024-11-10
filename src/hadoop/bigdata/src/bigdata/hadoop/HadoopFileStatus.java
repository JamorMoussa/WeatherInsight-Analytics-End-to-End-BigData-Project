package bigdata.hadoop;


import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

public class HadoopFileStatus {

	public static void main(String[] args) throws IOException{
		
		Configuration conf = new Configuration();
		
		FileSystem fs = FileSystem.get(conf);
	
		Path path = new Path(args[0], args[1]);
		
		FileStatus infos = fs.getFileStatus(path);
		
		System.out.println(infos.getLen() + " Bytes");
		
		fs.rename(path, new Path(args[0], args[2]));
		
		fs.close();
	}

}
