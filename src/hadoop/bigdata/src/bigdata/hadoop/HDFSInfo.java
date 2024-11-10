package bigdata.hadoop;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;

public class HDFSInfo {

	public static void main(String[] args) throws IOException{
		
		Configuration conf = new Configuration();
		
		FileSystem fs = FileSystem.get(conf);
		
		Path fileName = new Path(args[0]);
		
		if (! fs.exists(fileName)) {
			System.out.println("Le fichier n'existe pas");
		}
		
		FileStatus infos = fs.getFileStatus(fileName);
		System.out.println(Long.toString(infos.getLen()) + " octets");
		
		BlockLocation[] blocks = fs.getFileBlockLocations(infos, 0,infos.getLen());
		
		System.out.println("le nombre de blocks est:"+ blocks.length + " blocs :");
		
		for(BlockLocation block : blocks) {
			System.out.println("\t" + block.toString() + "length" + block.getLength());
		}
		
		fs.close();
		
	}

}
